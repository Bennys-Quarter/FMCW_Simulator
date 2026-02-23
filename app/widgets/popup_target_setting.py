#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 16:22:03 2026

@author: benny
"""

from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit
from app.ui_compiled.ui_popup_target_setting import Ui_Form

from app.core.app_state import AppState

class PopupTargetSetting(QWidget):
    def __init__(self, parent=None, ref_obj=None, idx=-1, name=""):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.state = AppState()
        
        self.ref_obj = ref_obj
        
        self.setWindowTitle(name)
        self.idx = idx
        
        self.l_d = self.findChild(QLineEdit, "lineEdit_d")
        self.l_v = self.findChild(QLineEdit, "lineEdit_v")
        self.l_d_start = self.findChild(QLineEdit, "lineEdit_d_start")
        self.l_v_start = self.findChild(QLineEdit, "lineEdit_v_start")
        self.l_v_stop = self.findChild(QLineEdit, "lineEdit_v_stop")
        self.l_v_stop = self.findChild(QLineEdit, "lineEdit_v_stop")
        self.apply_btn = self.findChild(QPushButton, "applyButton")
        self.reset_btn = self.findChild(QPushButton, "resetButton")
        
        self.l_d.setText(str(ref_obj.d))
        self.l_v.setText(str(ref_obj.v))
        
        self.apply_btn.clicked.connect(self.on_apply_clicked)
        self.reset_btn.clicked.connect(self.on_reset_clicked)
        
        
    def on_apply_clicked(self):
        d = int(self.l_d.text())
        v = int(self.l_v.text())
        
        params = self.state.radar.target_params
        
        for t in params["targets"]:
            if int(t["- id"]) == self.idx:
                t["velocity_mps"] = v
                t["range_m"] = d
                self.ref_obj.d = d
                self.ref_obj.v = v
                self.ref_obj.update_text()
                break
        
        
        self.state.radar.target_params = params
        self.state.radar.clear_target_parameters()
        self.state.radar.set_target_parameters(params)
        self.deleteLater()
    
    
    def on_reset_clicked(self):
        d = 0
        v = 0
        
        self.l_d.setText(str(d))
        self.l_v.setText(str(v))
        
        params = self.state.radar.target_params
        
        for t in params["targets"]:
            if int(t["- id"]) == self.idx:
                t["velocity_mps"] = v
                t["range_m"] = d
                self.ref_obj.d = d
                self.ref_obj.v = v
                self.ref_obj.update_text()
                break
        
        self.state.radar.target_params = params
        self.state.radar.clear_target_parameters()
        self.state.radar.set_target_parameters(params)
        
        
        
        