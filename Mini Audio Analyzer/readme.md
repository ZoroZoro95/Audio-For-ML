# Mini Audio Analyzer

A lightweight Python tool for generating, analyzing, and visualizing audio signals.

## Current Progress

The project currently supports synthetic audio signal generation, raw Fast Fourier Transform (FFT) spectrum computation, and basic waveform visualization.

### Features Implemented
*   **Synthetic Signal Generation (`audio_analyzer/signals.py`)**: 
    *   Generates a 3-second synthetic audio signal at a 16,000 Hz sample rate.
    *   The generated signal consists of three distinct 1-second segments:
        *   `0-1s`: A 200 Hz sine wave.
        *   `1-2s`: A 500 Hz sine wave.
        *   `2-3s`: A combined 200 Hz and 500 Hz sine wave.
*   **Spectrum Analysis (`audio_analyzer/spectrum.py`)**: 
    *   **Raw FFT**: Computes the raw FFT of the audio signal using `numpy.fft.fft`.
    *   Calculates the corresponding frequency bins using `numpy.fft.fftfreq` (achieving a ~0.3333 Hz bin spacing for the 3-second signal).
    *. **Amplitude Spectrum (`compute_spectrum_amplitude`)**: Computes the one-sided amplitude spectrum.
        *   *Why this is important*: Raw FFT output contains complex numbers and includes negative frequencies. The amplitude spectrum provides the physical magnitude of the frequencies from 0 to the Nyquist frequency (half the sample rate).
        *   *How it works*: It discards negative frequencies, scales the magnitude by the number of samples (`N`), and doubles the interior bins to account for the energy of the discarded negative frequencies, ensuring energy is preserved. DC (0 Hz) and Nyquist bins are not doubled.
*   **Visualization (`audio_analyzer/plotting.py`)**: 
    *   **Waveform (`plot_waveform`)**: Plots the synthetic audio waveform (amplitude vs time) using `matplotlib`.
    *   **Spectrum (`plot_spectrum`)**: Plots the one-sided amplitude spectrum (amplitude vs frequency). The plot is zoomed in to the 0-1000 Hz range to clearly visualize the 200 Hz and 500 Hz components of the synthetic signal.

### Testing
*   The project uses `pytest` for unit testing.
*   **Signal Tests (`tests/test_signal.py`)**: Validates the time array bounds, overall array shapes, and the exact mathematical correctness of all three signal segments.
*   **Spectrum Tests (`tests/test_spectrum.py`)**: Verifies the shape and complex type of the FFT output, the frequency bin spacing, and the zero-frequency bin.

## How to Run

1.  **Install Requirements:**
    Ensure you have an active virtual environment and run:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run the Main Script:**
    The `main.py` script serves as a demonstration. It generates the synthetic signal, prints out stats about the time and frequency domains, and plots the waveform.
    ```bash
    python main.py
    ```
3.  **Run Tests:**
    Run the test suite using pytest:
    ```bash
    pytest tests/ -v
    ```

## Next Steps
*   Implement Short-Time Fourier Transform (STFT) in `audio_analyzer/stft.py` and its corresponding tests in `tests/test_stft.py`.
