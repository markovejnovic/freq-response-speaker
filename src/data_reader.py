import csv
import numpy as np
from waveform import Waveform

def read_file(f):
    x = []
    y = []
    with open(f, 'r') as csvfile:
        r = csv.reader(csvfile, delimiter='\t')
        for row in r:
            x.append(float(row[0]))
            y.append(float(row[1]))

    return Waveform(x, y, 442 / 0.01, 0.5, 0.001, f)
