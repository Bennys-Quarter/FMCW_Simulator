#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 00:56:03 2026

@author: benny
"""

from PySide6.QtWidgets import QGroupBox
from app.ui_compiled.ui_box_pedestrian import Ui_BoxPedestrian

class BoxPedestrian(QGroupBox):  # <-- name Designer will promote to
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_BoxPedestrian()
        self.ui.setupUi(self)