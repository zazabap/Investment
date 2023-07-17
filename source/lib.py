# Date: 2023-07-17 
# Author: Shiwen An 
# Purpose: Write a library full of function
import numpy as np
from scipy.signal import fftconvolve
from scipy.signal import hilbert


# Add Super Smoother Filter by John
def super_smoother_filter(data, alpha):
    n = len(data)
    smoothed = np.zeros(n)
    for i in range(2, n):
        smoothed[i] = (data[i] + 2 * data[i-1] + data[i-2]) * alpha**2 + 2 * (1 - alpha) * smoothed[i-1] - (1 - alpha)**2 * smoothed[i-2]
    return smoothed

# Add MESA Maximum Entropy Spectrum Analysis
def mesa(data, period):
    n = len(data)
    weights = np.zeros(n)
    weights[0] = 1.0
    for i in range(1, n):
        weights[i] = weights[i-1] * (1.0 - 1.0/period)
    mesa_signal = fftconvolve(data, weights, mode='same')
    return mesa_signal



