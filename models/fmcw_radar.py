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


    def plot_transmit_chirp(self):
        """ Plot the frequency domain up chirp signal"""
        t_1 = self.t_pre + self.t_c
        t_2 = self.t_c+self.t_pre+self.t_fly
        t_3 = self.t_c+self.t_pre+self.t_fly+self.t_wait

        n_0 = np.linspace(0, self.t_pre, int(self.t_pre/(1/self.f_s)))
        n_1 = np.linspace(self.t_pre, t_1, int(self.t_c / (1 / self.f_s)))
        n_2 = np.linspace(t_1, t_2, int(self.t_fly / (1 / self.f_s)))
        n_3 = np.linspace(t_2, t_3, int(self.t_wait / (1 / self.f_s)))

        f_up = lambda n : self.k * n + self.f_start
        f_down = lambda n, d : -((self.f_BW + (self.k * self.t_pre)) / self.t_fly) * n  + d + self.f_start
        f_wait = np.ones(len(n_3)) * self.f_start

        plt.figure(figsize=(10,5))
        plt.title('FMCW Radar Signal in Frequency Domain')
        plt.plot(n_0*1e6, f_up(n_0)*1e-6, '--', color="gray")
        plt.plot(n_1*1e6, f_up(n_1)*1e-6, color="red")
        d_2 = t_1 * (self.k + ((self.f_BW + (self.k * self.t_pre)) / self.t_fly) )
        plt.plot(n_2*1e6, f_down(n_2, d_2)*1e-6, '--', color="gray")
        plt.plot(n_3*1e6, f_wait*1e-6, '--', color="gray")
        plt.xlabel('Time (μs)')
        plt.ylabel('Frequency (MHz)')

        sections = ['Prepayload', 'Payload', 'Flyback', 'Wait']
        section_ends = [self.t_pre*1e6, t_1*1e6, t_2*1e6, t_3*1e6]
        for i, label in enumerate(sections):
            plt.axvline(section_ends[i], color='gray', linestyle='--', linewidth=0.8)
            x_text = section_ends[i - 1] + (section_ends[i] - section_ends[i - 1]) / 2 if i > 0 else section_ends[i] / 2
            plt.text(x_text, self.f_start * 1e-6 + (self.k * t_1) * 1e-6, label, ha='center', va='bottom')

        plt.grid(True)
        plt.tight_layout()
        plt.show()