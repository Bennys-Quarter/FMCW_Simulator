import unittest
import numpy as np


class TestFMCWRadar(unittest.TestCase):

    def setUp(self):
        from models.fmcw_radar import FMCWRadar
        from file_handler import FileHandler

        f_handler = FileHandler()
        chirp_param = f_handler.read_input()
        self.radar = FMCWRadar(chirp_param)

    def test_noise(self):
        N = 1e9
        T_n = 290  # Thermal nois in °Kelvin
        F_r = 10 ** (13 / 10)
        G = 10 ** (20 / 10)
        N_0 = self.f_s / 2 # Noise bandwidth

        noiseReal = self.radar.addaptive_noise(N)

        # Imaginary Noise
        #noiseImag = np.random.normal(0, np.sqrt(2)/2, Num_s)
        #noise = np.sqrt(N_a) * (noiseReal + 1j*noiseImag)

        N_i = T_n * F_r * self.k_b * N_0    # Input Noise
        N_a = (F_r - 1) * N_i * G           # Output Noise

        noise_power = np.mean(np.abs(noiseReal)**2)

        print(N_a)
        print('noise power = ' + str(10 * np.log10(noise_power)))  

        self.assertAlmostEqual(N_a, noise_power, delta=4)

if __name__ == "__main__":
    unittest.main()