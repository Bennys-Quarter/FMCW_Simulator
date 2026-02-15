# main_window.py
from PySide6.QtWidgets import QMainWindow, QLineEdit, QPushButton
from app.ui_compiled.ui_main_window import Ui_MainWindow

from app.core.app_state import AppState

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
        
        self.setAcceptDrops(True)
        
        self.state = AppState()
        
        self.f_start_input = self.findChild(QLineEdit, "lineEdit_f_start")
        self.f_BW_input = self.findChild(QLineEdit, "lineEdit_f_BW")
        self.f_s_input = self.findChild(QLineEdit, "lineEdit_f_s")
        self.t_c_input = self.findChild(QLineEdit, "lineEdit_t_c")
        self.t_pri_input = self.findChild(QLineEdit, "lineEdit_t_pri")
        self.t_pre_input = self.findChild(QLineEdit, "lineEdit_t_pre")
        self.t_fly_input = self.findChild(QLineEdit, "lineEdit_t_fly")
        self.t_wait_input = self.findChild(QLineEdit, "lineEdit_t_wait")
        self.n_sample_input = self.findChild(QLineEdit, "lineEdit_n_sample")
        self.n_ramps_input = self.findChild(QLineEdit, "lineEdit_n_ramps")
        
        buttons = self.findChildren(QPushButton)  # all QPushButtons
        for b in buttons:
            print(b.objectName())
        
        self.fmcw_apply_btn = self.findChild(QPushButton, "applyAndSaveButton")
        self.fmcw_show_btn = self.findChild(QPushButton, "showButton")
        
        
        self.fmcw_apply_btn.clicked.connect(self.on_apply_clicked)
        self.fmcw_show_btn.clicked.connect(self.on_show_clicked)
        
        
    
    def on_apply_clicked(self):
        settings = {
        "f_start" : self.f_start_input.text(),
        "f_BW" : self.f_BW_input.text(),
        "f_s" : self.f_s_input.text(),
        "t_c" : self.t_c_input.text(),
        "t_pri" : self.t_pri_input.text(),
        "t_pre" : self.t_pre_input.text(),
        "t_fly" : self.t_fly_input.text(),
        "t_wait" : self.t_wait_input.text(),
        "n_sample" : self.n_sample_input.text(),
        "n_ramps" : self.n_ramps_input.text()
        }
        
        self.state.fmcw_settings = settings
        
        print(self.state.fmcw_settings)
    
    
    def on_show_clicked(self):
        pass