# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QGroupBox
from app.ui_compiled.ui_box_pedestrian import Ui_BoxPedestrian
from app.utils.drag_and_drop import DraggableMixin

class BoxPedestrian(DraggableMixin, QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_BoxPedestrian()
        self.ui.setupUi(self)
        
        self.enable_drag()
        

