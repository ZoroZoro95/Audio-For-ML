# Mini Audio Analyzer

A lightweight Python tool for generating, analyzing, and visualizing audio signals.

## Current Progress

The project currently supports synthetic audio signal generation, raw Fast Fourier Transform (FFT) spectrum computation, and basic waveform visualization.

### Features Implemented
*   **Synthetic Signal Generation (`audio_analyzer/signals.py`)**: 
    *   **Composite Signal**: Generates a 3-second synthetic audio signal at a 16,000 Hz sample rate with three distinct segments (200 Hz, 500 Hz, and combined).
    *   **Sine Wave Generation**: Utility to generate pure sine waves given frequency, sample rate, and length.
    *   **Windowing**: Applies window functions (e.g., Hann, Rectangular) to signals to mitigate spectral leakage.
*   **Spectrum Analysis (`audio_analyzer/spectrum.py`)**: 
    *   **Raw FFT**: Computes the raw FFT and corresponding frequency bins using `numpy.fft.fft` and `numpy.fft.fftfreq`.
    *   **Amplitude Spectrum**: Computes the one-sided amplitude spectrum, preserving energy from discarded negative frequencies. Includes support for custom normalization factors (e.g., for windowed signals).
    *   **Peak Detection**: Finds the top two dominant frequencies in the amplitude spectrum (excluding the DC component).
*   **Visualization (`audio_analyzer/plotting.py`)**: 
    *   **Waveform**: Plots the synthetic audio waveform (amplitude vs time).
    *   **Spectrum**: Plots the one-sided amplitude spectrum, zoomed in to highlight specific frequency ranges.
    *   **Spectral Leakage Comparison**: Visualizes the effect of different window functions on spectral leakage for frequencies that don't exactly fit into the FFT bins.

### Testing
*   The project uses `pytest` for unit testing.
*   **Signal Tests (`tests/test_signal.py`)**: Validates the time array bounds, overall array shapes, and the exact mathematical correctness of all three signal segments.
*   **Spectrum Tests (`tests/test_spectrum.py`)**: Verifies the shape and complex type of the FFT output, frequency bin spacing, zero-frequency bin, amplitude calibration, dominant frequency detection, and correct amplitude recovery when using a Hann window.

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
