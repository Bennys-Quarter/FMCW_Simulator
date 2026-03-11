#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 22:18:12 2026

@author: benny
"""

from PySide6.QtWidgets import QWidget, QPushButton, QFrame, QVBoxLayout
from app.ui_compiled.ui_plot_fullscreen_popupui import Ui_PlotFullScreenPopup

class PlotFullscreenPopup(QWidget):
    def __init__(self, origin = None, layout = None):
        super().__init__()
        self.ui = Ui_PlotFullScreenPopup()
        self.ui.setupUi(self)
        
        self.setWindowTitle("Fullscreen Popup")
        self.showFullScreen()
        
        self.origin = origin
        self.plot_layout = layout

        frame_layout = self.findChild(QFrame, "plotFrame")
        self.layout().removeWidget(frame_layout)
        self.layout().addWidget(self.plot_layout)
        
        
        self.btn_close = self.findChild(QPushButton, "closeButton")
        self.btn_close.clicked.connect(self.on_close_clicked)


    def on_close_clicked(self):
        # Passing back the plot frame
        self.origin.layout().addWidget(self.plot_layout)
        self.deleteLater()
        