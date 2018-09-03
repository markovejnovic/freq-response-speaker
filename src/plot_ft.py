#!/usr/bin/env python

import matplotlib.pyplot as plt
from waveform import Waveform
import data_reader
import sys

if __name__ == '__main__':
    w = data_reader.read_file(sys.argv[-1])
    peaks = w.ft_peaks()

    fx, fy = w.abs_dft()
    plt.plot(fx, fy)
    for peak in peaks:
        plt.plot(fx[peak], fy[peak], marker='o', color='r')
    plt.show()
