# Audio-For-ML

This repository contains Jupyter Notebooks focused on extracting basic audio features for Machine Learning tasks. 

## Contents

- **`AmpEnvelope.ipynb`**: Explores the extraction of the Amplitude Envelope from audio signals. The Amplitude Envelope gives a rough idea of the loudness of the signal and is useful for tasks like onset detection.
- **`RMSandZCR.ipynb`**: Covers the extraction of Root Mean Square (RMS) energy and Zero-Crossing Rate (ZCR). RMS is an indicator of the perceived loudness, and ZCR helps in identifying the percussive or noisy nature of a sound, often used in speech/music discrimination.
- **`Fourier Transform.ipynb`**: Introduces the Fourier Transform for converting an audio waveform from the time domain into the frequency domain. This helps identify which frequencies are present in a sound and how strong they are.
- **`AudioFiles/`**: Directory meant to store audio samples used by the notebooks.

## Usage

1. Place your audio files (e.g., `.wav`) in the `AudioFiles/` directory.
2. Open the Jupyter Notebooks to see the feature extraction in action.
3. Ensure you have the necessary dependencies installed (typically `librosa`, `numpy`, `matplotlib`).

## Features Covered
- **Amplitude Envelope (AE)**: Maximum amplitude value within a given frame.
- **Root Mean Square (RMS) Energy**: The root mean square of the amplitude within a frame.
- **Zero-Crossing Rate (ZCR)**: The rate at which the signal changes sign (goes from positive to negative or vice-versa).
- **Fourier Transform (FT)**: A mathematical transform that decomposes a time-domain audio signal into its frequency components.
- **Magnitude Spectrum**: Shows the strength of each frequency component after applying the Fourier Transform.

## Fourier Transform in Audio

Audio waveforms are recorded as amplitude values changing over time. This time-domain view is useful for seeing the shape of the signal, but it does not directly show the pitch or frequency content. The Fourier Transform converts the signal into the frequency domain, where the x-axis represents frequency and the y-axis usually represents magnitude.

For audio feature extraction, the Fourier Transform is useful because it helps reveal:

- Dominant frequencies in a sound.
- Harmonic structure of musical notes.
- Differences between low-frequency and high-frequency content.
- Spectral patterns that can be used for classification tasks.

In practice, audio analysis often uses the Fast Fourier Transform (FFT), which is an efficient algorithm for computing the Discrete Fourier Transform (DFT). For longer audio signals, the transform is usually applied frame by frame so frequency changes over time can be analyzed.
