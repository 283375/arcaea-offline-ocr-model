from PySide6.QtWidgets import QWidget

from project import Project

from .projectEntry_ui import Ui_ProjectEntry


class ProjectEntry(Ui_ProjectEntry, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.project = None

        self.tabManage.reloadProject.connect(self.reloadProject)

    def setProject(self, project: Project):
        self.project = project
        self.tabManage.setProject(project)
        self.tabClassify.setProject(project)

    def reloadProject(self):
        self.project.reload()
        self.setProject(self.project)
