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
    def __init__(self, l_target="T_X",idx=-1, v=0, d=0, rcs=0, parent=None):
        super().__init__(parent)
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        
        self.state = AppState()
        
        self.idx = idx
        self.v = v
        self.d = d
        self.rcs = rcs # in dBsm
        
        self.exit_btn = self.findChild(QToolButton, "ExitButton")
        self.option_btn = self.findChild(QToolButton, "OptionsButton")
        self.l_target = self.findChild(QLabel, "l_target")
        self.l_distance = self.findChild(QLabel, "l_distance")
        self.l_velocity = self.findChild(QLabel, "l_velocity")
        
        self.l_target.setText(l_target)
        self.update_text()
        
        self.exit_btn.clicked.connect(self.on_exit_clicked)
        self.option_btn.clicked.connect(self.on_option_clicked)
        
        
    def update_text(self):
        self.l_distance.setText(str(self.d))
        self.l_velocity.setText(str(self.v))
        
    
    def on_exit_clicked(self):
        params = self.state.radar.target_params
        targets = params["targets"]
        index_to_remove = next((i for i, d in enumerate(targets) if d.get('- id') == self.idx), None)
        if index_to_remove is not None:
            targets.pop(index_to_remove)
        
        self.state.radar.clear_target_parameters()
        #self.state.radar.set_target_parameters(params)
        self.state.remove_target_id(self.idx)
        self.deleteLater()
        
        
    def on_option_clicked(self):
        self.popup = PopupTargetSetting(ref_obj=self, idx=self.idx, name=self.l_target.text())
        self.popup.show()
    
        
        