from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidgetItem, QWidget

from project import Project, Projects

from ..components.projectEntry import ProjectEntry
from .tabProjects_ui import Ui_TabProjects


class ProjectListWidgetItem(QListWidgetItem):
    ProjectRole = Qt.ItemDataRole.UserRole

    def __init__(self, project: Project, parent=None):
        super().__init__(parent, QListWidgetItem.ItemType.Type)
        self.setData(Qt.ItemDataRole.DisplayRole, project.name)
        self.setData(self.ProjectRole, project)


class TabProjects(Ui_TabProjects, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.projectListWidget.itemClicked.connect(
            self.projectListWidget.setCurrentItem
        )
        self.projectListWidget.currentItemChanged.connect(self.switchProject)

        self.detectProjects()

    def detectProjects(self):
        ps = Projects()
        ps.detectProjects()
        projects = ps.projects
        for project in projects:
            item = ProjectListWidgetItem(project, self.projectListWidget)
            self.projectListWidget.addItem(item)

        self.projectListWidget.setMaximumWidth(
            self.projectListWidget.sizeHintForColumn(0) + 10
        )

    def switchProject(self):
        item = self.projectListWidget.currentItem()
        project: Project = item.data(ProjectListWidgetItem.ProjectRole)

        projectEntry = ProjectEntry(self)
        projectEntry.setProject(project)

        self.layout().removeWidget(self.projectEntry)
        self.projectEntry.deleteLater()
        self.layout().addWidget(projectEntry)
        self.projectEntry = projectEntry
