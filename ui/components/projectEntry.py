from PySide6.QtWidgets import QWidget

from project import Project

from .projectEntry_ui import Ui_ProjectEntry


class ProjectEntry(Ui_ProjectEntry, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.project = None

    def setProject(self, project: Project):
        self.project = project
        self.updateLabels()

    def updateLabels(self):
        if not self.project:
            self.projectNameLabel.setText("-")
            self.projectDescriptionLabel.setText("-")
            return

        self.projectNameLabel.setText(self.project.name)
        self.projectDescriptionLabel.setText(
            "<br>".join(
                [
                    str(self.project.path.resolve()),
                    f"{len(self.project.sources)} sources",
                    f"{len(self.project.samples)} samples ({len(self.project.samplesUnclassified)} unclassified)",
                ]
            )
        )
