import numpy as np
import matplotlib.pyplot as plt

class FMCWRadar:
    def __init__(self, chirp_param):
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

        # System parameters
        self.c = 299792458 # m/s
        self.t = None

        # Chirp parameters
        self.f_start = None
        self.f_BW = None
        self.f_s = None
        self.t_c = None
        self.t_pri = None
        self.t_pre = None
        self.t_fly = None
        self.t_wait = None
        self.k = None
        self.n_sample = None
        self.n_ramps = None
        self.waveform_type = None

        self.set_chirp_parameters(chirp_param)

        # Target parameters


    def set_chirp_parameters(self, chirp_param):
        param = chirp_param['signal_parameters']
        for key in param:
            setattr(self, key, param[key])

        self.k = self.f_BW / self.t_c


    def generate_chirp(self):
        """Generate transmitted FMCW chirp."""
        return np.cos(2 * np.pi * (self.f_start * self.t + 0.5 * self.k * self.t ** 2))


    def simulate_received(self, r):
        """Simulate the received signal with delay based on target range."""
        tau = 2 * r / self.c  # Round-trip delay
        t_delayed = self.t - tau
        received = np.cos(2 * np.pi * (self.f_start * t_delayed + 0.5 * self.k * t_delayed ** 2))
        return received


    def mix_signals(self, s_tx, s_rx):
        """Mix transmitted and received signals (simulate mixer output)."""
        return s_tx * s_rx


    def intermediate_signal(self, r):
        """Simulate the intermediate signal"""
        tau = 2 * r / self.c  # Round-trip delay
        intermediate = np.cos(2 * np.pi * (self.f_start * tau + self.k * tau * self.t
                                           - self.k * tau * (r / self.c )))

