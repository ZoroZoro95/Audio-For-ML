"""
Next milestone: raw FFT and frequency bins in spectrum.py.
Implement a function that:
Accepts signal and sample_rate.
Computes np.fft.fft(signal).
Computes matching frequencies using np.fft.fftfreq.
Returns frequencies, fft_values.
Expected:
frequencies.shape = (48000,)
fft_values.shape  = (48000,)
bin spacing       = 16000 / 48000 = 0.3333 Hz
fft_values dtype  = complex
"""
import numpy as np

def compute_spectrum(signal,sample_rate):
    """the FFT of a signal"""
    N = len(signal) #48000
    spectrum = np.fft.fft(signal) # FFT Values
    frequencies = np.fft.fftfreq(N, d= 1/sample_rate) #Freq Bins

    return frequencies,spectrum
