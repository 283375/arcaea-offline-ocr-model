# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logViewer.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHeaderView, QLabel, QSizePolicy, QSlider,
    QSpacerItem, QTreeView, QVBoxLayout, QWidget)

class Ui_LogViewer(object):
    def setupUi(self, LogViewer):
        if not LogViewer.objectName():
            LogViewer.setObjectName(u"LogViewer")
        LogViewer.resize(597, 443)
        LogViewer.setWindowTitle(u"LogViewer")
        self.verticalLayout = QVBoxLayout(LogViewer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(LogViewer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)

        self.groupComboBox = QComboBox(self.frame)
        self.groupComboBox.setObjectName(u"groupComboBox")

        self.gridLayout.addWidget(self.groupComboBox, 0, 4, 1, 1)

        self.levelLabel = QLabel(self.frame)
        self.levelLabel.setObjectName(u"levelLabel")

        self.gridLayout.addWidget(self.levelLabel, 0, 0, 1, 1)

        self.levelSlider = QSlider(self.frame)
        self.levelSlider.setObjectName(u"levelSlider")
        self.levelSlider.setMaximum(5)
        self.levelSlider.setSingleStep(1)
        self.levelSlider.setPageStep(1)
        self.levelSlider.setValue(2)
        self.levelSlider.setTracking(True)
        self.levelSlider.setOrientation(Qt.Horizontal)
        self.levelSlider.setTickPosition(QSlider.TicksBelow)

        self.gridLayout.addWidget(self.levelSlider, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(25, 10, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(4, 1)

        self.verticalLayout.addWidget(self.frame)

        self.logTreeView = QTreeView(LogViewer)
        self.logTreeView.setObjectName(u"logTreeView")

        self.verticalLayout.addWidget(self.logTreeView)


        self.retranslateUi(LogViewer)

        QMetaObject.connectSlotsByName(LogViewer)
    # setupUi

    def retranslateUi(self, LogViewer):
        self.label.setText(QCoreApplication.translate("LogViewer", u"Group", None))
        self.levelLabel.setText(QCoreApplication.translate("LogViewer", u"INFO", None))
        pass
    # retranslateUi

