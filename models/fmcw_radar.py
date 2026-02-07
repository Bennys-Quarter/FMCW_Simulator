import numpy as np
import matplotlib.pyplot as plt
from scipy import constants 


class FMCWRadar:
    def __init__(self, chirp_param, target_param):
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
        self.t = None
        
        self.set_chirp_parameters(chirp_param)
        self.set_sampling_times(self.t_pri, self.t_pre, self.t_c, self.n_sample, self.n_ramps)

        # TODO: Read all specified target inputs from file
        # Target parameters  
        self.object_ranges = []       # in meters
        self.object_velocities = []   # in m/s

        self.set_target_parameters(target_param)

        # Static system parameters
        self.c = constants.speed_of_light 
        self.k_b = constants.Boltzmann
        self.G = 10 ** (0 / 10)         # LNA and antenna gain in dB
        self.F_r = 10 ** (13 / 10)      # Noise factor
        self.L = 10 ** (10 / 10)        # Environment Losses
        self.T_n = 290                  # Thermal nois in °Kelvin


        # Performance parameter
        self.R_max = self.c/(2*self.f_BW)


    def set_chirp_parameters(self, chirp_param:dict ):
        if chirp_param == None: return

        param = chirp_param['signal_parameters']
        for key in param:
            setattr(self, key, param[key])

        self.k = self.f_BW / self.t_c

    
    def set_target_parameters(self, target_param:dict):
        if target_param == None: return

        targets = target_param['targets']
        if targets == None: return
        for param in targets:
            for key in param:
                if key == "range_m":
                    self.object_ranges.append(param[key]) 
                if key == "velocity_mps":
                    self.object_velocities.append(param[key]) 
        


    def set_sampling_times(self, t_pri, t_pre, t_c, n_sample, n_ramps):
        t = np.zeros(n_sample * n_ramps)

        # Ramp Sequence
        for i in range(n_ramps):            
            t_chirp = np.linspace(i*t_pri, t_pre + t_c + i*t_pri, n_sample)
            t[n_sample * i : n_sample + n_sample * i] = t_chirp[:]

        self.t = t


    def generate_chirp(self, t):
        """Generate transmitted FMCW chirp."""
        return np.cos(2 * np.pi * (self.f_start * t + 0.5 * self.k * t ** 2))


    def simulate_received(self, t, r):
        """Simulate the received signal with delay based on target range."""
        tau = 2 * r / self.c  # Round-trip delay
        t_delayed = t - tau
        received = np.cos(2 * np.pi * (self.f_start * t_delayed + 0.5 * self.k * t_delayed ** 2))
        return received


    def mix_signals(self, s_tx, s_rx):
        """Mix transmitted and received signals (simulate mixer output)."""
        return s_tx * s_rx


    def intermediate_signal(self, t, r, v):
        """Simulate the intermediate signal"""
        t_next = self.t_pri - self.t_c
        r = r + v * t 
        tau = 2 * r / self.c  # Round-trip delay 
        s_if = np.cos(2 * np.pi * (self.f_start * tau + self.k * tau * (t%(self.t_c + t_next))
                                           - self.k * tau * (r / self.c ))) 
        return s_if
    

    def aditive_noise(self, w_fun=""):
        """
        Aditive Johnson–Nyquist noise model
        """
        
        sigma = self.k_b * self.T_n * self.f_s
        sigma_sample = np.sqrt(sigma)
        
        return np.random.normal(0, sigma_sample, self.n_sample)
        

    def get_radar_scan(self):
        """ 
        Scans the environment for one single frame i.e.: one ramp sequence
        Creation of an array of raw data samples
        """
        # Data Frame of baseband signal
        data = np.zeros(self.n_sample * self.n_ramps)

        # Simulated baseband signal for each specified target
        for i_t in range(len(self.object_ranges)):
            object_baseband_response = np.zeros(self.n_sample * self.n_ramps)
            r = self.object_ranges[i_t] 
            v = self.object_velocities[i_t]
            
            # Create Ramp Sequence and baseband response
            for i in range(self.n_ramps):
                t_chirp = np.linspace(0, self.t_c, self.n_sample) + i * self.t_pri

                chirp_response = self.intermediate_signal(t_chirp, r, v) + self.aditive_noise()
                object_baseband_response[self.n_sample * i : self.n_sample + self.n_sample * i] = chirp_response[:]

            # Superposition of all object S_if response signals
            data = data + object_baseband_response

        return data


    def plot_transmit_chirp(self):
        """ Plot the frequency domain up chirp signal """
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


    def plot_raw_data(self, raw_data):
        """ Plot the time data sample values of all chirps"""

        plt.figure(1)
        for i in range(4):
            plt.plot(self.t[self.n_sample * i : self.n_sample + self.n_sample * i]*1e6, 
                     raw_data[self.n_sample * i : self.n_sample + self.n_sample * i])
        
        plt.title("Time domain intermediate signal of first four chirps")
        plt.xlabel('Time (μs)')
        plt.ylabel('Amplitude')

        plt.figure(2)
        for i in range(self.n_ramps):
            plt.plot(raw_data[self.n_sample * i : self.n_sample + self.n_sample * i])

        plt.xlabel('Sample')
        plt.ylabel('Amplitude')

        plt.show()