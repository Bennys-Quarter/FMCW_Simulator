#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 17:20:07 2026

@author: benny

This Example shows how to generate one frame of FMCW Radar Data

"""

from models.fmcw_radar import FMCWRadar
from processing.fmcw_processing import FMCWSignalProcessor
from file_handler import FileHandler


if __name__ == "__main__":
    
    # 1. STEP Setup
    
    file_handler = FileHandler()
    chirp_param, target_param = file_handler.read_input(path="../input/")
    
    radar = FMCWRadar(chirp_param, target_param)
    
    processor = FMCWSignalProcessor()
    
    processor.set_data_cube_shape(radar.n_sample, radar.n_ramps)
    
    # 2. STEP Processing
    
    raw_data = radar.get_radar_scan()
    
    processor.process_frame(raw_data, case=2)
    
    # 3. STEP Ploting
    
    processor.plot_range_fft()