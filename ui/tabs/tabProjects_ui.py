# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabProjects.ui'
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
    QSizePolicy, QWidget)

class Ui_TabProjects(object):
    def setupUi(self, TabProjects):
        if not TabProjects.objectName():
            TabProjects.setObjectName(u"TabProjects")
        TabProjects.resize(701, 582)
        TabProjects.setWindowTitle(u"TabProjects")
        self.horizontalLayout = QHBoxLayout(TabProjects)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.projectListWidget = QListWidget(TabProjects)
        self.projectListWidget.setObjectName(u"projectListWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectListWidget.sizePolicy().hasHeightForWidth())
        self.projectListWidget.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.projectListWidget)

        self.projectEntry = QWidget(TabProjects)
        self.projectEntry.setObjectName(u"projectEntry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.projectEntry.sizePolicy().hasHeightForWidth())
        self.projectEntry.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.projectEntry)


        self.retranslateUi(TabProjects)

        QMetaObject.connectSlotsByName(TabProjects)
    # setupUi

    def retranslateUi(self, TabProjects):
        pass
    # retranslateUi

