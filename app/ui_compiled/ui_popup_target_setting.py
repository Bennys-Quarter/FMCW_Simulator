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
        Form.resize(305, 152)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 281, 131))
        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 30, 261, 91))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_6 = QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)

        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.lineEdit_d = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_d.setObjectName(u"lineEdit_d")

        self.gridLayout.addWidget(self.lineEdit_d, 0, 1, 1, 1)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_v = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_v.setObjectName(u"lineEdit_v")

        self.gridLayout.addWidget(self.lineEdit_v, 1, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout.addLayout(self.verticalLayout, 2, 5, 1, 1)


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
        self.label.setText(QCoreApplication.translate("Form", u"Distance d ", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"m/s", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"m", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Velosity v", None))
        self.applyButton.setText(QCoreApplication.translate("Form", u"Apply", None))
        self.resetButton.setText(QCoreApplication.translate("Form", u"Reset", None))
    # retranslateUi

