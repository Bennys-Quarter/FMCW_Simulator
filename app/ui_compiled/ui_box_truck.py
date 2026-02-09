# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'box_truck.ui'
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
    QSizePolicy, QSpacerItem, QWidget)
from app.resources import icons_rc
from app.resources import icons_rc

class Ui_BoxTruck(object):
    def setupUi(self, BoxTruck):
        if not BoxTruck.objectName():
            BoxTruck.setObjectName(u"BoxTruck")
        BoxTruck.resize(311, 90)
        self.horizontalLayout = QHBoxLayout(BoxTruck)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_25 = QLabel(BoxTruck)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(80, 60))
        self.label_25.setPixmap(QPixmap(u":/truck_icon/truck_icon.png"))
        self.label_25.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_25)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.label_22 = QLabel(BoxTruck)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_4.addWidget(self.label_22)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.horizontalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(BoxTruck)

        QMetaObject.connectSlotsByName(BoxTruck)
    # setupUi

    def retranslateUi(self, BoxTruck):
        BoxTruck.setWindowTitle(QCoreApplication.translate("BoxTruck", u"GroupBox", None))
        self.label_25.setText("")
        self.label_22.setText(QCoreApplication.translate("BoxTruck", u"<html><head/><body><p>Truck</p></body></html>", None))
    # retranslateUi

