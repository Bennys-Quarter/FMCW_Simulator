import numpy as np
import matplotlib.pyplot as plt

class FMCWRadar:
    def __init__(self, f_start, f_end, t_chirp, fs, target_range=100, c=3e8):
        """
        Initialize the FMCW radar parameters.

        Parameters:
        - f_start: Start frequency of chirp (Hz)
        - f_end: End frequency of chirp (Hz)
        - T_chirp: Duration of chirp (seconds)
        - fs: Sampling frequency (Hz)
        - target_range: Distance to target (meters)
        - c: Speed of light (m/s)
        """

        self.f_start = f_start
        self.f_end = f_end
        self.T_chirp = t_chirp
        self.fs = fs
        self.target_range = target_range
        self.c = c

        self.k = (f_end - f_start) / t_chirp  # Chirp rate (Hz/s)
        self.t = np.arange(0, t_chirp, 1 / fs)  # Time array


    def generate_chirp(self):
        """Generate transmitted FMCW chirp."""
        return np.cos(2 * np.pi * (self.f_start * self.t + 0.5 * self.k * self.t ** 2))


    def simulate_received(self):
        """Simulate the received signal with delay based on target range."""
        tau = 2 * self.target_range / self.c  # Round-trip delay
        t_delayed = self.t - tau
        received = np.cos(2 * np.pi * (self.f_start * t_delayed + 0.5 * self.k * t_delayed ** 2))
        return received


    def mix_signals(self, s_tx, s_rx):
        """Mix transmitted and received signals (simulate mixer output)."""
        return s_tx * s_rx


    def intermediate_signal(self):
        """Simulate the intermediate signal"""
        tau = 2 * self.target_range / self.c  # Round-trip delay
        intermediate = np.cos(2 * np.pi * (self.f_start * tau + self.k * tau * self.t
                                           - self.k * tau * (self.target_range / self.c )))

