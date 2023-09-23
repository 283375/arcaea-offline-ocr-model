import json
from pathlib import Path

from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QLabel, QWidget

from project import Project

from .projectEntry_Classify_ui import Ui_ProjectEntry_Classify


class TagLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)

        self.project: Project | None = None
        self.tag = None

    def enableDropEffect(self):
        # palette = self.palette()
        # palette.setBrush(QPalette.ColorRole.Base, palette.highlight())
        # palette.setBrush(QPalette.ColorRole.Window, palette.highlight())
        # palette.setBrush(QPalette.ColorRole.Text, palette.highlightedText())
        # self.setPalette(palette)
        font = self.font()
        font.setBold(True)
        font.setUnderline(True)
        self.setFont(font)

    def disableDropEffect(self):
        # palette = self.palette()
        # palette.setBrush(QPalette.ColorRole.Base, palette.base())
        # palette.setBrush(QPalette.ColorRole.Window, palette.window())
        # palette.setBrush(QPalette.ColorRole.Text, palette.text())
        # self.setPalette(palette)
        font = self.font()
        font.setBold(False)
        font.setUnderline(False)
        self.setFont(font)

    def dragEnterEvent(self, event: QDragEnterEvent):
        mimeData = event.mimeData()
        if mimeData.hasFormat("application/ao-ocr-model_sample"):
            self.enableDropEffect()
            event.accept()

    def dragLeaveEvent(self, event):
        self.disableDropEffect()
        return super().dragLeaveEvent(event)

    def dropEvent(self, event: QDropEvent):
        if self.project and self.tag and event.dropAction() == Qt.DropAction.MoveAction:
            data = bytes(event.mimeData().data("application/ao-ocr-model_sample"))
            paths = json.loads(data.decode("utf-8"))
            paths = [Path(p) for p in paths]
            for path in paths:
                self.project.classify(path, self.tag)
            event.acceptProposedAction()

        if not event.isAccepted():
            event.ignore()
        self.disableDropEffect()


class ProjectEntry_Classify(Ui_ProjectEntry_Classify, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.project = None

        self.tagLabels: list[TagLabel] = []

    def setProject(self, project: Project):
        self.project = project

        for tagLabel in self.tagLabels:
            self.frame.layout().removeWidget(tagLabel)
            tagLabel.deleteLater()

        for tag in self.project.tags + ["ignored"]:
            tagLabel = TagLabel(self)
            tagLabel.tag = tag
            tagLabel.project = project
            tagLabel.setText(tag)
            self.frame.layout().addWidget(tagLabel)
            self.tagLabels.append(tagLabel)

    @Slot()
    def on_loadSamplesButton_clicked(self):
        self.samplesListWidget.setSamples(self.project.samplesUnclassified)
