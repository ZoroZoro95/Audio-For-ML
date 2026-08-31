"""Functions for visualizing audio signals."""

import matplotlib.pyplot as plt


def plot_waveform(time,signal):
    """Plot signal amplitude against time for the full recording."""
    plt.figure(figsize=(12,8))
    plt.plot(time,signal)

    plt.title("Synthetic Audio Waveform")
    plt.xlabel("Time [seconds]")
    plt.ylabel("Amplitude")
    plt.grid(True)

    # Hundreds of cycles are compressed into the full-duration view, so the
    # waveform appears as dense bands rather than individually visible cycles.
    plt.tight_layout()  # Prevent titles and axis labels from being clipped.
    plt.show()

def plot_spectrum(frequencies,amplitudes):
    #frequency spacing = sample_rate / number of samples = 16000/48000 = 1/3 = 0.33HZ
    #frequency bins = 0,0.333,0.666,1.000..........................................8000HZ

    plt.figure(figsize = (12,5))
    plt.plot(frequencies,amplitudes)
    plt.title("One sided Amplitude Spectrum")
    #plotting only first 1000Hz
    plt.xlim(0,1000) #from 0 to 1000 Hz
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_spectral_leakage_comparison(freq1,ampl1,freq2,ampl2):
    plt.figure(figsize = (12,5))
    plt.subplot(1,2,1)
    plt.stem(freq1,ampl1)
    plt.title("1000Hz")
    plt.xlim(500,1500)
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()

    plt.subplot(1,2,2)
    plt.stem(freq2,ampl2)
    plt.title("1007Hz")
    plt.xlim(500,1500)
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
