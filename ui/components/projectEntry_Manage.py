from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QApplication, QWidget

from project import Project

from .projectEntry_Manage_ui import Ui_ProjectEntry_Manage
from .yieldProgress import YieldProgress


class ProjectEntry_Manage(Ui_ProjectEntry_Manage, QWidget):
    reloadProject = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.project = None
        self.abort = False

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

    def setAbort(self, b: bool):
        self.abort = b

    @Slot()
    def on_extractButton_clicked(self):
        if not self.project:
            return

        progressDialog = YieldProgress(self)
        progressDialog.setWindowModality(Qt.WindowModality.ApplicationModal)

        self.abort = False
        progressDialog.abortButton.clicked.connect(lambda: self.setAbort(True))

        progressDialog.show()

        iterator = iter(self.project.extractSamplesYield())
        progressDialog.progressBar.setMinimum(0)
        while not self.abort:
            try:
                path, i, total = next(iterator)
                progressDialog.label.setText(path.name)
                progressDialog.progressBar.setValue(i)
                if i <= 2:
                    progressDialog.progressBar.setMaximum(total)

                if total > 10 and i % 10 == 0 or total <= 10:
                    progressDialog.update()
                    QApplication.processEvents()
            except StopIteration:
                break

        self.abort = False
        self.reloadProject.emit()
        progressDialog.close()
        progressDialog.deleteLater()

    @Slot()
    def on_redactSourcesButton_clicked(self):
        if not self.project:
            return

        progressDialog = YieldProgress(self)
        progressDialog.setWindowModality(Qt.WindowModality.ApplicationModal)

        self.abort = False
        progressDialog.abortButton.clicked.connect(lambda: self.setAbort(True))

        progressDialog.show()

        iterator = iter(self.project.redactSourcesYield())
        progressDialog.progressBar.setMinimum(0)
        while not self.abort:
            try:
                path, i, total = next(iterator)
                progressDialog.label.setText(path.name)
                progressDialog.progressBar.setValue(i)
                if i <= 2:
                    progressDialog.progressBar.setMaximum(total)

                if total > 10 and i % 10 == 0 or total <= 10:
                    progressDialog.update()
                    QApplication.processEvents()
            except StopIteration:
                break

        self.abort = False
        progressDialog.close()
        progressDialog.deleteLater()
