# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup_target_setting.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(305, 255)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 281, 231))
        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 30, 261, 192))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_12 = QLabel(self.horizontalLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 5, 2, 1, 1)

        self.label_10 = QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 3, 2, 1, 1)

        self.lineEdit_v_start = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_v_start.setObjectName(u"lineEdit_v_start")

        self.gridLayout.addWidget(self.lineEdit_v_start, 4, 1, 1, 1)

        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.label_6 = QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)

        self.lineEdit_d = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_d.setObjectName(u"lineEdit_d")

        self.gridLayout.addWidget(self.lineEdit_d, 0, 1, 1, 1)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.lineEdit_v = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_v.setObjectName(u"lineEdit_v")

        self.gridLayout.addWidget(self.lineEdit_v, 1, 1, 1, 1)

        self.label_8 = QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)

        self.label_11 = QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 4, 2, 1, 1)

        self.lineEdit_d_start = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_d_start.setObjectName(u"lineEdit_d_start")

        self.gridLayout.addWidget(self.lineEdit_d_start, 2, 1, 1, 1)

        self.lineEdit_d_stop = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_d_stop.setObjectName(u"lineEdit_d_stop")

        self.gridLayout.addWidget(self.lineEdit_d_stop, 3, 1, 1, 1)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout.addLayout(self.verticalLayout, 3, 5, 1, 1)

        self.lineEdit_v_stop = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_v_stop.setObjectName(u"lineEdit_v_stop")

        self.gridLayout.addWidget(self.lineEdit_v_stop, 5, 1, 1, 1)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_9 = QLabel(self.horizontalLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 2, 1, 1)

        self.label_7 = QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.applyButton = QPushButton(self.horizontalLayoutWidget)
        self.applyButton.setObjectName(u"applyButton")

        self.verticalLayout_2.addWidget(self.applyButton)

        self.resetButton = QPushButton(self.horizontalLayoutWidget)
        self.resetButton.setObjectName(u"resetButton")

        self.verticalLayout_2.addWidget(self.resetButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"T_X Setting", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"m/s", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"m", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"m", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"m/s", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Velosity v", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"d_stop", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"v_stop", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"m/s", None))
        self.label.setText(QCoreApplication.translate("Form", u"Distance d ", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"d_start", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"m", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"v_start", None))
        self.applyButton.setText(QCoreApplication.translate("Form", u"Apply", None))
        self.resetButton.setText(QCoreApplication.translate("Form", u"Reset", None))
    # retranslateUi

