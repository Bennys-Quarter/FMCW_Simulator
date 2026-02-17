# main_window.py
from PySide6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QGraphicsView
from app.ui_compiled.ui_main_window import Ui_MainWindow

from app.core.app_state import AppState

from app.widgets.box_drone import BoxDrone
from app.widgets.box_pedestrian import BoxPedestrian
from app.widgets.box_truck import BoxTruck
from app.widgets.plot_widget import PlotWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(1280, 720)
        self.setWindowTitle("FMCW Simulator")
        
        self.setAcceptDrops(True)
        
        self.state = AppState()
        
        self.f_start_ln = self.findChild(QLineEdit, "lineEdit_f_start")
        self.f_BW_ln = self.findChild(QLineEdit, "lineEdit_f_BW")
        self.f_s_ln = self.findChild(QLineEdit, "lineEdit_f_s")
        self.t_c_ln = self.findChild(QLineEdit, "lineEdit_t_c")
        self.t_pri_ln = self.findChild(QLineEdit, "lineEdit_t_pri")
        self.t_pre_ln = self.findChild(QLineEdit, "lineEdit_t_pre")
        self.t_fly_ln = self.findChild(QLineEdit, "lineEdit_t_fly")
        self.t_wait_ln = self.findChild(QLineEdit, "lineEdit_t_wait")
        self.n_sample_ln = self.findChild(QLineEdit, "lineEdit_n_sample")
        self.n_ramps_ln = self.findChild(QLineEdit, "lineEdit_n_ramps")
        
        self.param_settings = {
        "f_start" : self.f_start_ln ,
        "f_BW" : self.f_BW_ln ,
        "f_s" : self.f_s_ln ,
        "t_c" : self.t_c_ln ,
        "t_pri" : self.t_pri_ln,
        "t_pre" : self.t_pre_ln ,
        "t_fly" : self.t_fly_ln ,
        "t_wait" : self.t_wait_ln  ,
        "n_sample" : self.n_sample_ln ,
        "n_ramps" : self.n_ramps_ln
        }
        
        self.state.fmcw_settings = self.convert_fmcw_to_ui_units(self.state.fmcw_settings)
        self.on_chirp_param_changed()
        
        self.fmcw_apply_btn = self.findChild(QPushButton, "applyAndSaveButton")
        self.fmcw_show_btn = self.findChild(QPushButton, "showButton")
        self.canvas = self.findChild(PlotWidget, "plotWidget")
        
        self.fmcw_apply_btn.clicked.connect(self.on_apply_clicked)
        self.fmcw_show_btn.clicked.connect(self.on_show_clicked)
        
        self.state.fmcwSettingsChanged.connect(self.on_chirp_param_changed)

    
    def on_apply_clicked(self):
        setting = {name:widget.text() for name, widget in self.param_settings.items()}
        self.state.fmcw_settings = setting
    
    
    def on_show_clicked(self):
        self.canvas.update_plots()
    

    def on_chirp_param_changed(self):
        keys = self.state.fmcw_settings.keys()
        for key in keys:
            self.param_settings[key].setText(str(self.state.fmcw_settings[key]))
    
            
    @staticmethod
    def convert_fmcw_to_ui_units(params: dict) -> dict:
        HZ_TO_MHZ = 1e-6
        S_TO_US = 1e6
        return {
            "f_start": params["f_start"] * HZ_TO_MHZ,
            "f_BW": params["f_BW"] * HZ_TO_MHZ,
            "f_s": params["f_s"] * HZ_TO_MHZ,
    
            "t_c": params["t_c"] * S_TO_US,
            "t_pri": params["t_pri"] * S_TO_US,
            "t_pre": params["t_pre"] * S_TO_US,
            "t_fly": params["t_fly"] * S_TO_US,
            "t_wait": params["t_wait"] * S_TO_US,
    
            "n_sample": params["n_sample"],
            "n_ramps": params["n_ramps"],
        }   
        