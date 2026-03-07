import yaml
import re
import numpy as np
import sys

from models.fmcw_radar import FMCWRadar
from processing.fmcw_processing import FMCWSignalProcessor
from file_handler import FileHandler


from PySide6.QtWidgets import QApplication
from app.core.app_state import AppState
from app.windows.main_window import MainWindow  # your wrapper class


def cleanup():
    state = AppState()
    
    for t in state.threads:
        t.stop()
    
    for w in QApplication.topLevelWidgets():
        w.close()
    

def app():
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(cleanup)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    

    
    #app()
    
    
    
    
    
