import importlib
import json
import logging
import os
import re
import time
from copy import deepcopy
from functools import cached_property
from pathlib import Path
from typing import Any
from hashlib import md5
from io import BytesIO

import cv2

PROJECTS_ROOT_PATH = Path("projects")
ACCEPT_EXTS = [".jpg", ".png"]


class Project:
    path: Path

    def __init__(self, path: Path):
        self.path = path
        self._tagValueDict = {}
        with open(self.path / "project.json", "r", encoding="utf-8") as jf:
            projectJson = json.loads(jf.read())
            self._tagValueDict: dict[str, Any] = projectJson["tagValueMap"]
            self.name = projectJson.get("name", self.path.name)
        self._tags = list(self._tagValueDict.keys())
        self._values = list(self._tagValueDict.values())

    def __repr__(self):
        return f"Project(path={repr(self.path)})"

    @cached_property
    def tags(self):
        return deepcopy(self._tags)

    @cached_property
    def values(self):
        return deepcopy(self.values)

    @cached_property
    def tagValueMap(self):
        return deepcopy(self._tagValueDict)

    @cached_property
    def tagsReExp(self):
        tagsDivided = "|".join(str(tag) for tag in self.tags)
        return re.compile(f"^({tagsDivided})\\^")

    @cached_property
    def sourcesPath(self):
        return self.path / "sources"

    @cached_property
    def samplesPath(self):
        return self.path / "samples"

    @cached_property
    def samplesUnclassifiedPath(self):
        return self.samplesPath / "unclassified"

    @cached_property
    def samplesClassifiedPath(self):
        return self.samplesPath / "classified"

    @cached_property
    def samplesIgnoredPath(self):
        return self.samplesPath / "ignored"

    def createFolders(self):
        folders = [
            self.sourcesPath,
            self.samplesClassifiedPath,
            self.samplesUnclassifiedPath,
            self.samplesIgnoredPath,
        ]

        for folder in folders:
            folder.mkdir(parents=True, exist_ok=True)

    def listPathFiles(self, path: Path, acceptSuffixes: list[str] = ACCEPT_EXTS):
        return [p for p in path.glob("**/*") if p.suffix in acceptSuffixes]

    @property
    def sources(self):
        return self.listPathFiles(self.sourcesPath)

    @property
    def samples(self):
        return self.listPathFiles(self.samplesPath)

    @property
    def samplesUnclassified(self):
        return self.listPathFiles(self.samplesUnclassifiedPath)

    @property
    def samplesClassified(self):
        return self.listPathFiles(self.samplesClassifiedPath)

    @property
    def samplesIgnored(self):
        return self.listPathFiles(self.samplesIgnoredPath)

    def samplesByTag(self, tag: str):
        if tag not in self.tags:
            raise ValueError(f'Unknown tag "{tag}"')

        samples = self.samples
        return [p for p in samples if p.stem.startswith(f"{tag}^")]

    def extractYield(self):
        cwdPath = Path(os.getcwd())
        importParts = [
            *self.path.resolve().relative_to(cwdPath.resolve()).parts,
            "extract",
        ]
        importName = ".".join(importParts)
        projectExtractModule = importlib.import_module(importName)
        getSamples = projectExtractModule.getSamples
        assert callable(getSamples)

        extractLogger = logging.getLogger(
            f"extract-{self.name}-{int(time.time() * 1000)}"
        )

        extractLogger.info("Reading existing samples MD5...")
        # existingSamplesMd5 = [
        #     self.getSampleOriginalFileName(sample).split(".")[0] for sample in samples
        # ]
        existingSamplesMd5 = []
        for sample in self.samples:
            with open(sample, "rb") as sf:
                existingSamplesMd5.append(md5(sf.read()).hexdigest())

        sources = self.sources
        sourcesNum = len(sources)
        for i, source in enumerate(sources):
            try:
                extractLogger.info(f"Extracting {source.resolve()}")
                samples = getSamples(source)
                for sample in samples:
                    success, sampleBuffer = cv2.imencode(".jpg", sample)
                    if not success:
                        extractLogger.warning(
                            f"cv2 cannot encode {sampleMd5} from {source.name}, skipping"
                        )
                        continue

                    sampleMd5 = md5(sampleBuffer).hexdigest()
                    if sampleMd5 in existingSamplesMd5:
                        extractLogger.debug(f"{sampleMd5} from {source.name} skipped")
                        continue

                    extractLogger.info(f"{sampleMd5} <- {source.name}")
                    sampleSavePath = self.samplesUnclassifiedPath / f"{sampleMd5}.jpg"
                    with open(sampleSavePath, "wb") as sf:
                        sf.write(sampleBuffer)
                    existingSamplesMd5.append(sampleMd5)
            except Exception:
                extractLogger.exception(f"Error extracting {source.resolve()}")
            finally:
                yield (source, i, sourcesNum)

    def extract(self):
        list(self.extractYield())

    def getSampleOriginalFileName(self, sample: Path):
        return self.tagsReExp.sub("", sample.name)

    def classify(self, sample: Path, tag: str):
        if tag not in self.tags:
            raise ValueError(f'Unknown tag "{tag}"')

        originalFileName = self.getSampleOriginalFileName(sample)
        classifiedFileName = f"{tag}^{originalFileName}"
        return sample.rename(self.samplesClassifiedPath / classifiedFileName)

    def unclassify(self, sample: Path):
        originalFileName = self.getSampleOriginalFileName(sample)
        return sample.rename(self.samplesUnclassifiedPath / originalFileName)

    def ignore(self, sample: Path):
        originalFileName = self.getSampleOriginalFileName(sample)
        return sample.rename(self.samplesIgnoredPath / originalFileName)


class Projects:
    def __init__(self, rootFolderPath=PROJECTS_ROOT_PATH):
        self.rootFolderPath = rootFolderPath
        self.projects: list[Project] = []
        self.detectProjects()

    def detectProjects(self):
        self.projects.clear()

        folders = [p for p in self.rootFolderPath.iterdir() if p.is_dir()]
        for folder in folders:
            if not (folder / "project.json").exists():
                continue
            project = Project(folder)
            if not (
                project.sourcesPath.exists()
                and project.samplesClassifiedPath.exists()
                and project.samplesUnclassifiedPath.exists()
                and project.samplesIgnoredPath.exists()
            ):
                continue
            self.projects.append(project)
