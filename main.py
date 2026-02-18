import yaml
import re
import numpy as np

from models.fmcw_radar import FMCWRadar
from processing.simple_processing import SimpleSignalProcessor
from file_handler import FileHandler

if __name__ == '__main__':
    # Load input parameters 
    f_handler = FileHandler()
    chirp_param, target_param = f_handler.read_input()

    radar = FMCWRadar(chirp_param, target_param)
    processor = SimpleSignalProcessor()
    
    processor.set_data_cube_shape(radar.n_sample, radar.n_ramps) # 2D plane

    raw_data = radar.get_radar_scan()
    processor.process_frame(raw_data)
    
    # processor.plot_doppler_fft() 

    processor.plot_RD_map(disp="2D")
    
    #%% Functions
    
    radar.plot_transmit_chirp()
    
    # processor.plot_range_fft()
    # radar.plot_raw_data(raw_data)
    
