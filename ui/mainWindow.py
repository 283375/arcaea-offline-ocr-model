from PySide6.QtCore import Qt
from PySide6.QtWidgets import QListWidgetItem, QMainWindow, QSizePolicy, QWidget

from .mainWindow_ui import Ui_MainWindow
from .tabs.tabProjects import TabProjects


class MainWindow(Ui_MainWindow, QMainWindow):
    TabWidgetTypeRole = Qt.ItemDataRole.UserRole + 10

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.tabsListWidget.itemClicked.connect(self.setItemSelected)
        self.tabsListWidget.currentItemChanged.connect(self.switchTab)

        projectsItem = QListWidgetItem("Projects", self.tabsListWidget)
        projectsItem.setData(self.TabWidgetTypeRole, TabProjects)
        self.tabsListWidget.addItem(projectsItem)

        self.tabsListWidget.setMaximumWidth(
            self.tabsListWidget.sizeHintForColumn(0) + 10
        )

        self.tabsListWidget.setCurrentIndex(self.tabsListWidget.model().index(0, 0))

    def setItemSelected(self, item: QListWidgetItem):
        item.setSelected(True)

    def switchTab(self):
        item = self.tabsListWidget.currentItem()

        tabWidgetType = item.data(self.TabWidgetTypeRole)
        tabWidget: QWidget = tabWidgetType(self)
        # tabWidget.setSizePolicy(
        #     QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        # )

        self.centralWidget().layout().removeWidget(self.tabWidget)
        self.tabWidget.deleteLater()
        self.centralWidget().layout().addWidget(tabWidget)
        self.tabWidget = tabWidget
