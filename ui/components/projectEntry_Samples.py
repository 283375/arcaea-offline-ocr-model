import logging

from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QListWidgetItem, QWidget

from project import Project

from ..extends.samplesListWidget import SamplesListWidget
from .blockLabelDialog import BlockLabelDialog
from .projectEntry_Samples_ui import Ui_ProjectEntry_Samples

logger = logging.getLogger(__name__)


class ProjectEntry_Samples(Ui_ProjectEntry_Samples, QWidget):
    TagRole = Qt.ItemDataRole.UserRole + 1

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.samplesListWidget.setDragEnabled(False)

        self.project = None

    def setProject(self, project: Project):
        self.project = project
        self.updateSampleTags()

    def updateSampleTags(self):
        self.tagsListWidget.clear()

        with BlockLabelDialog(self) as block:
            block.setText(f"{self.project.name}<br>Loading tags")
            block.show()
            for tag in self.project.tags + ["ignored"]:
                samples = self.project.samplesByTag(tag)
                item = QListWidgetItem(f"{tag} ({len(samples)} samples)")
                item.setData(self.TagRole, tag)
                self.tagsListWidget.addItem(item)

    @Slot()
    def on_loadSamplesButton_clicked(self):
        tag = self.tagsListWidget.currentItem().data(self.TagRole)
        samples = self.project.samplesByTag(tag)
        self.samplesListWidget.setSamples(samples, cancellable=False)

    @Slot()
    def on_reloadButton_clicked(self):
        self.updateSampleTags()

    @Slot()
    def on_unclassifyButton_clicked(self):
        selectedSampleItems = self.samplesListWidget.selectedItems()
        paths = [
            item.data(SamplesListWidget.PathlibPathRole) for item in selectedSampleItems
        ]
        for item, path in zip(selectedSampleItems, paths):
            try:
                self.project.unclassify(path)
                index = self.samplesListWidget.indexFromItem(item)
                self.samplesListWidget.model().removeRow(index.row())
            except Exception:
                logger.exception(f"cannot unclassify {path}")
