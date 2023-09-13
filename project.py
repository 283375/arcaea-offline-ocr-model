import importlib
import logging
import os
import time
from copy import deepcopy
from functools import cached_property
from hashlib import md5
from pathlib import Path

import cv2
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from dbModels import ClassifiedSample, ProjectBase, Property, TagValue

PROJECTS_ROOT_PATH = Path("projects")
ACCEPT_EXTS = [".jpg", ".png"]


def initProject(path: Path):
    engine = create_engine(
        f"sqlite:///{(path / 'project.db').resolve().as_posix()}", poolclass=NullPool
    )
    ProjectBase.metadata.create_all(engine)
    (path / "sources").mkdir(parents=True, exist_ok=True)
    (path / "samples").mkdir(parents=True, exist_ok=True)


class Project:
    path: Path

    def __init__(self, path: Path):
        self.path = path

        self.__engine = create_engine(
            f"sqlite:///{(path / 'project.db').resolve().as_posix()}",
            poolclass=NullPool,
        )
        self.__sessionmaker = sessionmaker(self.__engine)
        self.reload()

    def reload(self):
        with self.__sessionmaker() as session:
            nameProperty = session.scalar(
                select(Property).where(Property.key == "name")
            )
            self.__name = nameProperty.value if nameProperty else self.path.name

            self._tagValueDict = {}
            tagValues = session.scalars(select(TagValue))
            for tagValue in tagValues:
                self._tagValueDict[tagValue.tag] = tagValue.value
            self._tags = list(self._tagValueDict.keys())
            self._values = list(self._tagValueDict.values())

        # expire property caches
        # https://stackoverflow.com/a/69367025/16484891, CC BY-SA 4.0
        self.__dict__.pop("name", None)
        self.__dict__.pop("tags", None)
        self.__dict__.pop("values", None)
        self.__dict__.pop("tagValueMap", None)

    def __repr__(self):
        return f"Project(path={repr(self.path)})"

    @property
    def name(self):
        return self.__name

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
    def sourcesPath(self):
        return self.path / "sources"

    @cached_property
    def samplesPath(self):
        return self.path / "samples"

    def listPathFiles(self, path: Path, acceptSuffixes: list[str] = ACCEPT_EXTS):
        return [p for p in path.glob("**/*") if p.suffix in acceptSuffixes]

    @property
    def sources(self):
        return self.listPathFiles(self.sourcesPath)

    @property
    def samples(self):
        return self.listPathFiles(self.samplesPath)

    @property
    def samplesClassified(self):
        with self.__sessionmaker() as session:
            return [
                cs.sampleNumpyMd5 for cs in session.scalars(select(ClassifiedSample))
            ]

    @property
    def samplesIgnored(self):
        with self.__sessionmaker() as session:
            return [
                cs.sampleNumpyMd5
                for cs in session.scalars(
                    select(ClassifiedSample).where(ClassifiedSample.tag == "ignored")
                )
            ]

    @property
    def samplesUnclassified(self):
        samplesNumpyMd5s = [s.stem for s in self.samples]
        classifiedSamples = []
        classifiedSamples += self.samplesClassified
        classifiedSamples += self.samplesIgnored
        return [s for s in samplesNumpyMd5s if s not in classifiedSamples]

    def samplesByTag(self, tag: str):
        if tag != "ignored" and tag not in self.tags:
            raise ValueError(f'Unknown tag "{tag}"')

        with self.__sessionmaker() as session:
            return [
                cs.sampleNumpyMd5
                for cs in session.scalars(
                    select(ClassifiedSample).where(ClassifiedSample.tag == tag)
                )
            ]

    def getModule(self, moduleName: str):
        cwdPath = Path(os.getcwd())
        importParts = [
            *self.path.resolve().relative_to(cwdPath.resolve()).parts,
            moduleName,
        ]
        importName = ".".join(importParts)
        return importlib.import_module(importName)

    def extractSamplesYield(self):
        extractModule = self.getModule("extract")
        getSamples = extractModule.extractSamples
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
                    sampleSavePath = self.samplesPath / f"{sampleMd5}.jpg"
                    with open(sampleSavePath, "wb") as sf:
                        sf.write(sampleBuffer)
                    existingSamplesMd5.append(sampleMd5)
            except Exception:
                extractLogger.exception(f"Error extracting {source.resolve()}")
            finally:
                yield (source, i, sourcesNum)

    def extractSamples(self):
        list(self.extractSamplesYield())

    def redactSourcesYield(self):
        redactModule = self.getModule("redact")
        redactSource = redactModule.redactSource
        assert callable(redactSource)

        redactLogger = logging.getLogger(
            f"redact-{self.name}-{int(time.time() * 1000)}"
        )

        sources = self.sources
        sourcesNum = len(sources)
        for i, source in enumerate(sources):
            try:
                redactLogger.info(f"Redacting {source.resolve()}")
                redactSource(source)
            except Exception:
                redactLogger.exception(f"Error redacting {source.resolve()}")
            finally:
                yield (source, i, sourcesNum)

    def redactSources(self):
        list(self.redactSourcesYield())

    def classify(self, sample: Path, tag: str):
        if tag not in self.tags:
            raise ValueError(f'Unknown tag "{tag}"')

        with self.__sessionmaker() as session:
            cs = ClassifiedSample()
            cs.sampleNumpyMd5 = sample.stem
            cs.tag = tag
            session.add(cs)
            session.commit()

    def unclassify(self, sample: Path):
        with self.__sessionmaker() as session:
            cs = ClassifiedSample()
            cs.sampleNumpyMd5 = sample.stem
            session.delete(cs)
            session.commit()

    def ignore(self, sample: Path):
        self.classify(sample, "ignored")


class Projects:
    def __init__(self, rootFolderPath=PROJECTS_ROOT_PATH):
        self.rootFolderPath = rootFolderPath
        self.projects: list[Project] = []
        self.detectProjects()

    def detectProjects(self):
        self.projects.clear()

        folders = [p for p in self.rootFolderPath.iterdir() if p.is_dir()]
        for folder in folders:
            if not (folder / "project.db").exists():
                continue
            project = Project(folder)
            if not (project.sourcesPath.exists() and project.samplesPath.exists()):
                continue
            self.projects.append(project)
