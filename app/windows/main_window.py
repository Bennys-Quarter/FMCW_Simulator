# main_window.py
from PySide6.QtWidgets import QMainWindow
from app.ui_compiled.ui_main_window import Ui_MainWindow

from app.widgets.box_drone import BoxDrone
from app.widgets.box_pedestrian import BoxPedestrian
from app.widgets.box_truck import BoxTruck

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(1280, 720)
        self.setWindowTitle("FMCW Simulator")
        
        