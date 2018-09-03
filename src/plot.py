#!/usr/bin/env python

import matplotlib.pyplot as plt
import data_reader
import sys

if __name__ == '__main__':
    data_reader.read_file(sys.argv[-1]).plot()
 
    plt.show()
