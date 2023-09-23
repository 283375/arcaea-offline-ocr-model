# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projectEntry_Samples.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

from ui.extends.samplesListWidget import SamplesListWidget

class Ui_ProjectEntry_Samples(object):
    def setupUi(self, ProjectEntry_Samples):
        if not ProjectEntry_Samples.objectName():
            ProjectEntry_Samples.setObjectName(u"ProjectEntry_Samples")
        ProjectEntry_Samples.resize(648, 504)
        ProjectEntry_Samples.setWindowTitle(u"ProjectEntry_Samples")
        self.horizontalLayout = QHBoxLayout(ProjectEntry_Samples)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tagsListWidget = QListWidget(ProjectEntry_Samples)
        self.tagsListWidget.setObjectName(u"tagsListWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tagsListWidget.sizePolicy().hasHeightForWidth())
        self.tagsListWidget.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.tagsListWidget)

        self.loadSamplesButton = QPushButton(ProjectEntry_Samples)
        self.loadSamplesButton.setObjectName(u"loadSamplesButton")

        self.verticalLayout_2.addWidget(self.loadSamplesButton)

        self.reloadButton = QPushButton(ProjectEntry_Samples)
        self.reloadButton.setObjectName(u"reloadButton")

        self.verticalLayout_2.addWidget(self.reloadButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.samplesListWidget = SamplesListWidget(ProjectEntry_Samples)
        self.samplesListWidget.setObjectName(u"samplesListWidget")

        self.horizontalLayout.addWidget(self.samplesListWidget)

        self.frame = QFrame(ProjectEntry_Samples)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.unclassifyButton = QPushButton(self.frame)
        self.unclassifyButton.setObjectName(u"unclassifyButton")

        self.verticalLayout.addWidget(self.unclassifyButton)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(ProjectEntry_Samples)

        QMetaObject.connectSlotsByName(ProjectEntry_Samples)
    # setupUi

    def retranslateUi(self, ProjectEntry_Samples):
        self.loadSamplesButton.setText(QCoreApplication.translate("ProjectEntry_Samples", u"Load >", None))
        self.reloadButton.setText(QCoreApplication.translate("ProjectEntry_Samples", u"Reload", None))
        self.unclassifyButton.setText(QCoreApplication.translate("ProjectEntry_Samples", u"Unclassify", None))
        pass
    # retranslateUi

