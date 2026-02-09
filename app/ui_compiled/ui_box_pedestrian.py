# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'box_pedestrian.ui'
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

class Ui_BoxPedestrian(object):
    def setupUi(self, BoxPedestrian):
        if not BoxPedestrian.objectName():
            BoxPedestrian.setObjectName(u"BoxPedestrian")
        BoxPedestrian.resize(311, 90)
        self.verticalLayout = QVBoxLayout(BoxPedestrian)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pedestrian_layout = QHBoxLayout()
        self.pedestrian_layout.setObjectName(u"pedestrian_layout")
        self.label_26 = QLabel(BoxPedestrian)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(60, 60))
        self.label_26.setPixmap(QPixmap(u":/pedestrian_icon/pedestrian_icon.png"))
        self.label_26.setScaledContents(True)

        self.pedestrian_layout.addWidget(self.label_26)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.pedestrian_layout.addItem(self.horizontalSpacer)

        self.label_21 = QLabel(BoxPedestrian)
        self.label_21.setObjectName(u"label_21")

        self.pedestrian_layout.addWidget(self.label_21)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.pedestrian_layout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.pedestrian_layout)


        self.retranslateUi(BoxPedestrian)

        QMetaObject.connectSlotsByName(BoxPedestrian)
    # setupUi

    def retranslateUi(self, BoxPedestrian):
        BoxPedestrian.setWindowTitle(QCoreApplication.translate("BoxPedestrian", u"GroupBox", None))
        self.label_26.setText("")
        self.label_21.setText(QCoreApplication.translate("BoxPedestrian", u"<html><head/><body><p>Pedestrian</p></body></html>", None))
    # retranslateUi

