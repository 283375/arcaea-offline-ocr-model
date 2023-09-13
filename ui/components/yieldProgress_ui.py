# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'yieldProgress.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_YieldProgress(object):
    def setupUi(self, YieldProgress):
        if not YieldProgress.objectName():
            YieldProgress.setObjectName(u"YieldProgress")
        YieldProgress.resize(450, 200)
        YieldProgress.setWindowTitle(u"YieldProgress")
        self.verticalLayout = QVBoxLayout(YieldProgress)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(YieldProgress)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.progressBar = QProgressBar(YieldProgress)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximum(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setFormat(u"%v/%m %p%")

        self.verticalLayout.addWidget(self.progressBar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.abortButton = QPushButton(YieldProgress)
        self.abortButton.setObjectName(u"abortButton")

        self.horizontalLayout.addWidget(self.abortButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(YieldProgress)

        QMetaObject.connectSlotsByName(YieldProgress)
    # setupUi

    def retranslateUi(self, YieldProgress):
        self.label.setText(QCoreApplication.translate("YieldProgress", u"...", None))
        self.abortButton.setText(QCoreApplication.translate("YieldProgress", u"Abort", None))
        pass
    # retranslateUi

