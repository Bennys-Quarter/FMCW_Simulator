#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:04:42 2026

@author: benny
"""

from PySide6.QtWidgets import QWidget
from app.ui_compiled.ui_plot_format_single import Ui_Form

class PlotFormatSingle(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)