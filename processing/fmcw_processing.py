import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray 
from scipy.signal.windows import chebwin
from scipy.fft import fft, fftshift
from scipy.ndimage import maximum_filter

# Signal Processing Chain
# 0.: Input: radar intermediate signal time data frame
# 1.: Range FFT
# 2.: Doppler FFT -> RD - map


class FMCWSignalProcessor():
    """
    Radar signal processor to detect targets in a range doppler map and generate a point cloud

    The most simple form of radar data processing is considered, excluding direction of arrival (DoA) estimation
    """
    def __init__(self):
        self.n_sample: int = None
        self.n_ramps: int = None

        # Data
        self.data = None
        self.r_fft: NDArray = None
        self.RD_map: NDArray = None
        
        # Target List Parameters
        self.target_list = {
            "peak_power_dB": [],
            "idx": [],
        }

        # CA_CFAR parameters
        self.ca_cfar = {
            "training_cells" : 3,
            "guard_cells" : 3,
            "cfar_th" : 0.86
        }
        
        # Single threshold 
        self.t_th = -80
        
        # Signal Processing Chain
        self.pro_chain = {
            0: [],      
            1: [self.range_fft],
            2: [self.range_fft, self.doppler_fft]
        }


    def set_data_cube_shape(self, n_sample, n_ramps, n_spatial = 0):
        """ Determins the shape of the signal processing cube """
        self.n_sample = n_sample
        self.n_ramps = n_ramps


    def frame2cube(self, data_frame): 
        """ Data frame conversion """
        return data_frame.reshape(self.n_ramps, self.n_sample)


    def range_fft(self):
        """ Performs range fft """
        data_fft = np.zeros(np.shape(self.data), dtype=complex)
        w = chebwin(self.n_sample, at = 100)
        self.data = self.data * w
        for i in range(self.n_sample):
            data_fft[i] = fft(self.data[i] , self.n_sample) / (np.sum(w))
        self.r_fft = data_fft[:, :self.data.shape[1]]
        return self.r_fft
    

    def doppler_fft(self):
        """ Perform doppler fft """
        data_fft = np.zeros((self.data.shape[1], self.data.shape[0]), dtype=complex)
        w = chebwin(self.n_ramps , at = 100)
        r_fft = self.r_fft.transpose() * w

        for i in range(self.n_sample):
            re = fft(r_fft[i], self.n_ramps)
            data_fft[i] = fftshift(re) / (np.sum(w))
        
        # Range Doppler Map generation in dBFS
        self.RD_map = data_fft
        return self.RD_map


    def process_frame(self, raw_data, case=2):
        """ Execute the Signal Processing Chain 
        
            cases:
                0: Do nothing
                1: Range FFT
                2: Range FFT + Doppler FFT -> RangeDoppler Map
        """
        self.data = self.frame2cube(raw_data)
        
        for func in self.pro_chain[case]:
            func()
            
            
    def ca_cfar_1d(self, data, gc, tc, th=1):
        """
        1D Cell Averaging CFAR
        
        Parameters
        ----------
        data : array-like
            Input signal (e.g. power spectrum)
        gc : int
            Number of guard cells on each side
        tc : int
            Number of training cells on each side
        th : float
            Threshold scaling factor
            
        Returns
        -------
        threshold : np.ndarray
            CFAR threshold for each cell
        """
        data = np.asarray(data)
        n = len(data)
        threshold = np.zeros(n)
        
        window = gc + tc
        
        for i in range(window, n - window):
        
            leading = data[i - window:i - gc]
            trailing = data[i + gc + 1:i + window + 1]
        
            noise_level = (np.sum(leading) + np.sum(trailing)) / (2 * tc)
        
            threshold[i] = noise_level * th
        
        return threshold
    
    
    def ca_cfar_2d(self, data, gc, tc, th=1):
        """
        2D Cell Averaging CFAR
        
        Parameters
        ----------
        data : 2D array
            Input signal (e.g. range-doppler map)
        gc : int
            Number of guard cells on each side
        tc : int
            Number of training cells on each side
        th : float
            Threshold scaling factor
            
        Returns
        -------
        threshold : np.ndarray
            CFAR threshold for each cell
        """

        data = np.asarray(data)
        rows, cols = data.shape
        threshold = np.zeros_like(data)
        
        window = gc + tc
        
        for i in range(window, rows - window):
            for j in range(window, cols - window):
        
                # Extract full window
                region = data[
                    i - window : i + window + 1,
                    j - window : j + window + 1
                ]
        
                # Remove guard cells + CUT
                guard_region = data[
                    i - gc : i + gc + 1,
                    j - gc : j + gc + 1
                ]
        
                noise_sum = np.sum(region) - np.sum(guard_region)
        
                num_training = region.size - guard_region.size
                noise_level = noise_sum / num_training
        
                threshold[i, j] = noise_level * th
        
        return threshold
    
    
    def target_detection(self, option:str = "CFAR"):
        """
        Generates a target detection list with indixes of the detected peaks.
        The detection is performed with the selected detection algorithm
        
        Parameters
        ----------
        option:
            - threshold : Target detection based on a single threshold
            - CFAR : Applies the CA-CFAR Algorithm
        Returns
        -------
            - dl : Target detection list 

        """
        
        rdm = self.RD_map[:self.n_sample//2, :]
        rdm = 10*np.log10(np.abs(rdm)**2)
        
        dl = []
        base = -200 # in dBfs
        
        if option == "CFAR":
            th_cfar = self.ca_cfar_2d(rdm,
                                      self.ca_cfar["guard_cells"],
                                      self.ca_cfar["training_cells"],
                                      self.ca_cfar["cfar_th"])
            
            rdm[rdm < th_cfar] = base
            
            neighborhood = np.ones((3,3))
            local_max = (rdm == maximum_filter(rdm, footprint=neighborhood))
            dl = np.argwhere(local_max)
        elif option == "threshold":
            rdm[rdm < self.t_th] = base
            local_max = (rdm == maximum_filter(rdm, footprint=neighborhood))
            dl = np.argwhere(local_max)
            
        return dl, rdm
    
    
    def plot_range_fft(self, disp: str = "default"):
        """ 
        Plots the 2D range fft
        
        disp:
            "default"   plots all range fft outputs
            "NCI"       plots the non-choherent-intigrated result off all range ffts
            "CFAR"      plots the constant false alarm rate decision line based on the nci range fft data
        """
        fig, ax = plt.subplots()

        N = min(self.n_sample//2, np.shape(self.r_fft)[0])
        
        fig.suptitle(" Range FFT ")
        ax.set_xlabel(" Number of Samples ")
        ax.set_ylabel("Amplitude in dBFS ")
        ax.grid(True)

        if disp == "CFAR":
            for i in range(N):
                r_fft = np.mean(10*np.log10(np.abs(self.r_fft)**2), axis=0)
                th_cfar = self.ca_cfar_1d(r_fft,
                                          self.ca_cfar["guard_cells"],
                                          self.ca_cfar["training_cells"],
                                          self.ca_cfar["cfar_th"])
                
                ax.plot(th_cfar, color="red")
            
            ax.plot(r_fft, color="blue")

        elif disp == "NCI":
            r_fft_nci = np.mean(10*np.log10(np.abs(self.r_fft)**2), axis=0)
            ax.plot(r_fft_nci)
            
        else:
            for i in range(N):
                ax.plot(10*np.log10(np.abs(self.r_fft[i])**2))
      
        return fig


    def plot_doppler_fft(self, disp: str = "default"):
        """ 
        Plots the 2D doppler fft 
        """
        fig, ax = plt.subplots()
        
        fig.suptitle(" Doppler FFT ")
        ax.set_xlabel(" Number of Ramps ")
        ax.set_ylabel("Amplitude in dBFS ")
        ax.grid(True)

        for i in range(self.n_ramps):
            ax.plot(10*np.log10(np.abs(self.RD_map[i])**2))
        
        return fig


    def plot_RD_map(self, rdm=None, disp: str="2D"):
        """
        Plot the Range–Doppler map.
        
        Parameters
        ----------
        disp : str
        Display mode for the plot. Options are:
            
            - "2D"    : Show the Range–Doppler map as a 2D heatmap.
            - "3D"    : Show the map as a 3D surface plot.
            - "CFAR"  : Display the CFAR detection map.
            - "PEAKS" : Show detected peaks in the Range–Doppler map.
        """
        if rdm is None:
            rdm = self.RD_map[:self.n_sample//2, :]
            rdm = 10*np.log10(np.abs(rdm)**2)

        doppler_axis = np.arange(-self.n_ramps//2 , self.n_ramps//2, 1) 
        range_axis = np.arange(0, self.n_sample//2 , 1) 
        
        if disp == "3D":
            fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
            X, Y = np.meshgrid(doppler_axis, range_axis) 
            surf = ax.plot_surface(X, Y, rdm, cmap='viridis')

        elif disp == "2D":
            fig = plt.figure()
            ax = fig.add_subplot(111)
            im = ax.imshow(rdm, extent=(doppler_axis.min(), doppler_axis.max(), range_axis.min(), range_axis.max()), origin='lower', cmap='viridis')
            fig.colorbar(im, shrink=0.4, aspect=25 ,pad=0.05 , label="Power in dB")
            
        elif disp == "CFAR":
            fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
            th_cfar = self.ca_cfar_2d(rdm,
                                      self.ca_cfar["guard_cells"],
                                      self.ca_cfar["training_cells"],
                                      self.ca_cfar["cfar_th"])
            X, Y = np.meshgrid(doppler_axis, range_axis) 
            surf = ax.plot_surface(X, Y, rdm, cmap='viridis', alpha=0.3)
            lim = self.ca_cfar["guard_cells"] + self.ca_cfar["training_cells"]
            surf = ax.plot_surface(X[lim:-lim, lim:-lim], Y[lim:-lim, lim:-lim], th_cfar[lim:-lim, lim:-lim], cmap='plasma', alpha=1)
        elif disp == "PEAKS":
            _ , rdm = self.target_detection(option = "CFAR")
            fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
            X, Y = np.meshgrid(doppler_axis, range_axis) 
            surf = ax.plot_surface(X, Y, rdm, cmap='viridis')
            
            
        ax.set_title(f"Range - Doppler Map; Frame")
        ax.set_xlabel("Doppler Bins")
        ax.set_ylabel("Range Bins")
        plt.show()