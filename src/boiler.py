#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import os
from waveform import Waveform
import data_reader

if __name__ == '__main__':
    waveforms = []
    xs = []
    ys = []

    for trial in ['Trial_6']:
        datafiles = sorted(os.listdir(os.path.join(sys.argv[-1], trial)), 
                key=lambda item: (int(item.partition(' ')[0]) 
                    if item[0].isdigit() else float('inf'), item))
        print(datafiles)
        for datum in datafiles:
            w = data_reader.read_file(os.path.join(sys.argv[-1], trial, datum))
            waveforms.append(w)

    for w in waveforms:
        x, y = w.abs_dft()
        peaks = w.ft_peaks()
        xs.append(x[peaks[0]])
        ys.append(y[peaks[0]])
        #plt.plot(x, y)
        #plt.plot(x[peaks[0]], y[peaks[0]], marker='o', color='r')
        #plt.show()

    sorted_x = sorted(xs)
    sorted_y = [x for _,x in sorted(zip(ys, xs))]

    plt.plot(sorted_x, sorted_y)
    plt.show()
