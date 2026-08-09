# Audio Processing for Machine Learning - Wiki

Welcome to the Audio-For-ML wiki! This wiki contains detailed theoretical and code-based explanations for extracting basic audio features and understanding the Fourier Transform in audio processing. The code logic found in these pages is directly derived from the companion Jupyter Notebooks.

## Table of Contents

- **[Time-Domain Features](Time-Domain-Features.md)**
  - Amplitude Envelope
  - Root Mean Square (RMS) energy
  - Zero-Crossing Rate (ZCR)
  
- **[Sinusoids and Superposition](Sinusoids-and-Superposition.md)**
  - Pure tones (frequency, amplitude, phase)
  - Superimposing pure tones to form complex signals

- **[Complex Numbers in Audio](Complex-Numbers-in-Audio.md)**
  - Euler's Formula
  - Complex test waves
  - Correlation via Center of Gravity

- **[Discrete Fourier Transform (DFT)](Discrete-Fourier-Transform-(DFT).md)**
  - Mathematical definition of DFT
  - Matching frequencies
  - Calculating manual Fourier coefficients

- **[Fast Fourier Transform (FFT)](Fast-Fourier-Transform-(FFT).md)**
  - Calculating FFT with Python (`np.fft.fft` and `np.fft.rfft`)
  - One-sided vs Two-sided spectrum
  - Magnitude scaling and extracting frequency bins

- **[Spectral Leakage and Intuition](Spectral-Leakage-and-Intuition.md)**
  - Intuitive understanding of Fourier Transforms
  - The problem of spectral leakage
