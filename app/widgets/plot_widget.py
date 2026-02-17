#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 19:59:07 2026

@author: benny
"""
import random

from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from app.core.app_state import AppState


class PlotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setParent(parent)
        
        self.state = AppState()
        
        self.layout = QVBoxLayout(self)
        
        self.fig = self.state.radar.plot_transmit_chirp()
        self.canvas = FigureCanvas(self.fig)
        
        self.layout.addWidget(self.canvas)
        
        self.canvas.draw()
        
    
    def update_plots(self):
        self.fig = self.state.radar.plot_transmit_chirp()
        self.layout.removeWidget(self.canvas)
        self.canvas = FigureCanvas(self.fig)
        self.layout.addWidget(self.canvas)
        self.canvas.draw()