from PySide6.QtWidgets import QGroupBox
from app.ui_compiled.ui_box_truck import Ui_BoxTruck
from app.utils.drag_and_drop import DraggableMixin

class BoxTruck(DraggableMixin, QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_BoxTruck()
        self.ui.setupUi(self)
        
        self.enable_drag()