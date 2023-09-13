# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projectEntry.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListWidget, QListWidgetItem,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

from ui.components.projectEntry_Manage import ProjectEntry_Manage
from ui.components.samplesListWidget import SamplesListWidget

class Ui_ProjectEntry(object):
    def setupUi(self, ProjectEntry):
        if not ProjectEntry.objectName():
            ProjectEntry.setObjectName(u"ProjectEntry")
        ProjectEntry.resize(605, 488)
        self.verticalLayout = QVBoxLayout(ProjectEntry)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(ProjectEntry)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabManage = ProjectEntry_Manage()
        self.tabManage.setObjectName(u"tabManage")
        self.tabWidget.addTab(self.tabManage, "")
        self.tabClassify = QWidget()
        self.tabClassify.setObjectName(u"tabClassify")
        self.horizontalLayout = QHBoxLayout(self.tabClassify)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.unclassifiedListWidget = SamplesListWidget(self.tabClassify)
        self.unclassifiedListWidget.setObjectName(u"unclassifiedListWidget")

        self.horizontalLayout.addWidget(self.unclassifiedListWidget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tagsListWidget = QListWidget(self.tabClassify)
        self.tagsListWidget.setObjectName(u"tagsListWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tagsListWidget.sizePolicy().hasHeightForWidth())
        self.tagsListWidget.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.tagsListWidget)

        self.classfiedListWidget = SamplesListWidget(self.tabClassify)
        self.classfiedListWidget.setObjectName(u"classfiedListWidget")

        self.verticalLayout_2.addWidget(self.classfiedListWidget)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.tabClassify, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(ProjectEntry)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ProjectEntry)
    # setupUi

    def retranslateUi(self, ProjectEntry):
        ProjectEntry.setWindowTitle(QCoreApplication.translate("ProjectEntry", u"projectEntry", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabManage), QCoreApplication.translate("ProjectEntry", u"Manage", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabClassify), QCoreApplication.translate("ProjectEntry", u"Classify", None))
    # retranslateUi

