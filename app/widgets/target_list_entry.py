#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 20:02:24 2026

@author: benny
"""

from PySide6.QtWidgets import QGroupBox, QToolButton, QLabel
from app.ui_compiled.ui_target_List_Entry import Ui_Frame
from app.utils.drag_and_drop import DraggableMixin
from app.widgets.popup_target_setting import PopupTargetSetting

from app.core.app_state import AppState

class TargetListEntry(DraggableMixin, QGroupBox):
    def __init__(self, l_target="T_X",idx=-1, v=0, d=0, parent=None):
        super().__init__(parent)
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        
        self.state = AppState()
        
        self.idx = idx
        self.v = v
        self.d = d
        
        self.exit_btn = self.findChild(QToolButton, "ExitButton")
        self.option_btn = self.findChild(QToolButton, "OptionsButton")
        self.l_target = self.findChild(QLabel, "l_target")
        self.l_distance = self.findChild(QLabel, "l_distance")
        self.l_velocity = self.findChild(QLabel, "l_velocity")
        
        self.l_target.setText(l_target)
        self.l_distance.setText(str(self.d))
        self.l_velocity.setText(str(self.v))
        
        self.exit_btn.clicked.connect(self.on_exit_clicked)
        self.option_btn.clicked.connect(self.on_option_clicked)
    
    def on_exit_clicked(self):
        self.state.remove_target_id(self.idx)
        self.deleteLater()
        
    def on_option_clicked(self):
        self.popup = PopupTargetSetting(name=self.l_target.text())
        self.popup.show()
        
        