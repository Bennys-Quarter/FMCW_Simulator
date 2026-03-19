# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

from app.widgets.box_drone import BoxDrone
from app.widgets.box_pedestrian import BoxPedestrian
from app.widgets.box_truck import BoxTruck
from app.widgets.target_list import TargetList
from app.resources import icons_rc
from app.resources import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1269, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAnimated(True)
        self.actionReset = QAction(MainWindow)
        self.actionReset.setObjectName(u"actionReset")
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.actionRun = QAction(MainWindow)
        self.actionRun.setObjectName(u"actionRun")
        self.actionStop = QAction(MainWindow)
        self.actionStop.setObjectName(u"actionStop")
        self.actionFullscreen = QAction(MainWindow)
        self.actionFullscreen.setObjectName(u"actionFullscreen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setGeometry(QRect(9, -1, 1251, 681))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy2)
        self.mainFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_7 = QHBoxLayout(self.mainFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.mainSettingsFrame = QFrame(self.mainFrame)
        self.mainSettingsFrame.setObjectName(u"mainSettingsFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainSettingsFrame.sizePolicy().hasHeightForWidth())
        self.mainSettingsFrame.setSizePolicy(sizePolicy3)
        self.mainSettingsFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.mainSettingsFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tabWidget = QTabWidget(self.mainSettingsFrame)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(350, 655))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 10, 331, 601))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget_3 = QWidget(self.frame_4)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 10, 310, 505))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox = QGroupBox(self.verticalLayoutWidget_3)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy4)
        self.groupBox.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setEnabled(True)
        self.radioButton.setChecked(True)

        self.horizontalLayout_9.addWidget(self.radioButton)


        self.verticalLayout_7.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy4)
        self.groupBox_2.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setBold(False)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setFlat(False)
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.radioButton_2 = QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy5)
        self.radioButton_2.setMinimumSize(QSize(0, 15))
        self.radioButton_2.setChecked(True)

        self.horizontalLayout_8.addWidget(self.radioButton_2)

        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setMinimumSize(QSize(0, 15))

        self.horizontalLayout_8.addWidget(self.radioButton_4)

        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setMinimumSize(QSize(0, 15))

        self.horizontalLayout_8.addWidget(self.radioButton_3)


        self.verticalLayout_7.addWidget(self.groupBox_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_7)

        self.line_3 = QFrame(self.verticalLayoutWidget_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.label_14 = QLabel(self.verticalLayoutWidget_3)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 1, 2, 1, 1)

        self.label_20 = QLabel(self.verticalLayoutWidget_3)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 7, 2, 1, 1)

        self.label_10 = QLabel(self.verticalLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 6, 0, 1, 1)

        self.label_11 = QLabel(self.verticalLayoutWidget_3)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)

        self.label_12 = QLabel(self.verticalLayoutWidget_3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)

        self.label_5 = QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_13 = QLabel(self.verticalLayoutWidget_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 0, 2, 1, 1)

        self.label_17 = QLabel(self.verticalLayoutWidget_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 4, 2, 1, 1)

        self.lineEdit_t_pre = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_t_pre.setObjectName(u"lineEdit_t_pre")

        self.gridLayout.addWidget(self.lineEdit_t_pre, 5, 1, 1, 1)

        self.label_19 = QLabel(self.verticalLayoutWidget_3)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 6, 2, 1, 1)

        self.lineEdit_t_wait = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_t_wait.setObjectName(u"lineEdit_t_wait")

        self.gridLayout.addWidget(self.lineEdit_t_wait, 7, 1, 1, 1)

        self.label_7 = QLabel(self.verticalLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)

        self.lineEdit_n_sample = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_n_sample.setObjectName(u"lineEdit_n_sample")

        self.gridLayout.addWidget(self.lineEdit_n_sample, 8, 1, 1, 1)

        self.lineEdit_f_s = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_f_s.setObjectName(u"lineEdit_f_s")

        self.gridLayout.addWidget(self.lineEdit_f_s, 2, 1, 1, 1)

        self.label = QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_8 = QLabel(self.verticalLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.lineEdit_f_BW = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_f_BW.setObjectName(u"lineEdit_f_BW")

        self.gridLayout.addWidget(self.lineEdit_f_BW, 1, 1, 1, 1)

        self.lineEdit_f_start = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_f_start.setObjectName(u"lineEdit_f_start")
        self.lineEdit_f_start.setMinimumSize(QSize(100, 0))
        self.lineEdit_f_start.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEdit_f_start, 0, 1, 1, 1)

        self.lineEdit_t_c = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_t_c.setObjectName(u"lineEdit_t_c")

        self.gridLayout.addWidget(self.lineEdit_t_c, 3, 1, 1, 1)

        self.lineEdit_t_fly = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_t_fly.setObjectName(u"lineEdit_t_fly")

        self.gridLayout.addWidget(self.lineEdit_t_fly, 6, 1, 1, 1)

        self.lineEdit_t_pri = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_t_pri.setObjectName(u"lineEdit_t_pri")

        self.gridLayout.addWidget(self.lineEdit_t_pri, 4, 1, 1, 1)

        self.label_15 = QLabel(self.verticalLayoutWidget_3)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 2, 2, 1, 1)

        self.lineEdit_n_ramps = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_n_ramps.setObjectName(u"lineEdit_n_ramps")

        self.gridLayout.addWidget(self.lineEdit_n_ramps, 9, 1, 1, 1)

        self.label_9 = QLabel(self.verticalLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)

        self.label_18 = QLabel(self.verticalLayoutWidget_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 5, 2, 1, 1)

        self.label_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 9, 0, 1, 1)

        self.label_6 = QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_16 = QLabel(self.verticalLayoutWidget_3)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 3, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout)

        self.line = QFrame(self.verticalLayoutWidget_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.applyAndSaveButton = QPushButton(self.verticalLayoutWidget_3)
        self.applyAndSaveButton.setObjectName(u"applyAndSaveButton")

        self.horizontalLayout_2.addWidget(self.applyAndSaveButton)

        self.showButton = QPushButton(self.verticalLayoutWidget_3)
        self.showButton.setObjectName(u"showButton")

        self.horizontalLayout_2.addWidget(self.showButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.frame_6 = QFrame(self.tab_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, 10, 331, 601))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.scrollArea = QScrollArea(self.tab_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 320, 331, 291))
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 329, 289))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Box_Pedestrian = BoxPedestrian(self.scrollAreaWidgetContents)
        self.Box_Pedestrian.setObjectName(u"Box_Pedestrian")

        self.verticalLayout_4.addWidget(self.Box_Pedestrian)

        self.Box_Drone = BoxDrone(self.scrollAreaWidgetContents)
        self.Box_Drone.setObjectName(u"Box_Drone")

        self.verticalLayout_4.addWidget(self.Box_Drone)

        self.Box_Truck = BoxTruck(self.scrollAreaWidgetContents)
        self.Box_Truck.setObjectName(u"Box_Truck")

        self.verticalLayout_4.addWidget(self.Box_Truck)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.TargetList = TargetList(self.tab_2)
        self.TargetList.setObjectName(u"TargetList")
        self.TargetList.setGeometry(QRect(10, 10, 331, 301))
        self.TargetList.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.TargetList.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 329, 299))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.TargetList.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.frame_5 = QFrame(self.tab_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 10, 331, 601))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget_2 = QWidget(self.frame_5)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 311, 581))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBox = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox.setObjectName(u"checkBox")
        font1 = QFont()
        font1.setBold(True)
        self.checkBox.setFont(font1)

        self.horizontalLayout_6.addWidget(self.checkBox)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.line_4 = QFrame(self.verticalLayoutWidget_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_4)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.setTargetDetection = QComboBox(self.verticalLayoutWidget_2)
        self.setTargetDetection.addItem("")
        self.setTargetDetection.addItem("")
        self.setTargetDetection.setObjectName(u"setTargetDetection")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.setTargetDetection)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.checkBox_2 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font1)

        self.verticalLayout_3.addWidget(self.checkBox_2)

        self.line_8 = QFrame(self.verticalLayoutWidget_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_8)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_22 = QLabel(self.verticalLayoutWidget_2)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_22)

        self.setTargetDetection_2 = QComboBox(self.verticalLayoutWidget_2)
        self.setTargetDetection_2.addItem("")
        self.setTargetDetection_2.addItem("")
        self.setTargetDetection_2.setObjectName(u"setTargetDetection_2")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.setTargetDetection_2)


        self.verticalLayout_3.addLayout(self.formLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.applyButton = QPushButton(self.verticalLayoutWidget_2)
        self.applyButton.setObjectName(u"applyButton")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.applyButton.sizePolicy().hasHeightForWidth())
        self.applyButton.setSizePolicy(sizePolicy6)
        self.applyButton.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.applyButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.frame_3 = QFrame(self.tab_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 10, 331, 601))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget_4 = QWidget(self.frame_3)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 9, 311, 581))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.verticalLayoutWidget_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_23)

        self.line_5 = QFrame(self.verticalLayoutWidget_4)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_25 = QLabel(self.verticalLayoutWidget_4)
        self.label_25.setObjectName(u"label_25")
        sizePolicy5.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy5)

        self.horizontalLayout_4.addWidget(self.label_25)

        self.plotLayoutSelector = QComboBox(self.verticalLayoutWidget_4)
        self.plotLayoutSelector.addItem("")
        self.plotLayoutSelector.addItem("")
        self.plotLayoutSelector.setObjectName(u"plotLayoutSelector")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.plotLayoutSelector.sizePolicy().hasHeightForWidth())
        self.plotLayoutSelector.setSizePolicy(sizePolicy7)

        self.horizontalLayout_4.addWidget(self.plotLayoutSelector)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.label_24 = QLabel(self.verticalLayoutWidget_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_24)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_3 = QGroupBox(self.verticalLayoutWidget_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radioButton_3D = QRadioButton(self.groupBox_3)
        self.radioButton_3D.setObjectName(u"radioButton_3D")

        self.gridLayout_2.addWidget(self.radioButton_3D, 0, 2, 1, 1)

        self.radioButton_2D = QRadioButton(self.groupBox_3)
        self.radioButton_2D.setObjectName(u"radioButton_2D")
        self.radioButton_2D.setChecked(True)

        self.gridLayout_2.addWidget(self.radioButton_2D, 0, 1, 1, 1)

        self.label_26 = QLabel(self.groupBox_3)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_2.addWidget(self.label_26, 0, 0, 1, 1)


        self.horizontalLayout_10.addLayout(self.gridLayout_2)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_5 = QGroupBox(self.verticalLayoutWidget_4)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.radioButton_white = QRadioButton(self.groupBox_5)
        self.radioButton_white.setObjectName(u"radioButton_white")
        self.radioButton_white.setChecked(False)

        self.gridLayout_4.addWidget(self.radioButton_white, 0, 1, 1, 1)

        self.label_30 = QLabel(self.groupBox_5)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_4.addWidget(self.label_30, 0, 0, 1, 1)

        self.radioButton_black = QRadioButton(self.groupBox_5)
        self.radioButton_black.setObjectName(u"radioButton_black")
        self.radioButton_black.setChecked(True)

        self.gridLayout_4.addWidget(self.radioButton_black, 0, 2, 1, 1)


        self.horizontalLayout_11.addLayout(self.gridLayout_4)


        self.verticalLayout_2.addWidget(self.groupBox_5)

        self.groupBox_4 = QGroupBox(self.verticalLayoutWidget_4)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.radioButton_physical = QRadioButton(self.groupBox_4)
        self.radioButton_physical.setObjectName(u"radioButton_physical")
        self.radioButton_physical.setChecked(True)

        self.gridLayout_3.addWidget(self.radioButton_physical, 0, 2, 1, 1)

        self.radioButton_bins = QRadioButton(self.groupBox_4)
        self.radioButton_bins.setObjectName(u"radioButton_bins")
        self.radioButton_bins.setChecked(False)

        self.gridLayout_3.addWidget(self.radioButton_bins, 0, 1, 1, 1)

        self.label_29 = QLabel(self.groupBox_4)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_3.addWidget(self.label_29, 0, 0, 1, 1)


        self.horizontalLayout_12.addLayout(self.gridLayout_3)


        self.verticalLayout_2.addWidget(self.groupBox_4)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)

        self.line_7 = QFrame(self.verticalLayoutWidget_4)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_7)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.spinMinClimBox = QSpinBox(self.verticalLayoutWidget_4)
        self.spinMinClimBox.setObjectName(u"spinMinClimBox")
        self.spinMinClimBox.setMinimum(-160)
        self.spinMinClimBox.setMaximum(20)
        self.spinMinClimBox.setValue(-120)

        self.gridLayout_5.addWidget(self.spinMinClimBox, 0, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_6, 0, 1, 1, 1)

        self.spinMaxClimBox = QSpinBox(self.verticalLayoutWidget_4)
        self.spinMaxClimBox.setObjectName(u"spinMaxClimBox")
        self.spinMaxClimBox.setMinimum(-160)
        self.spinMaxClimBox.setMaximum(20)
        self.spinMaxClimBox.setValue(-35)

        self.gridLayout_5.addWidget(self.spinMaxClimBox, 0, 4, 1, 1)

        self.label_31 = QLabel(self.verticalLayoutWidget_4)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_5.addWidget(self.label_31, 0, 3, 1, 1)

        self.label_32 = QLabel(self.verticalLayoutWidget_4)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_5.addWidget(self.label_32, 0, 5, 1, 1)

        self.label_28 = QLabel(self.verticalLayoutWidget_4)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_5.addWidget(self.label_28, 0, 0, 1, 1)

        self.label_33 = QLabel(self.verticalLayoutWidget_4)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_5.addWidget(self.label_33, 0, 6, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_5)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.runPlotButton = QPushButton(self.verticalLayoutWidget_4)
        self.runPlotButton.setObjectName(u"runPlotButton")

        self.horizontalLayout_3.addWidget(self.runPlotButton)

        self.stopPlotButton = QPushButton(self.verticalLayoutWidget_4)
        self.stopPlotButton.setObjectName(u"stopPlotButton")

        self.horizontalLayout_3.addWidget(self.stopPlotButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab_4, "")

        self.horizontalLayout_5.addWidget(self.tabWidget)


        self.horizontalLayout_7.addWidget(self.mainSettingsFrame)

        self.plotFrame = QFrame(self.mainFrame)
        self.plotFrame.setObjectName(u"plotFrame")
        sizePolicy2.setHeightForWidth(self.plotFrame.sizePolicy().hasHeightForWidth())
        self.plotFrame.setSizePolicy(sizePolicy2)
        self.plotFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.plotFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_7.addWidget(self.plotFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1269, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuRun = QMenu(self.menubar)
        self.menuRun.setObjectName(u"menuRun")
        self.menuPlots = QMenu(self.menuRun)
        self.menuPlots.setObjectName(u"menuPlots")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionReset)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuRun.addAction(self.menuPlots.menuAction())
        self.menuPlots.addAction(self.actionFullscreen)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(4)
        self.plotLayoutSelector.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionReset.setText(QCoreApplication.translate("MainWindow", u"Reset Settings", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.actionRun.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.actionStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.actionFullscreen.setText(QCoreApplication.translate("MainWindow", u"Fullscreen", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Source", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"FMCW", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Waveform", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Up-Chirp", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Down-Chirp", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Triangle-Chirp", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"MHz", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u00b5s", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"t_fly", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"t_pre", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"t_pri", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"f_BW", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"MHz", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u00b5s", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u00b5s", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"n_sample", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"f_start", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"t_c", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"MHz", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"t_wait", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u00b5s", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"n_ramps", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"f_s", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u00b5s", None))
        self.applyAndSaveButton.setText(QCoreApplication.translate("MainWindow", u"Apply && Save", None))
        self.showButton.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Signal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"MIMO", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Targets", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Target Detection", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Algorithm", None))
        self.setTargetDetection.setItemText(0, QCoreApplication.translate("MainWindow", u"Single Threshold", None))
        self.setTargetDetection.setItemText(1, QCoreApplication.translate("MainWindow", u"CA-CFAR", None))

        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"DoA", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Algorithm", None))
        self.setTargetDetection_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Angle FFT", None))
        self.setTargetDetection_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Delay-Sum-Beamformer", None))

        self.applyButton.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Processing", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Selection", None))
        self.plotLayoutSelector.setItemText(0, QCoreApplication.translate("MainWindow", u"RD-Map", None))
        self.plotLayoutSelector.setItemText(1, QCoreApplication.translate("MainWindow", u"Signals", None))

        self.plotLayoutSelector.setCurrentText(QCoreApplication.translate("MainWindow", u"RD-Map", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"RD Map", None))
        self.radioButton_3D.setText(QCoreApplication.translate("MainWindow", u"3D", None))
        self.radioButton_2D.setText(QCoreApplication.translate("MainWindow", u"2D", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Dimension", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Visuals", None))
        self.radioButton_white.setText(QCoreApplication.translate("MainWindow", u"white", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Background", None))
        self.radioButton_black.setText(QCoreApplication.translate("MainWindow", u"black", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Axis", None))
        self.radioButton_physical.setText(QCoreApplication.translate("MainWindow", u"physical", None))
        self.radioButton_bins.setText(QCoreApplication.translate("MainWindow", u"bins", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Ticks Lables", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Clim", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"dBfs", None))
        self.runPlotButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.stopPlotButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Window", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuRun.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.menuPlots.setTitle(QCoreApplication.translate("MainWindow", u"Plots", None))
    # retranslateUi

