from audio_analyzer.signals import generate_synthetic_signal,generate_sine_wave,apply_window
from audio_analyzer.plotting import plot_waveform,plot_spectrum,plot_spectral_leakage_comparison
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

    #spectral leakage testing
    signal_1 = generate_sine_wave(1000,16000,1024)
    signal_2 = generate_sine_wave(1007,16000,1024)

    freq1,ampl1 = compute_spectrum_amplitude(signal_1,16000)
    freq2,ampl2 = compute_spectrum_amplitude(signal_2,16000)

    #compare plots for 1000Hz vs 1007Hz
    plot_spectral_leakage_comparison(
        freq1, ampl1, freq2, ampl2, "Rectangular"
    )

    windowed_signal_1, hann_window = apply_window(signal_1,'hann')
    windowed_signal_2, _ = apply_window(signal_2,'hann')

    hann_normalization = hann_window.sum()
    windowed_freq1,windowed_ampl1 = compute_spectrum_amplitude(
        windowed_signal_1, 16000, hann_normalization
    )
    windowed_freq2,windowed_ampl2 = compute_spectrum_amplitude(
        windowed_signal_2, 16000, hann_normalization
    )

    #compare plots for 1000Hz vs 1007Hz
    plot_spectral_leakage_comparison(
        windowed_freq1,
        windowed_ampl1,
        windowed_freq2,
        windowed_ampl2,
        "Hann",
    )

    

if __name__ == "__main__":
    main()
