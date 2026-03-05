#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 19:59:07 2026

@author: benny
"""

import time
import random
import numpy as np
import pyvista as pv

from pyvistaqt import QtInteractor
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import QThread, Signal, Slot
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from app.core.app_state import AppState


class PlotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setParent(parent)
        self.state = AppState()
        self.layout = QVBoxLayout(self)
        
        self.canvas = None
        self.thread = None
        
    
    def remove_plots(self):
        if self.thread:
            self.thread.stop()
        if self.canvas:
            self.layout.removeWidget(self.canvas)
            self.canvas = None
        
        
    def update_plots(self):
        self.fig = self.state.radar.plot_transmit_chirp()
        self.remove_plots()
        self.canvas = FigureCanvas(self.fig)
        self.layout.addWidget(self.canvas)
        self.canvas.draw()


    def draw_transmitt_chirp(self):
        self.fig = self.state.radar.plot_transmit_chirp()
        self.canvas = FigureCanvas(self.fig)
        self.layout.addWidget(self.canvas)
        self.canvas.draw()


    def draw_RD_map(self):
        self.canvas = QtInteractor(self)
        self.layout.addWidget(self.canvas.interactor)
        
        self.x = np.linspace(-self.state.radar.n_ramps//2, self.state.radar.n_ramps//2, self.state.radar.n_ramps)
        self.y = np.linspace(0, self.state.radar.n_sample//2, self.state.radar.n_sample//2)
        self.x, self.y = np.meshgrid(self.x, self.y)
        
        self.state.processor.set_data_cube_shape(self.state.radar.n_sample, 
                                                 self.state.radar.n_ramps)
        
        raw_data = self.state.radar.get_radar_scan()
        self.state.processor.process_frame(raw_data, case=2)
        rdm = self.state.processor.RD_map[0:self.state.radar.n_sample//2, 0:self.state.radar.n_ramps]
        self.z = rdm 
        self.z = 10*np.log10(np.abs(rdm)**2)
        self.grid = pv.StructuredGrid(self.x, self.y, self.z)
        self.grid.dimensions = (self.state.radar.n_ramps, self.state.radar.n_sample//2 , 1)
        self.grid["scalars"] = self.z.ravel()
        
        self.mesh_actor = self.canvas.add_mesh(self.grid, 
                                               scalars="scalars",
                                               cmap="inferno",
                                               clim=[-140,0]
                                               #show_edges=True
                                               )
    
        
        self.canvas.reset_camera()
        self.canvas.camera_position = [
            (-512, -512, 0),  # camera location (look from negative X)
            (0, 0, 0),    # focal point (center of grid)
            (0, 0, 1)     # up direction
        ]
        self.canvas.camera.view_angle = 30.0
        self.canvas.camera.elevation = 45.0
        
        self.canvas.show_grid(grid='back', location='outer',
                              bounds=[-self.state.radar.n_ramps//2,self.state.radar.n_ramps//2,
                                      0,self.state.radar.n_sample//2,
                                      -160, 0],
                              fmt="%.0f",
                              xtitle="Doppler bins",
                              ytitle="Range bins",
                              ztitle="Power in dBfs")
        
        self.thread = UpdateThread(self.x, self.y)
        self.thread.data_updated.connect(self.update_surface)
        self.thread.start()


    def update_surface(self, new_z):
        """Update the surface mesh with new Z values"""
        self.grid["scalars"] = new_z.ravel()
        points = np.c_[self.x.ravel(), self.y.ravel(), new_z.ravel()]
        self.grid.points = points
        self.mesh_actor.mapper.dataset.points = points
        self.mesh_actor.mapper.dataset.Modified()
        self.canvas.render()


    def on_run_triggered(self):
        self.remove_plots()
        self.draw_RD_map()


    def on_stop_triggered(self):
        self.thread.stop()
        
    
    def closeEvent(self, event):
        self.thread.stop()
        event.accept()


# Worker thread to generate new Z data
class UpdateThread(QThread):
    data_updated = Signal(np.ndarray)  # emit new Z array

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.running = False
        self.t = 0
        self.fps = 20
        self.state = AppState()
        self.state.threads.append(self)


    def run(self):
        self.running = True
        self.state.processor.set_data_cube_shape(self.state.radar.n_sample, 
                                                 self.state.radar.n_ramps)
        while self.running:
            raw_data = self.state.radar.get_radar_scan()
            self.state.processor.process_frame(raw_data, case=2)
            rdm = self.state.processor.RD_map[0:self.state.radar.n_sample//2, 0:self.state.radar.n_ramps]
            self.z = rdm 
            z = 10*np.log10(np.abs(rdm)**2)
            
            self.data_updated.emit(z)
            self.t += 1/self.fps
            time.sleep(1/self.fps)  # ~20 FPS


    def stop(self):
        self.running = False
        self.wait()