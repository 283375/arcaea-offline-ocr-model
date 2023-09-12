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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

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
        self.tabManage = QWidget()
        self.tabManage.setObjectName(u"tabManage")
        self.gridLayout = QGridLayout(self.tabManage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.tabManage)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)

        self.projectNameLabel = QLabel(self.tabManage)
        self.projectNameLabel.setObjectName(u"projectNameLabel")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.projectNameLabel.setFont(font)

        self.gridLayout.addWidget(self.projectNameLabel, 0, 0, 1, 2)

        self.pushButton_2 = QPushButton(self.tabManage)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)

        self.projectDescriptionLabel = QLabel(self.tabManage)
        self.projectDescriptionLabel.setObjectName(u"projectDescriptionLabel")

        self.gridLayout.addWidget(self.projectDescriptionLabel, 1, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 2)

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
        self.pushButton.setText(QCoreApplication.translate("ProjectEntry", u"Extract", None))
        self.projectNameLabel.setText(QCoreApplication.translate("ProjectEntry", u"-", None))
        self.pushButton_2.setText(QCoreApplication.translate("ProjectEntry", u"...", None))
        self.projectDescriptionLabel.setText(QCoreApplication.translate("ProjectEntry", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabManage), QCoreApplication.translate("ProjectEntry", u"Manage", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabClassify), QCoreApplication.translate("ProjectEntry", u"Classify", None))
    # retranslateUi

