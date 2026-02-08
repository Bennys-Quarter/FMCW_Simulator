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
    QPushButton, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(357, 98)
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 20, 311, 48))
        self.frame_3.setMaximumSize(QSize(311, 48))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_27 = QLabel(self.frame_3)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_5.addWidget(self.label_27)

        self.label_30 = QLabel(self.frame_3)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_5.addWidget(self.label_30)

        self.label_31 = QLabel(self.frame_3)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_5.addWidget(self.label_31)

        self.label_34 = QLabel(self.frame_3)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_5.addWidget(self.label_34)

        self.label_29 = QLabel(self.frame_3)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_5.addWidget(self.label_29)

        self.label_32 = QLabel(self.frame_3)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_5.addWidget(self.label_32)

        self.label_33 = QLabel(self.frame_3)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_5.addWidget(self.label_33)

        self.toolButton = QToolButton(self.frame_3)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_5.addWidget(self.toolButton)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_5.addWidget(self.pushButton_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"T_X", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">v =</p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"XXX", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"m/s", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">d =</p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"XXX", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"m", None))
        self.toolButton.setText(QCoreApplication.translate("Form", u"...", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"X", None))
    # retranslateUi

