# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plot_fullscreen_popupui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_PlotFullScreenPopup(object):
    def setupUi(self, PlotFullScreenPopup):
        if not PlotFullScreenPopup.objectName():
            PlotFullScreenPopup.setObjectName(u"PlotFullScreenPopup")
        PlotFullScreenPopup.resize(939, 542)
        self.verticalLayout = QVBoxLayout(PlotFullScreenPopup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.closeButton = QPushButton(PlotFullScreenPopup)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setMinimumSize(QSize(20, 20))
        self.closeButton.setMaximumSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.closeButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.plotFrame = QFrame(PlotFullScreenPopup)
        self.plotFrame.setObjectName(u"plotFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.plotFrame.sizePolicy().hasHeightForWidth())
        self.plotFrame.setSizePolicy(sizePolicy1)
        self.plotFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.plotFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.plotFrame)


        self.retranslateUi(PlotFullScreenPopup)

        QMetaObject.connectSlotsByName(PlotFullScreenPopup)
    # setupUi

    def retranslateUi(self, PlotFullScreenPopup):
        PlotFullScreenPopup.setWindowTitle(QCoreApplication.translate("PlotFullScreenPopup", u"Form", None))
        self.closeButton.setText(QCoreApplication.translate("PlotFullScreenPopup", u"x", None))
    # retranslateUi

