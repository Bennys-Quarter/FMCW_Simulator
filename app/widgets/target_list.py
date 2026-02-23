#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 17:17:22 2026

@author: benny
"""
from PySide6.QtCore import Qt, QRect, QEvent, QObject
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QScrollArea, QVBoxLayout, QWidget
from app.utils.drag_and_drop import DraggableMixin
from app.widgets.target_list_entry import TargetListEntry
from app.core.app_state import AppState

class TargetList(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.state = AppState()
        
        self.setAcceptDrops(True)
        self._original_stylesheet = self.styleSheet()
        self._target_list=[
            "Box_Pedestrian",
            "Box_Drone",
            "Box_Truck"
            ]
        
        
    def dragEnterEvent(self, event):
        self.setStyleSheet("background-color: rgba(100, 100, 255, 50);")
        event.accept() 


    def dragLeaveEvent(self, event):
        self.setStyleSheet(self._original_stylesheet)
        event.accept()


    def dropEvent(self, event):
        if event.mimeData().hasText():
            name = event.mimeData().text()
            if any(name in item for item in self._target_list):
                char = name.split("Box_", 1)[1][0]
                idx = self.state.generate_target_id()
                en_index = char + "_" + str(idx)
                new_entry = TargetListEntry(l_target=en_index,
                                            idx=idx)
                self.widget().layout().insertWidget(0, new_entry)
                self.on_new_target(new_entry.idx, new_entry.v, new_entry.d)
                
        self.setStyleSheet(self._original_stylesheet)
        event.accept()   


    def on_new_target(self, idx, v, d):
        new_target = {
                "- id": idx,
                "range_m": d, 
                "velocity_mps": v
                }
        targets = self.state.radar.target_params
        targets["targets"].append(new_target)
        self.state.radar.target_params = targets
        self.state.radar.set_target_parameters(targets)
