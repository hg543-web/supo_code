import numpy as np
import urllib.request

import scipy.io.wavfile
from IPython.display import Audio


# Read frequency and data array for sound track
fs, x = scipy.io.wavfile.read("Armstrong_Small_step.ogg") 

# If we have a stero track (left and right channels), take just the first channel
if len(x.shape) > 1:
    x = x[:, 0]


# Perform discrete Fourier transform (real signal)
xf = np.fft.rfft(x)

# Create copy of transformed signal
xf_filtered = xf.copy()

# Cut-off frequencies (Hz)
cutoff_freq_low = 1200
cutoff_freq_high = 1500

# Cut-off indices in transform array
n_cut_low = int(2*cutoff_freq_low*len(xf_filtered)/fs)
n_cut_high = int(2*cutoff_freq_high*len(xf_filtered)/fs)

# Remove low and high frequencies
xf_filtered[:n_cut_low] = 0.0
xf_filtered[n_cut_high:] = 0.0

# Perform inverse transform on filtered signal
x_filtered = np.fft.irfft(xf_filtered)


Audio(x_filtered, rate=fs)