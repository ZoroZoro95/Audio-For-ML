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

def compute_spectrum_amplitude(signal, sample_rate, normalization_factor=None):
    """
    returns one sided amplitude spectrum from 0 to sample_rate / 2.
    """
    N = len(signal)
    spectrum = np.fft.fft(signal)

    if normalization_factor is None:
        normalization_factor = N

    half = N // 2

    # Indices 0 through N/2, including Nyquist.
    frequencies = np.arange(half + 1) * sample_rate / N
    #0,0.333,0.666,.......8000Hz
    # Keep DC through Nyquist and normalize.
    amplitudes = np.abs(spectrum[:half + 1]) / normalization_factor

    # Double only the interior bins.
    amplitudes[1:-1] *= 2

    return frequencies, amplitudes

def find_dominant_frequencies(frequencies,amplitudes):
    """
    returns : (Dominant1 Hz , Amp1) and (Dominant2 Hz, Amp2)
    """
    #exclude dc
    largest = float('-inf')
    second_largest = float('-inf')
    largest_index = 0
    second_largest_index = 0
    for i,curr_amp in enumerate(amplitudes[1:],start= 1):
        if curr_amp > largest:
            second_largest = largest
            second_largest_index = largest_index
            largest = curr_amp
            largest_index = i
        elif curr_amp > second_largest:
            second_largest = curr_amp
            second_largest_index = i
    largest_freq = frequencies[largest_index]
    second_freq = frequencies[second_largest_index]
    return largest_freq, second_freq, largest_index, second_largest_index, largest, second_largest
