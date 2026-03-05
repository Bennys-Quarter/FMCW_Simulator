# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'target_List_Entry.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QToolButton, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(280, 45)
        self.horizontalLayout = QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.l_target = QLabel(Frame)
        self.l_target.setObjectName(u"l_target")

        self.horizontalLayout_5.addWidget(self.l_target)

        self.label_30 = QLabel(Frame)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_5.addWidget(self.label_30)

        self.l_velocity = QLabel(Frame)
        self.l_velocity.setObjectName(u"l_velocity")

        self.horizontalLayout_5.addWidget(self.l_velocity)

        self.label_34 = QLabel(Frame)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_5.addWidget(self.label_34)

        self.label_29 = QLabel(Frame)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_5.addWidget(self.label_29)

        self.l_distance = QLabel(Frame)
        self.l_distance.setObjectName(u"l_distance")

        self.horizontalLayout_5.addWidget(self.l_distance)

        self.label_33 = QLabel(Frame)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_5.addWidget(self.label_33)

        self.OptionsButton = QToolButton(Frame)
        self.OptionsButton.setObjectName(u"OptionsButton")

        self.horizontalLayout_5.addWidget(self.OptionsButton)

        self.ExitButton = QToolButton(Frame)
        self.ExitButton.setObjectName(u"ExitButton")

        self.horizontalLayout_5.addWidget(self.ExitButton)


        self.horizontalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.l_target.setText(QCoreApplication.translate("Frame", u"T_X", None))
        self.label_30.setText(QCoreApplication.translate("Frame", u"<html><head/><body><p align=\"right\">v =</p></body></html>", None))
        self.l_velocity.setText(QCoreApplication.translate("Frame", u"XXX", None))
        self.label_34.setText(QCoreApplication.translate("Frame", u"m/s", None))
        self.label_29.setText(QCoreApplication.translate("Frame", u"<html><head/><body><p align=\"right\">d =</p></body></html>", None))
        self.l_distance.setText(QCoreApplication.translate("Frame", u"XXX", None))
        self.label_33.setText(QCoreApplication.translate("Frame", u"m", None))
        self.OptionsButton.setText(QCoreApplication.translate("Frame", u"...", None))
        self.ExitButton.setText(QCoreApplication.translate("Frame", u"X", None))
    # retranslateUi

