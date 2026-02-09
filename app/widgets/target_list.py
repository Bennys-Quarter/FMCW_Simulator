#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 17:17:22 2026

@author: benny
"""
from PySide6.QtCore import Qt, QRect, QEvent, QObject
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QScrollArea
from app.utils.drag_and_drop import DraggableMixin

from app.widgets.box_drone import BoxDrone
from app.widgets.box_pedestrian import BoxPedestrian
from app.widgets.box_truck import BoxTruck


class TargetList(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._hovered = False
        # self._content_candidate_list = [
        #     BoxDrone, 
        #     BoxPedestrian, 
        #     BoxTruck
        #     ]
        
        self.viewport().setAttribute(Qt.WA_Hover, True)
        self.viewport().setMouseTracking(True)
        
        self.setAcceptDrops(True)
    
        
    def dragEnterEvent(self, event):
        print("hi")
    
    def onDragHover(self):
        self.check_viewport()
        self.setStyleSheet("background: rgba(0, 150, 255, 60);")    
    
    
    def check_viewport(self):
        if DraggableMixin._global_drag_active == True:
            print("hi")


    def reset_hover(self):
        if self._hovered:
            self._hovered = False
            self.setStyleSheet("")
           
            
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("Mouse pressed inside viewport!")
        super().mousePressEvent(event)


    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("Mouse released!")
        super().mouseReleaseEvent(event)
    
    
    def mouseMoveEvent(self, event):
        pos = event.position()
        print(pos)
        if event.buttons() & Qt.LeftButton:  # Check if left mouse button is pressed
            print(f"Mouse moving with button pressed at {pos.x():.0f},{pos.y():.0f}")
        super().mouseMoveEvent(event)
    
    
    def viewportEvent(self, event):
        if event.type() == QEvent.Enter:
            self.setStyleSheet("background: rgba(0, 150, 255, 60);")
    
        elif event.type() == QEvent.Leave:
            self.setStyleSheet("")
    
        return super().viewportEvent(event)