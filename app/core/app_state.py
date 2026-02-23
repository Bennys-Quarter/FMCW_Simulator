from PySide6.QtCore import QObject, Signal

from models.fmcw_radar import FMCWRadar
from processing.fmcw_processing import FMCWSignalProcessor
from file_handler import FileHandler

class AppState(QObject):
    _instance = None
    
    fmcwSettingsChanged = Signal(str)
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            QObject.__init__(cls._instance)
        return cls._instance


    def __init__(self):
        # Prevent reinitialization
        if getattr(self, "_initialized", False):
            return
        self._initialized = True
        
        self.f_handler = FileHandler()
        chirp_param, target_param = self.f_handler.read_input()
        
        self.radar = FMCWRadar(chirp_param, target_param)
        self.processor = FMCWSignalProcessor()
        
        # FMCW - Settings
        self._fmcw_settings = {
        "f_start" : self.radar.f_start,
        "f_BW" : self.radar.f_BW,
        "f_s" : self.radar.f_s,
        "t_c" : self.radar.t_c,
        "t_pri" : self.radar.t_pri,
        "t_pre" : self.radar.t_pre,
        "t_fly" : self.radar.t_fly,
        "t_wait" : self.radar.t_wait,
        "n_sample" : self.radar.n_sample,
        "n_ramps" : self.radar.n_ramps
        }
        
        
    # ---- Properties ----
    
    @property
    def fmcw_settings(self):
        return self._fmcw_settings
    
    @fmcw_settings.setter
    def fmcw_settings(self, value):
        if value != self.fmcw_settings:
            self._fmcw_settings = value
            self.radar.f_start =  float(self._fmcw_settings["f_start"]) * 1e6
            self.radar.f_BW = float(self._fmcw_settings["f_BW"])*1e6
            self.radar.f_s  = float(self._fmcw_settings["f_s"])*1e6
            self.radar.t_c = float(self._fmcw_settings["t_c"])*1e-6
            self.radar.t_pri = float(self._fmcw_settings["t_pri" ]) *1e-6
            self.radar.t_pre = float(self._fmcw_settings["t_pre"]) *1e-6
            self.radar.t_fly = float(self._fmcw_settings["t_fly"]) *1e-6
            self.radar.t_wait = float(self._fmcw_settings["t_wait"]) *1e-6
            self.radar.n_sample = int(self._fmcw_settings["n_sample"])
            self.radar.n_ramps = int(self._fmcw_settings["n_ramps"])
            
            self.fmcwSettingsChanged.emit(value)