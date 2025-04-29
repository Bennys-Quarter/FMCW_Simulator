import yaml
import re

from models.fmcw_radar import FMCWRadar
from file_handler import FileHandler


if __name__ == '__main__':
    # Step 1: Load input parameters
    f_handler = FileHandler()
    chirp_param = f_handler.read_input()

    radar = FMCWRadar(chirp_param)
    radar.plot_transmit_chirp()
