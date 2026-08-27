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

In spectrum.py, write a function that:
- Accepts signal and sample_rate.
- Keeps FFT bins 0 through N/2.
- Produces 24001 frequencies from 0 to 8000 Hz.
- Calculates amplitude as abs(FFT) / N.
- Doubles interior bins.
- Does not double DC or Nyquist.
- Returns frequencies and amplitudes.
"""
import numpy as np

def compute_spectrum(signal,sample_rate):
    """the FFT of a signal"""
    N = len(signal) #48000
    spectrum = np.fft.fft(signal) # FFT Values
    frequencies = np.fft.fftfreq(N, d= 1/sample_rate) #Freq Bins

    return frequencies,spectrum

def compute_spectrum_amplitude(signal, sample_rate):
    N = len(signal)
    spectrum = np.fft.fft(signal)

    half = N // 2

    # Indices 0 through N/2, including Nyquist.
    frequencies = np.arange(half + 1) * sample_rate / N

    # Keep DC through Nyquist and normalize.
    amplitudes = np.abs(spectrum[:half + 1]) / N

    # Double only the interior bins.
    amplitudes[1:-1] *= 2

    return frequencies, amplitudes
