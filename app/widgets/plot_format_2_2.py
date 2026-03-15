#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 00:18:28 2026

@author: benny
"""

from PySide6.QtWidgets import QWidget
from app.ui_compiled.ui_plot_format_2_2 import Ui_Form

class PlotFormat_2_2(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)