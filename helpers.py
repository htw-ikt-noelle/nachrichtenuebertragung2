import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

def gen_time_axis(sr=1000, T=1.0):
    t = np.arange(0, T, 1/sr)
    return t