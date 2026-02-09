#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 03:57:38 2026

@author: benny
"""

import sys
import numpy as np
import pyvista as pv
from pyvistaqt import QtInteractor
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import QThread, Signal
import time

# Worker thread to generate new Z data
class UpdateThread(QThread):
    data_updated = Signal(np.ndarray)  # emit new Z array

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.running = True
        self.t = 0

    def run(self):
        while self.running:
            # Example: dynamic sine-cosine wave
            z = np.sin(0.3 * self.x + 0.1*self.t) * np.cos(0.3 * self.y + 0.1*self.t)
            self.data_updated.emit(z)
            self.t += 1
            time.sleep(0.05)  # ~20 FPS

    def stop(self):
        self.running = False
        self.wait()

# Main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyVista 3D Surface with Dynamic Z")

        # Layout
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        # PyVista plotter
        self.plotter = QtInteractor(self)
        layout.addWidget(self.plotter.interactor)

        # Create surface
        self.x = np.linspace(0, 10, 100)
        self.y = np.linspace(0, 10, 100)
        self.x, self.y = np.meshgrid(self.x, self.y)
        self.z = np.sin(0.3*self.x) * np.cos(0.3*self.y)
        self.grid = pv.StructuredGrid(self.x, self.y, self.z)
        self.mesh_actor = self.plotter.add_mesh(self.grid, show_edges=True, cmap="viridis")
        
        #self.plotter.show_axes()
        self.plotter.reset_camera()
        self.plotter.show_grid(color='gray', grid='back', location='outer')

        # Start worker thread
        self.thread = UpdateThread(self.x, self.y)
        self.thread.data_updated.connect(self.update_surface)
        self.thread.start()

    def update_surface(self, new_z):
        """Update the surface mesh with new Z values"""
        # Update grid points
        points = np.c_[self.x.ravel(), self.y.ravel(), new_z.ravel()]
        self.grid.points = points
        self.plotter.update()  # refresh rendering

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())


