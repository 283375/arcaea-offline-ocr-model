# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projectEntry_Manage.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_ProjectEntry_Manage(object):
    def setupUi(self, ProjectEntry_Manage):
        if not ProjectEntry_Manage.objectName():
            ProjectEntry_Manage.setObjectName(u"ProjectEntry_Manage")
        ProjectEntry_Manage.resize(500, 400)
        ProjectEntry_Manage.setWindowTitle(u"ProjectEntry_Manage")
        self.gridLayout = QGridLayout(ProjectEntry_Manage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.projectDescriptionLabel = QLabel(ProjectEntry_Manage)
        self.projectDescriptionLabel.setObjectName(u"projectDescriptionLabel")

        self.gridLayout.addWidget(self.projectDescriptionLabel, 1, 0, 1, 2)

        self.extractButton = QPushButton(ProjectEntry_Manage)
        self.extractButton.setObjectName(u"extractButton")

        self.gridLayout.addWidget(self.extractButton, 3, 0, 1, 1)

        self.projectNameLabel = QLabel(ProjectEntry_Manage)
        self.projectNameLabel.setObjectName(u"projectNameLabel")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.projectNameLabel.setFont(font)

        self.gridLayout.addWidget(self.projectNameLabel, 0, 0, 1, 2)

        self.redactSourcesButton = QPushButton(ProjectEntry_Manage)
        self.redactSourcesButton.setObjectName(u"redactSourcesButton")

        self.gridLayout.addWidget(self.redactSourcesButton, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 2)

        self.updateButton = QPushButton(ProjectEntry_Manage)
        self.updateButton.setObjectName(u"updateButton")

        self.gridLayout.addWidget(self.updateButton, 2, 0, 1, 1)


        self.retranslateUi(ProjectEntry_Manage)

        QMetaObject.connectSlotsByName(ProjectEntry_Manage)
    # setupUi

    def retranslateUi(self, ProjectEntry_Manage):
        self.projectDescriptionLabel.setText(QCoreApplication.translate("ProjectEntry_Manage", u"-", None))
        self.extractButton.setText(QCoreApplication.translate("ProjectEntry_Manage", u"Extract", None))
        self.projectNameLabel.setText(QCoreApplication.translate("ProjectEntry_Manage", u"-", None))
        self.redactSourcesButton.setText(QCoreApplication.translate("ProjectEntry_Manage", u"Redact sources", None))
        self.updateButton.setText(QCoreApplication.translate("ProjectEntry_Manage", u"Update", None))
        pass
    # retranslateUi

