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

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            
            drag = QDrag(self)
            mime = QMimeData()
            mime.setText(self.objectName())
            drag.setMimeData(mime)
            drag.exec(Qt.DropAction.MoveAction)
    
            