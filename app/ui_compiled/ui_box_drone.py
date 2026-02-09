# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'box_drone.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from app.resources import icons_rc
from app.resources import icons_rc

class Ui_Box_Drone(object):
    def setupUi(self, Box_Drone):
        if not Box_Drone.objectName():
            Box_Drone.setObjectName(u"Box_Drone")
        Box_Drone.resize(311, 90)
        self.verticalLayout = QVBoxLayout(Box_Drone)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_24 = QLabel(Box_Drone)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setEnabled(True)
        self.label_24.setMaximumSize(QSize(60, 60))
        self.label_24.setAutoFillBackground(False)
        self.label_24.setPixmap(QPixmap(u":/drone_icon/drone_icon.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setWordWrap(False)

        self.horizontalLayout_6.addWidget(self.label_24)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.label_23 = QLabel(Box_Drone)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_6.addWidget(self.label_23)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.retranslateUi(Box_Drone)

        QMetaObject.connectSlotsByName(Box_Drone)
    # setupUi

    def retranslateUi(self, Box_Drone):
        Box_Drone.setWindowTitle(QCoreApplication.translate("Box_Drone", u"GroupBox", None))
        self.label_24.setText("")
        self.label_23.setText(QCoreApplication.translate("Box_Drone", u"<html><head/><body><p>Drone</p></body></html>", None))
    # retranslateUi

