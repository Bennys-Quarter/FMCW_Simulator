# main_window.py
from PySide6.QtWidgets import (QApplication, QMainWindow, QLineEdit, 
                               QPushButton, QWidget, QGraphicsView, QMenu, 
                               QFrame, QVBoxLayout, QPushButton, QHBoxLayout,
                               QComboBox, QRadioButton, QSpinBox, QCheckBox)
from PySide6.QtGui import QAction
from app.ui_compiled.ui_main_window import Ui_MainWindow

from app.core.app_state import AppState

from app.widgets.box_drone import BoxDrone
from app.widgets.box_pedestrian import BoxPedestrian
from app.widgets.box_truck import BoxTruck
from app.widgets.plot_widget import PlotWidget
from app.widgets.plot_format_2_2 import PlotFormat_2_2
from app.widgets.plot_format_single import PlotFormatSingle
from app.widgets.plot_fullscreen_popup import PlotFullscreenPopup


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
        self.run_plot_btn = self.findChild(QPushButton, "runPlotButton")
        self.stop_plot_btn = self.findChild(QPushButton, "stopPlotButton")
        self.menu_window = self.findChild(QMenu, "menuPlots")
        self.main_frame = self.findChild(QFrame, "mainFrame")
        self.plot_layout_selector = self.findChild(QComboBox, "plotLayoutSelector")
        self.target_dt_selector = self.findChild(QComboBox, "setTargetDetection")
        self.rd_btn_2D = self.findChild(QRadioButton, "radioButton_2D")
        self.rd_btn_3D = self.findChild(QRadioButton, "radioButton_3D")
        self.rd_btn_black = self.findChild(QRadioButton, "radioButton_black")
        self.rd_btn_white = self.findChild(QRadioButton, "radioButton_white")
        self.rd_btn_bins = self.findChild(QRadioButton, "radioButton_bins")
        self.rd_btn_physical = self.findChild(QRadioButton, "radioButton_physical")
        self.sp_box_min_clim = self.findChild(QSpinBox, "spinMinClimBox")
        self.sp_box_max_clim = self.findChild(QSpinBox, "spinMaxClimBox")
        self.ch_box_target_dt = self.findChild(QCheckBox, "checkBoxTargetDetection")
        
        
        self.plot_fullscreen_action = self.findChild(QAction, "actionFullscreen")
        
        self.canvas_frame = self.findChild(QFrame, "plotFrame")
        self.canvas_frame.setLayout(QVBoxLayout())
        
        self.canvas = None
        self.plot_full_screen_popup = None
        
        self.setting_widgets = [
            self.rd_btn_2D, 
            self.rd_btn_3D, 
            self.rd_btn_black,
            self.rd_btn_white,
            self.rd_btn_bins,
            self.rd_btn_physical, 
            self.sp_box_min_clim, 
            self.sp_box_max_clim, 
            self.run_plot_btn
            ]
        
        self.fmcw_apply_btn.clicked.connect(self.on_apply_clicked)
        self.fmcw_show_btn.clicked.connect(self.on_show_clicked)
        self.state.fmcwSettingsChanged.connect(self.on_chirp_param_changed)
        self.run_plot_btn.clicked.connect(self.on_run_plot_clicked)
        self.stop_plot_btn.clicked.connect(self.on_stop_plot_clicked)
        self.plot_fullscreen_action.triggered.connect(self.on_plot_fullscreen_triggered)
        self.rd_btn_2D.toggled.connect(self.on_plot_setting_changed)
        self.rd_btn_3D.toggled.connect(self.on_plot_setting_changed) 
        self.rd_btn_black.toggled.connect(self.on_plot_setting_changed)
        self.rd_btn_white.toggled.connect(self.on_plot_setting_changed)
        self.rd_btn_bins.toggled.connect(self.on_plot_setting_changed)
        self.rd_btn_physical.toggled.connect(self.on_plot_setting_changed)
        self.sp_box_max_clim.valueChanged.connect(self.on_plot_setting_changed)
        self.sp_box_min_clim.valueChanged.connect(self.on_plot_setting_changed)
        self.plot_layout_selector.currentIndexChanged.connect(self.on_plot_setting_changed)
        self.target_dt_selector.currentIndexChanged.connect(self.on_target_detection_changed)
        self.ch_box_target_dt.checkStateChanged.connect(self.on_target_detection_checked)
        
        
        self.init_settings()
    
    
    def init_settings(self):
        self.on_plot_setting_changed()
        
        
    def add_plots(self):
        # TODO: check settings first before selecting new_entry 
        # Delete all widgets from plot frame 
        layout = self.canvas_frame.layout()
        
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        
        if self.state.plot_mode["Window"] == "RD-Map":
            new_entry = PlotFormatSingle()
            layout.insertWidget(0, new_entry)
            self.canvas = [new_entry.findChild(PlotWidget, "plotWidget")]
        if self.state.plot_mode["Window"] == "Signals":
            new_entry = PlotFormat_2_2()
            layout.insertWidget(0, new_entry)
            self.canvas = [
                new_entry.findChild(PlotWidget, "plotWidget1"),
                new_entry.findChild(PlotWidget, "plotWidget2"),
                new_entry.findChild(PlotWidget, "plotWidget3"),
                new_entry.findChild(PlotWidget, "plotWidget4"),
                ]
    
    
    def set_settings_enabeld(self, enable: bool):
        for w in self.setting_widgets:
            w.setEnabled(enable)


    def on_apply_clicked(self):
        setting = {name:widget.text() for name, widget in self.param_settings.items()}
        self.state.fmcw_settings = setting


    def on_show_clicked(self):
        layout = self.canvas_frame.layout()
        
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        
        new_entry = PlotFormatSingle()
        self.canvas = new_entry.findChild(PlotWidget, "plotWidget")
        self.canvas.layout = layout
        self.canvas.update_plots()
        
    
    def on_target_detection_checked(self):
        if self.ch_box_target_dt.isChecked():
            self.state.set_flag("TargetDetection", True)
        else:
            self.state.set_flag("TargetDetection", False)
            
    
    def on_target_detection_changed(self):
        text = self.target_dt_selector.currentText()
        
        if text == "Single Threshold":
            self.state.set_processing_setting("TargetDetection", "threshold")
        elif text == "CA-CFAR":
            self.state.set_processing_setting("TargetDetection", "CFAR")
        
        


    def on_chirp_param_changed(self):
        keys = self.state.fmcw_settings.keys()
        for key in keys:
            self.param_settings[key].setText(str(self.state.fmcw_settings[key]))
    
    
    def on_run_plot_clicked(self):
        self.add_plots()
        self.set_settings_enabeld(False)
        if self.canvas == None: return
        for i, cnv in enumerate(self.canvas):
            cnv.prepeare_plots(option = self.state.plot_mode["Window"], plt_idx=i)
        
        
    def on_stop_plot_clicked(self):
        for cnv in self.canvas:
            cnv.on_stop_triggered()
        self.canvas = None
        self.set_settings_enabeld(True)
    
    
    def on_plot_fullscreen_triggered(self):
        self.plot_full_screen_popup = None
        if self.canvas == None: return
        self.plot_full_screen_popup = PlotFullscreenPopup(self.main_frame, self.canvas_frame)
    
        
    def on_plot_setting_changed(self):
        if self.rd_btn_2D.isChecked():
            self.state.plot_mode["RDM"] = "2D"
        elif self.rd_btn_3D.isChecked():
            self.state.plot_mode["RDM"] = "3D"
        
        if self.rd_btn_black.isChecked():
            self.state.plot_mode["Background Color"] = "black"
            self.state.plot_mode["Grid Color"] = "white"
        elif self.rd_btn_white.isChecked():
            self.state.plot_mode["Background Color"] = "white"
            self.state.plot_mode["Grid Color"] = "black"
        
        if self.rd_btn_bins.isChecked():
            self.state.plot_mode["Axis Ticks"] = "bins"
        elif self.rd_btn_physical.isChecked():
            self.state.plot_mode["Axis Ticks"] = "physical"
        
        c_max = self.sp_box_max_clim.value()
        c_min = self.sp_box_min_clim.value()
        
        self.state.plot_mode["Window"] = self.plot_layout_selector.currentText()
        
        self.state.plot_mode["Clim"] = [c_min, c_max]
    
    
    def closeEvent(self, event):
        event.ignore()
        
        for w in QApplication.topLevelWidgets():
            if w is not self:
                w.close()
        
        self.deleteLater()
        QApplication.instance().quit()


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
        