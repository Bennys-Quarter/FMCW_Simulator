
from PySide6.QtWidgets import QGroupBox
from app.ui_compiled.ui_box_drone import Ui_Box_Drone
from app.utils.drag_and_drop import DraggableMixin

class BoxDrone(DraggableMixin, QGroupBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Box_Drone()
        self.ui.setupUi(self)
        
