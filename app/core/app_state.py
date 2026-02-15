from PySide6.QtCore import QObject, Signal

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

        # FMCW - Settings
        self._fmcw_settings = {
        "f_start" : None,
        "f_BW" : None,
        "f_s" : None,
        "t_c" : None,
        "t_pri" : None,
        "t_pre" : None,
        "t_fly" : None,
        "t_wait" : None,
        "n_sample" : None,
        "n_ramps" : None
        }
        
    # ---- Properties ----
    
    @property
    def fmcw_settings(self):
        return self._fmcw_settings
    
    @fmcw_settings.setter
    def fmcw_settings(self, value):
        if value != self.fmcw_settings:
            self._fmcw_settings = value
            self.fmcwSettingsChanged.emit(value)