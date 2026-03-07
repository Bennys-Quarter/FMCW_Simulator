import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray 
from scipy.signal.windows import chebwin
from scipy.fft import fft, fftshift

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
            "cfar_th" : 3
        }
        
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

    
    def plot_range_fft(self, option: str = "default"):
        """ 
        Plot the range fft 
        
        :option:
            "default" plots all range fft outputs
            "cfar" plots the cfar output of the NCI range fft
        """
        plt.figure()

        N = min(self.n_sample//2, np.shape(self.r_fft)[0])
        
        plt.title(" Range FFT ")
        plt.xlabel(" Number of Samples ")
        plt.ylabel("Amplitude in dBFS ")

        if option == "cfar":
            for i in range(N):
                r_fft = np.mean(10*np.log10(np.abs(self.r_fft)**2), axis=0)
                cfar = self.ca_cfar_1d(r_fft,
                                          self.guard_cells,
                                          self.training_cells,
                                          self.cfar_th)
                
                plt.plot(cfar, color="red")
            
            plt.plot(r_fft, color="blue")

        elif option == "nci":
            r_fft_nci = np.mean(10*np.log10(np.abs(self.r_fft)**2), axis=0)
            plt.plot(r_fft_nci)
            plt.show()

        elif option == "targets":
            r_fft_nci = np.mean(10*np.log10(np.abs(self.r_fft)**2), axis=0)
            cfar = self.ca_cfar_1d(r_fft_nci)
            self.identify_targets(data=r_fft_nci, threshold=cfar)

            plt.plot(r_fft_nci)
            x = self.target_list["idx"]
            y = self.target_list["peak_power_dB"]
            plt.scatter(x,y, marker="x", color="red")
            
        else:
            for i in range(N):
                plt.plot(10*np.log10(np.abs(self.r_fft[i])**2))
      
            plt.show()


    def plot_doppler_fft(self):
        """ 
        Plot the doppler fft 
        """
        plt.figure()
        
        plt.title(" Doppler FFT ")
        plt.xlabel(" Number of Ramps ")
        plt.ylabel("Amplitude in dBFS ")

        for i in range(self.n_ramps):
            plt.plot(10*np.log10(np.abs(self.RD_map[i])**2))
        plt.show()



    def plot_RD_map(self, rdm=None, disp="2D"):
        """ 
        Plot the Range Doppler map 

        :disp: 
            option is either "2D" or "3D"
        """
        if rdm is None:
            rdm = self.RD_map[:self.n_sample//2, :]
            rdm = 10*np.log10(np.abs(rdm)**2)

        doppler_axis = np.arange(-self.n_ramps//2 , self.n_ramps//2, 1) 
        range_axis = np.arange(0, self.n_sample//2 , 1) 
        
        if disp == "3D" or disp == "cfar":
            fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
            X, Y = np.meshgrid(doppler_axis, range_axis//2) 
            surf = ax.plot_surface(X, Y, rdm, cmap='viridis')

        elif disp == "2D":
            fig = plt.figure()
            ax = fig.add_subplot(111)
            im = ax.imshow(rdm, extent=(doppler_axis.min(), doppler_axis.max(), range_axis.min(), range_axis.max()), origin='lower', cmap='viridis')
            fig.colorbar(im, shrink=0.4, aspect=25 ,pad=0.05 , label="Power in dB")

        ax.set_title(f"Range - Doppler Map; Frame")
        ax.set_xlabel("Doppler Bins")
        ax.set_ylabel("Range Bins")
        plt.show()