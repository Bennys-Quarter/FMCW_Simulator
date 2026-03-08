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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

from app.widgets.box_drone import BoxDrone
from app.widgets.box_pedestrian import BoxPedestrian
from app.widgets.box_truck import BoxTruck
from app.widgets.plot_widget import PlotWidget
from app.widgets.target_list import TargetList
from app.resources import icons_rc
from app.resources import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1271, 720)
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 1251, 661))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-1, -1, 361, 661))
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.tabWidget = QTabWidget(self.frame_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(6, 10, 351, 651))
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
        self.sigSetLayout = QFormLayout()
        self.sigSetLayout.setObjectName(u"sigSetLayout")
        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.sigSetLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.setTargetDetection = QComboBox(self.verticalLayoutWidget_2)
        self.setTargetDetection.addItem("")
        self.setTargetDetection.addItem("")
        self.setTargetDetection.setObjectName(u"setTargetDetection")

        self.sigSetLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.setTargetDetection)


        self.verticalLayout_3.addLayout(self.sigSetLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.applyButton = QPushButton(self.verticalLayoutWidget_2)
        self.applyButton.setObjectName(u"applyButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.applyButton.sizePolicy().hasHeightForWidth())
        self.applyButton.setSizePolicy(sizePolicy2)
        self.applyButton.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.applyButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 10, 331, 601))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget_3 = QWidget(self.frame_4)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 10, 311, 581))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.line = QFrame(self.verticalLayoutWidget_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
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

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 3, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

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
        self.plot_frame = QFrame(self.frame)
        self.plot_frame.setObjectName(u"plot_frame")
        self.plot_frame.setGeometry(QRect(359, 9, 891, 651))
        self.plot_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.plot_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayoutWidget = QWidget(self.plot_frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 861, 631))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.plotWidget = PlotWidget(self.verticalLayoutWidget)
        self.plotWidget.setObjectName(u"plotWidget")

        self.verticalLayout_2.addWidget(self.plotWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1271, 22))
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
        self.menuPlots.addAction(self.actionRun)
        self.menuPlots.addAction(self.actionStop)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionReset.setText(QCoreApplication.translate("MainWindow", u"Reset Settings", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.actionRun.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.actionStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Target - List", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Target Detection", None))
        self.setTargetDetection.setItemText(0, QCoreApplication.translate("MainWindow", u"Single Threshold", None))
        self.setTargetDetection.setItemText(1, QCoreApplication.translate("MainWindow", u"CA-CFAR", None))

        self.applyButton.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Sig. Proc.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Up Chrip Settings", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"FMCW - Settings", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuRun.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.menuPlots.setTitle(QCoreApplication.translate("MainWindow", u"Plots", None))
    # retranslateUi

