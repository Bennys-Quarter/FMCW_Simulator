#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 00:09:50 2026

@author: bennys-quarter
"""

from PySide6.QtWidgets import QGroupBox
from PySide6.QtCore import QPoint, Qt, QMimeData
from PySide6.QtGui import QDrag

class DraggableMixin:
    """Mixin to add drag & reset behavior to any widget"""
    _global_drag_active = False # global atrribute (Attention: not thread safe!)
    
    def enable_drag(self):
        self._drag_active = False
        self._drag_position = QPoint()
        self._original_pos = self.pos()
        self._original_parent = self.parentWidget()
        self._original_geometry = self.geometry()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            DraggableMixin._global_drag_active = True
            if self.parentWidget() != self.window():
                
                #Create new instance
                copy = type(self)(self.parentWidget())
                copy.setObjectName(str(self.title))
                copy.setGeometry(self.geometry())
                copy.setStyleSheet(self.styleSheet())
                self.parent().layout().addWidget(copy)
                copy.show()
                
                #drag = QDrag(self)
                #mimeData = QMimeData()
                #drag.setMimeData(mimeData)
                #drag.exec(Qt.DropAction.MoveAction)
                
                pos_in_window = self.mapToGlobal(QPoint(0, 0))
                self.setParent(self.window()) 
                pos_in_new_parent = self.parent().mapFromGlobal(pos_in_window)
                self.move(pos_in_new_parent)       
                self.raise_()                  
                self.show() 
                
            self._drag_active = True
            self._drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()
                 
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if getattr(self, "_drag_active", False):
            new_pos = event.globalPosition().toPoint() - self._drag_position
            self.move(new_pos)
                
            event.accept()
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if getattr(self, "_drag_active", False):
            DraggableMixin._global_drag_active = False
            self._drag_active = False
            self.move(self._original_pos)
            
            # Delete Widget
            parent = self.parentWidget()
            if parent and parent.layout():
                parent.layout().removeWidget(self)
            self.setParent(None)
            self.deleteLater()
            
            event.accept()
        else:
            super().mouseReleaseEvent(event)