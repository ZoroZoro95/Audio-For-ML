from audio_analyzer.signals import generate_synthetic_signal
from audio_analyzer.plotting import plot_waveform,plot_spectrum
from audio_analyzer.spectrum import compute_spectrum,find_dominant_frequencies
from audio_analyzer.spectrum import compute_spectrum_amplitude

def main():
    sample_rate = 16000
    duration = 3.0

    time,signal = generate_synthetic_signal(sample_rate,duration)
    print(f"Sample rate: {sample_rate} Hz")
    print(f"Duration: {duration} seconds")
    print(f"Number of samples: {signal.size}")
    print(f"Time shape: {time.shape}")
    print(f"Signal shape: {signal.shape}")
    print(f"First time value: {time[0]}")
    print(f"Last time value: {time[-1]}")

    frequencies,spectrum = compute_spectrum(signal,sample_rate)
    print(f"Frequencies shape: {frequencies.shape}")
    print(f"Spectrum shape: {spectrum.shape}")
    print(f"First frequency value: {frequencies[0]}")
    print(f"Last frequency value: {frequencies[-1]}")
    print(f"First spectrum value: {spectrum[0]}")
    print(f"Last spectrum value: {spectrum[-1]}")
    #bin spacing
    bin_spacing = frequencies[1] - frequencies[0]
    print(f"Bin spacing: {bin_spacing}")

    frequencies,amplitudes = compute_spectrum_amplitude(signal,sample_rate)
    print(f"Amplitudes shape: {amplitudes.shape}")
    print(f"First frequency value: {frequencies[0]}")
    print(f"Last frequency value: {frequencies[-1]}")

    #plot waveform
    plot_waveform(time,signal)

    #plot spectrum Freq vs Amp
    plot_spectrum(frequencies,amplitudes)

    dominant_freq, second_dominant_freq, largest_index, second_largest_index, dom_amp, second_amp = find_dominant_frequencies(frequencies,amplitudes)

    print(f"Dominant frequency: {dominant_freq} Hz with amplitude {dom_amp}")
    print(f"Second dominant frequency: {second_dominant_freq} Hz with amplitude {second_amp}")

if __name__ == "__main__":
    main()