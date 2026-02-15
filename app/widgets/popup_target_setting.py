#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 16:22:03 2026

@author: benny
"""

from PySide6.QtWidgets import QWidget
from app.ui_compiled.ui_popup_target_setting import Ui_Form


class PopupTargetSetting(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)