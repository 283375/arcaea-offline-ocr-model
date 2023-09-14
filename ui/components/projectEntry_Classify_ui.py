# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projectEntry_Classify.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from ui.extends.samplesListWidget import SamplesListWidget

class Ui_ProjectEntry_Classify(object):
    def setupUi(self, ProjectEntry_Classify):
        if not ProjectEntry_Classify.objectName():
            ProjectEntry_Classify.setObjectName(u"ProjectEntry_Classify")
        ProjectEntry_Classify.resize(677, 523)
        ProjectEntry_Classify.setWindowTitle(u"ProjectEntry_Classify")
        self.horizontalLayout = QHBoxLayout(ProjectEntry_Classify)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.samplesListWidget = SamplesListWidget(ProjectEntry_Classify)
        self.samplesListWidget.setObjectName(u"samplesListWidget")

        self.horizontalLayout.addWidget(self.samplesListWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.loadSamplesButton = QPushButton(ProjectEntry_Classify)
        self.loadSamplesButton.setObjectName(u"loadSamplesButton")

        self.verticalLayout.addWidget(self.loadSamplesButton)

        self.frame = QFrame(ProjectEntry_Classify)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(100, 200))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(ProjectEntry_Classify)

        QMetaObject.connectSlotsByName(ProjectEntry_Classify)
    # setupUi

    def retranslateUi(self, ProjectEntry_Classify):
        self.loadSamplesButton.setText(QCoreApplication.translate("ProjectEntry_Classify", u"Load samples", None))
        pass
    # retranslateUi

