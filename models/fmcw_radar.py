import numpy as np
import matplotlib.pyplot as plt
from scipy import constants 
from scipy.signal import cheby1, filtfilt


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

        # Target parameters  
        self.target_params = {
            "targets": []
                }
        
        self.object_ranges = []       # in meters
        self.object_velocities = []   # in m/s

        self.set_target_parameters(target_param)

        # Static system parameters
        self.c = constants.speed_of_light 
        self.k_b = constants.Boltzmann
        self.G = 10 ** (14 / 10)        # antenna gain in dBi
        self.G_LNA = 10 ** (30 / 10)    # LNA gain
        self.F_r = 10 ** (35 / 10)      # Noise factor
        self.L = 10 ** (10 / 10)        # Environment Losses
        self.T_n = 290                  # Thermal nois in °Kelvin

        self.wavelength = self.c / self.f_start
        self.slope = self.f_BW / self.t_c

        # Performance parameter
        self.R_max = (self.c/(2*self.slope)) * (self.f_s/2)
        self.V_max = (self.wavelength/(4 * self.t_pri))


    def set_chirp_parameters(self, chirp_param:dict ):
        if chirp_param == None: return

        param = chirp_param['signal_parameters']
        for key in param:
            setattr(self, key, param[key])

        self.k = self.f_BW / self.t_c
        
    
    def clear_target_parameters(self):
        self.object_ranges = []       # in meters
        self.object_velocities = []   # in m/s

    
    def set_target_parameters(self, target_param:dict):
        if target_param == None: return

        targets = target_param['targets']
        if targets == None: return
        for t in targets:
            self.target_params["targets"].append(t)
    

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
        sigma_sample = np.sqrt(sigma) * self.F_r
        
        return np.random.normal(0, sigma_sample, self.n_sample)
        

    def get_radar_scan(self):
        """ 
        Scans the environment for one single frame i.e.: one ramp sequence
        Creation of an array of raw data samples
        """
        # Data Frame of baseband signal
        data = np.zeros(self.n_sample * self.n_ramps)
        targets = self.target_params['targets']

        # Simulated baseband signal for each specified target
        if targets:
            for target in targets:
                object_baseband_response = np.zeros(self.n_sample * self.n_ramps)
                r = target["range_m"]
                v = target["velocity_mps"]
                rcs = target["rcs_dBsm"]
                
                # Create Ramp Sequence and baseband response
                for i in range(self.n_ramps):
                    t_chirp = np.linspace(0, self.t_c, self.n_sample) + i * self.t_pri
    
                    chirp_response = self.attenutation(r, rcs) * self.intermediate_signal(t_chirp, r, v) + self.aditive_noise()
                    object_baseband_response[self.n_sample * i : self.n_sample + self.n_sample * i] = chirp_response[:]
    
                # Superposition of all object S_if response signals
                data = data + object_baseband_response
        else:
            
            object_baseband_response = np.zeros(self.n_sample * self.n_ramps)
            for i in range(self.n_ramps):
                chirp_response = self.aditive_noise()
                object_baseband_response[self.n_sample * i : self.n_sample + self.n_sample * i] = chirp_response[:]

            data = data + object_baseband_response
            
        return data
    
    
    def calculate_IF_signal(self):
        """
        Calculates the normalized mixed signal raw data after low pass filtering 
        for all targets in the scene

        Returns
        -------
        
        data 
        """

        fs = self.f_s       
        t_int = self.t_c
        t = np.arange(0, t_int , 1/fs)
        
        # Transmit signal
        s_tx = np.exp(1j * 2*np.pi * (self.f_start*t + 0.5*self.slope*t**2))
        
        # Chebyshev filter parameters
        order = 6                        # filter order
        ripple = 1                       # passband ripple (dB)
        cutoff = (fs/2) - 1 * 1e6        # cutoff frequency
        
        # Design filter
        b, a = cheby1(order, ripple, cutoff/(fs/2), btype='low')
        
        data = np.zeros((1, self.n_sample))
        s_rx = np.zeros((1, self.n_sample), dtype=complex)
        
        targets = self.target_params['targets']

        if targets:
            for target in targets:
                
                # Target
                r = target["range_m"]
                sigma = 10**(target["rcs_dBsm"]/10)
                
                tau = 2 * r / self.c
                
                t_del = t - tau
                
                A = np.sqrt(sigma) / (r**2)
                
                s_rx[0] += A * np.exp(1j * 2*np.pi * (self.f_start*t_del + 0.5*self.slope*t_del**2)) 
        
        # Mixing (THIS produces IF)
        data = s_tx * np.conj(s_rx[0])
        data = data / np.max(np.abs(data))    # Normalize 
        data = filtfilt(b, a, data)
        
        return data
    
    
    def attenutation(self, r, rcs) -> float:
        """
        Returns attenuation in dB relative to reference_distance.
        Radar equation for recived power Pr
        
        """
        if r < 1e-2 : return 1.0
        
        Pt = 1.0 # in Watts
        c = 3e8
        
        # Convert RCS dBsm → linear (m^2)
        sigma = 10 ** (rcs / 10)
        
        # Convert antenna gain dBi → linear
        G = 10 ** (self.G / 10)
        
        Pr = (Pt * (G ** 2) * (self.wavelength ** 2) * sigma / ((4 * np.pi) ** 3 * r ** 4)) * self.G_LNA
        A_r = np.sqrt(Pr)
        return float(A_r)


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

        fig = plt.figure(figsize=(10,5))
        ax = fig.add_subplot()
        ax.set_title('FMCW Radar Signal in Frequency Domain')
        ax.plot(n_0*1e6, f_up(n_0)*1e-6, '--', color="gray")
        ax.plot(n_1*1e6, f_up(n_1)*1e-6, color="red")
        d_2 = t_1 * (self.k + ((self.f_BW + (self.k * self.t_pre)) / self.t_fly) )
        ax.plot(n_2*1e6, f_down(n_2, d_2)*1e-6, '--', color="gray")
        ax.plot(n_3*1e6, f_wait*1e-6, '--', color="gray")
        ax.set_xlabel('Time (μs)')
        ax.set_ylabel('Frequency (MHz)')

        sections = ['Prepayload', 'Payload', 'Flyback', 'Wait']
        section_ends = [self.t_pre*1e6, t_1*1e6, t_2*1e6, t_3*1e6]
        for i, label in enumerate(sections):
            ax.axvline(section_ends[i], color='gray', linestyle='--', linewidth=0.8)
            x_text = section_ends[i - 1] + (section_ends[i] - section_ends[i - 1]) / 2 if i > 0 else section_ends[i] / 2
            ax.text(x_text, self.f_start * 1e-6 + (self.k * t_1) * 1e-6, label, ha='center', va='bottom')

        ax.grid(True)
        ax.set_in_layout(False)
        
        return fig
    

    def plot_raw_data(self, raw_data):
        """ Plot the time data sample values of all chirps"""

        fig1 = plt.figure(1)
        ax1 = fig1.add_subplot()
        
        for i in range(4):
            ax1.plot(self.t[self.n_sample * i : self.n_sample + self.n_sample * i]*1e6, 
                     raw_data[self.n_sample * i : self.n_sample + self.n_sample * i])
        
        ax1.set_title("Time domain intermediate signal of first four chirps")
        ax1.set_xlabel('Time (μs)')
        ax1.set_ylabel('Amplitude')

        return fig1
    
    
    def plot_mixed_signal(self):
        fig2 = plt.figure(2)
        ax2 = fig2.add_subplot()
        
        data = self.calculate_IF_signal()
        
        ax2.plot(np.real(data)) 
        ax2.grid("on")
                
        return fig2