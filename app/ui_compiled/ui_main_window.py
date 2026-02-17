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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

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
        MainWindow.resize(1270, 720)
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
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-1, -1, 361, 661))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.tabWidget = QTabWidget(self.frame_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(6, 10, 351, 651))
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.scrollArea = QScrollArea(self.tab_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 320, 331, 301))
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 329, 299))
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
        self.TargetList.setGeometry(QRect(10, 10, 333, 301))
        self.TargetList.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.TargetList.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 331, 299))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.TargetList.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.chirp_param = QFrame(self.tab)
        self.chirp_param.setObjectName(u"chirp_param")
        self.chirp_param.setGeometry(QRect(19, 19, 311, 381))
        self.chirp_param.setFrameShape(QFrame.NoFrame)
        self.horizontalLayoutWidget = QWidget(self.chirp_param)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 339, 291, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.applyAndSaveButton = QPushButton(self.horizontalLayoutWidget)
        self.applyAndSaveButton.setObjectName(u"applyAndSaveButton")

        self.horizontalLayout_2.addWidget(self.applyAndSaveButton)

        self.showButton = QPushButton(self.horizontalLayoutWidget)
        self.showButton.setObjectName(u"showButton")

        self.horizontalLayout_2.addWidget(self.showButton)

        self.formLayoutWidget = QWidget(self.chirp_param)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 291, 324))
        self.gridLayout = QGridLayout(self.formLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.formLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)

        self.lineEdit_f_BW = QLineEdit(self.formLayoutWidget)
        self.lineEdit_f_BW.setObjectName(u"lineEdit_f_BW")

        self.gridLayout.addWidget(self.lineEdit_f_BW, 1, 1, 1, 1)

        self.lineEdit_f_start = QLineEdit(self.formLayoutWidget)
        self.lineEdit_f_start.setObjectName(u"lineEdit_f_start")
        self.lineEdit_f_start.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEdit_f_start, 0, 1, 1, 1)

        self.label_18 = QLabel(self.formLayoutWidget)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 5, 2, 1, 1)

        self.lineEdit_t_pri = QLineEdit(self.formLayoutWidget)
        self.lineEdit_t_pri.setObjectName(u"lineEdit_t_pri")

        self.gridLayout.addWidget(self.lineEdit_t_pri, 4, 1, 1, 1)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)

        self.label_12 = QLabel(self.formLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)

        self.lineEdit_t_pre = QLineEdit(self.formLayoutWidget)
        self.lineEdit_t_pre.setObjectName(u"lineEdit_t_pre")

        self.gridLayout.addWidget(self.lineEdit_t_pre, 5, 1, 1, 1)

        self.label_20 = QLabel(self.formLayoutWidget)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 7, 2, 1, 1)

        self.label_17 = QLabel(self.formLayoutWidget)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 4, 2, 1, 1)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 9, 0, 1, 1)

        self.lineEdit_n_sample = QLineEdit(self.formLayoutWidget)
        self.lineEdit_n_sample.setObjectName(u"lineEdit_n_sample")

        self.gridLayout.addWidget(self.lineEdit_n_sample, 8, 1, 1, 1)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_19 = QLabel(self.formLayoutWidget)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 6, 2, 1, 1)

        self.label_13 = QLabel(self.formLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 0, 2, 1, 1)

        self.label_9 = QLabel(self.formLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)

        self.label_15 = QLabel(self.formLayoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 2, 2, 1, 1)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.lineEdit_t_fly = QLineEdit(self.formLayoutWidget)
        self.lineEdit_t_fly.setObjectName(u"lineEdit_t_fly")

        self.gridLayout.addWidget(self.lineEdit_t_fly, 6, 1, 1, 1)

        self.lineEdit_f_s = QLineEdit(self.formLayoutWidget)
        self.lineEdit_f_s.setObjectName(u"lineEdit_f_s")

        self.gridLayout.addWidget(self.lineEdit_f_s, 2, 1, 1, 1)

        self.lineEdit_n_ramps = QLineEdit(self.formLayoutWidget)
        self.lineEdit_n_ramps.setObjectName(u"lineEdit_n_ramps")

        self.gridLayout.addWidget(self.lineEdit_n_ramps, 9, 1, 1, 1)

        self.label_10 = QLabel(self.formLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 6, 0, 1, 1)

        self.label_16 = QLabel(self.formLayoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 3, 2, 1, 1)

        self.lineEdit_t_c = QLineEdit(self.formLayoutWidget)
        self.lineEdit_t_c.setObjectName(u"lineEdit_t_c")

        self.gridLayout.addWidget(self.lineEdit_t_c, 3, 1, 1, 1)

        self.lineEdit_t_wait = QLineEdit(self.formLayoutWidget)
        self.lineEdit_t_wait.setObjectName(u"lineEdit_t_wait")

        self.gridLayout.addWidget(self.lineEdit_t_wait, 7, 1, 1, 1)

        self.label_14 = QLabel(self.formLayoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.plot_frame = QFrame(self.frame)
        self.plot_frame.setObjectName(u"plot_frame")
        self.plot_frame.setGeometry(QRect(359, 9, 891, 651))
        self.plot_frame.setFrameShape(QFrame.StyledPanel)
        self.plot_frame.setFrameShadow(QFrame.Raised)
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
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1270, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuRun = QMenu(self.menubar)
        self.menuRun.setObjectName(u"menuRun")
        self.menuPause = QMenu(self.menubar)
        self.menuPause.setObjectName(u"menuPause")
        self.menuStop = QMenu(self.menubar)
        self.menuStop.setObjectName(u"menuStop")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuPause.menuAction())
        self.menubar.addAction(self.menuStop.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionReset)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionReset.setText(QCoreApplication.translate("MainWindow", u"Reset Settings", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Target - List", None))
        self.applyAndSaveButton.setText(QCoreApplication.translate("MainWindow", u"Apply && Save", None))
        self.showButton.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"t_pre", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u00b5s", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"n_sample", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"t_pri", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u00b5s", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u00b5s", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"t_c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"n_ramps", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"f_s", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"f_start", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u00b5s", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"MHz", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"t_wait", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"MHz", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"f_BW", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"t_fly", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u00b5s", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"MHz", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"FMCW - Settings", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuRun.setTitle(QCoreApplication.translate("MainWindow", u"Run", None))
        self.menuPause.setTitle(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.menuStop.setTitle(QCoreApplication.translate("MainWindow", u"Stop", None))
    # retranslateUi

