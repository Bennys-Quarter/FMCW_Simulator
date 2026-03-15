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
        self.layout = None
        
        self.canvas = None
        self.thread = None
        
        self.plots = {
            "RD-Map": [self.draw_RD_map],
            "Signals": [ self.draw_chirp, self.draw_mixed_signal, self.draw_range_fft ,  self.draw_doppler_fft]
                }
        
        
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
        plt = FigureCanvas(self.fig)
        self.layout.addWidget(plt)
        

    def draw_chirp(self):
        raw_data = self.state.radar.get_radar_scan()
        fig1, fig2 = self.state.radar.plot_raw_data(raw_data)
        plt = FigureCanvas(fig1)
        self.layout.addWidget(plt)
        
        
    def draw_mixed_signal(self):
        self.state.processor.set_data_cube_shape(self.state.radar.n_sample, 
                                                 self.state.radar.n_ramps)
        raw_data = self.state.radar.get_radar_scan()
        self.state.processor.process_frame(raw_data, case=2)
        fig_range = self.state.processor.plot_range_fft(disp="NCI")
        plt = FigureCanvas(fig_range)
        self.layout.addWidget(plt)
        
    
    def draw_range_fft(self):
        self.state.processor.set_data_cube_shape(self.state.radar.n_sample, 
                                                 self.state.radar.n_ramps)
        raw_data = self.state.radar.get_radar_scan()
        self.state.processor.process_frame(raw_data, case=2)
        fig_range = self.state.processor.plot_range_fft(disp="CFAR")
        plt = FigureCanvas(fig_range)
        self.layout.addWidget(plt)
        #self.canvas.draw()
        
    
    def draw_doppler_fft(self):
        self.state.processor.set_data_cube_shape(self.state.radar.n_sample, self.state.radar.n_ramps)
        raw_data = self.state.radar.get_radar_scan()
        self.state.processor.process_frame(raw_data, case=2)
        fig_doppler = self.state.processor.plot_doppler_fft()
        plt = FigureCanvas(fig_doppler)
        self.layout.addWidget(plt)
        #self.canvas.draw()
        

    def draw_RD_map(self):
        self.canvas = QtInteractor(self)
        
        self.state.processor.set_data_cube_shape(self.state.radar.n_sample, 
                                                 self.state.radar.n_ramps)
        
        raw_data = self.state.radar.get_radar_scan()
        self.state.processor.process_frame(raw_data, case=2)
        rdm = self.state.processor.RD_map[0:self.state.radar.n_sample//2, 0:self.state.radar.n_ramps]
        self.z = rdm 
        self.z = 10*np.log10(np.abs(rdm)**2)
        
        titles = []
        ax_ranges = []
        if self.state.plot_mode["Axis Ticks"] == "bins" :
            ax_ranges = [-self.state.radar.n_ramps//2,
                         self.state.radar.n_ramps//2,
                         0,
                         self.state.radar.n_sample//2,
                         0,
                         -140
                         ]
            titles = [
                "Doppler bins",
                "Range bins",
                "Power in dBfs"]
        elif self.state.plot_mode["Axis Ticks"] == "physical" :
            ax_ranges = [-self.state.radar.V_max,
                         self.state.radar.V_max,
                         0,
                         self.state.radar.R_max,
                         0,
                         -140
                         ]
            titles = [
                "Velocity in m/s",
                "Range in m",
                "Power in dBfs"]
            
        self.canvas.add_text(
                "Range Doppler Map",
                position="upper_edge",
                font_size=18,
                color=self.state.plot_mode["Grid Color"],
            )
        
        if self.state.plot_mode["RDM"] == "3D":
            
            self.x = np.linspace(-self.state.radar.n_ramps//2, self.state.radar.n_ramps//2, self.state.radar.n_ramps)
            self.y = np.linspace(0, self.state.radar.n_sample//2, self.state.radar.n_sample//2)
            self.x, self.y = np.meshgrid(self.x, self.y)
            
            self.grid = pv.StructuredGrid(self.x, self.y, self.z)
            self.grid.dimensions = (self.state.radar.n_ramps, self.state.radar.n_sample//2 , 1)
            self.grid["Power dBfs"] = self.z.ravel()
            
            self.mesh_actor = self.canvas.add_mesh(self.grid, 
                                                   scalars="Power dBfs",
                                                   cmap="viridis",
                                                   clim=self.state.plot_mode["Clim"],
                                                   show_scalar_bar = True,
                                                   scalar_bar_args= {
                                                       "color" : self.state.plot_mode["Grid Color"],
                                                       "vertical" : True
                                                       },
                                                   )
            
            self.canvas.reset_camera()
            self.canvas.camera_position = 'xz'
            self.canvas.add_camera_orientation_widget()
            self.canvas.camera.view_angle = 40.0
            self.canvas.camera.elevation = 50.0
            self.canvas.camera.zoom(1.4)
                          
            self.canvas.show_bounds(
                grid = 'back',
                location = 'outer',
                axes_ranges=ax_ranges,
                bounds = [-self.state.radar.n_ramps//2, 
                          self.state.radar.n_ramps//2,
                          0,
                          self.state.radar.n_sample//2,
                          -140,
                          0
                          ],
                color=self.state.plot_mode["Grid Color"],
                n_ylabels= 4,
                n_zlabels= 5,
                ticks = 'both',
                xtitle = titles[0],
                ytitle = titles[1],
                ztitle = titles[2],
                show_zlabels = False,
                minor_ticks = False,
                padding = 0.0,
                fmt = "{:.0f}"
                )

            self.canvas.set_background(color=self.state.plot_mode["Background Color"])
            
        
        elif self.state.plot_mode["RDM"] == "2D":

            dy = self.state.radar.n_ramps
            dx = self.state.radar.n_sample

            
            self.grid = pv.ImageData(
                dimensions=(self.state.radar.n_sample//2, self.state.radar.n_ramps, 1),
                spacing=(dx, dy, 1),
                origin=(0,0,0)
            )
            
            # Assign scalars — must flatten in column-major ('F') order
            self.grid.point_data["Power (dB)"] = np.abs(rdm).flatten(order="F")
            
            self.mesh_actor = self.canvas.add_mesh(
                self.grid,
                scalars="Power (dB)",
                cmap="viridis",
                show_scalar_bar = True,
                clim=self.state.plot_mode["Clim"],
                scalar_bar_args={
                    "title": "Power in dBfs",
                    "color" : self.state.plot_mode["Grid Color"],
                    "position_y" : 0.02
                    }
            )
            
            self.canvas.show_bounds(
                n_ylabels= 5,
                n_xlabels= 4,
                axes_ranges=[
                    ax_ranges[2], 
                    ax_ranges[3], 
                    ax_ranges[0],
                    ax_ranges[1], 
                    0,0],
                color=self.state.plot_mode["Grid Color"],
                xtitle = titles[1],
                ytitle = titles[0],
                minor_ticks = True,
                fmt = "{:.0f}",
                use_3d_text = False,
                )
            
            self.canvas.set_background(color=self.state.plot_mode["Background Color"])
            
            #self.canvas.camera.tight()
            self.canvas.view_yx()  # top-down 2D view
            self.canvas.camera.zoom(1.1)
            self.canvas.enable_parallel_projection()  # optional for 2D style
        
        
        self.thread = UpdateThread(self.x, self.y)
        self.thread.data_updated.connect(self.update_surface)
        self.thread.start()


    def update_surface(self, new_z):
        """Update the surface mesh with new Z values"""
        if self.state.plot_mode["RDM"] == "3D":
            self.grid["Power dBfs"] = new_z.ravel()
            points = np.c_[self.x.ravel(), self.y.ravel(), new_z.ravel()]
            self.grid.points = points
            self.mesh_actor.mapper.dataset.points = points
            self.mesh_actor.mapper.dataset.Modified()
            self.canvas.render()
            
        elif self.state.plot_mode["RDM"] == "2D":
            self.grid.point_data["Power (dB)"] = new_z.flatten(order="F")
    
            # Tell VTK the data has changed
            self.grid.Modified()      # mark the dataset as modified
            self.canvas.render()      # update the display


    def prepeare_plots(self, option:str, plt_idx:int):
        """
        Draw radar plots depending on the settings in the plot window
        
        option:
            - RDM : Plots a single range doppler map
            - Signals : Plot a the signal result after each processing step 
        Returns
        -------
        None.

        """
        
        self.remove_plots()
        
        self.layout = QVBoxLayout(self)
        
        plt = self.plots[option][plt_idx]

        plt()
        #self.layout.addWidget(self.canvas.interactor)


    def on_stop_triggered(self):
        if self.thread:
            self.thread.stop()
        
    
    def closeEvent(self, event):
        if self.thread:
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