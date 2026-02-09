import yaml
import re
import numpy as np
import sys

from models.fmcw_radar import FMCWRadar
from processing.fmcw_processing import FMCWSignalProcessor
from file_handler import FileHandler

import sys
from PySide6.QtWidgets import QApplication
from app.windows.main_window import MainWindow  # your wrapper class


def app():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    #%% Load input parameters 
    
    f_handler = FileHandler()
    chirp_param, target_param = f_handler.read_input()

    radar = FMCWRadar(chirp_param, target_param)
    processor = FMCWSignalProcessor()
    
    processor.set_data_cube_shape(radar.n_sample, radar.n_ramps) # 2D plane


    #%% Functions
    
    # raw_data = radar.get_radar_scan()
    
    # processor.process_frame(raw_data, case=2)
    
    # radar.plot_transmit_chirp()
    
    # radar.plot_raw_data(raw_data)
    
    # processor.plot_range_fft(option="nci")
    
    # processor.plot_doppler_fft()
    
    # processor.plot_RD_map(disp="3D")

    #%% Thermal Noise floor
    
    # sigma = radar.k_b * radar.T_n * radar.f_s
    
    # P_n = (sigma * 1.5) / radar.n_sample
    
    # A_noise_bin = 20 * np.log10(np.sqrt(P_n))
    
    # print("Thermal Noise:", A_noise_bin)
    
    #%% app
    
    app()
    
    
    
    
    
