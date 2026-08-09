# Audio-For-ML

This repository contains Jupyter Notebooks focused on extracting basic audio features and understanding audio processing concepts for Machine Learning tasks.

## 📚 Documentation & Wiki

For detailed theoretical explanations, mathematical definitions, and intuitive breakdowns of the code found in these notebooks, please refer to the project's [Wiki](wiki/Home.md).

The documentation is organized into the following core topics:

- **[Time-Domain Features](wiki/Time-Domain-Features.md)**: Details on Amplitude Envelope, Root Mean Square (RMS) energy, and Zero-Crossing Rate (ZCR).
- **[Sinusoids and Superposition](wiki/Sinusoids-and-Superposition.md)**: Understanding pure tones and how they combine to form complex signals.
- **[Complex Numbers in Audio](wiki/Complex-Numbers-in-Audio.md)**: Exploring Euler's Formula and how complex test waves are used to measure frequency correlation.
- **[Discrete Fourier Transform (DFT)](wiki/Discrete-Fourier-Transform-(DFT).md)**: The mathematical definition of DFT and a manual Python implementation.
- **[Fast Fourier Transform (FFT)](wiki/Fast-Fourier-Transform-(FFT).md)**: Practical application using NumPy, extracting frequency bins, and proper magnitude scaling.
- **[Spectral Leakage and Intuition](wiki/Spectral-Leakage-and-Intuition.md)**: The conceptual intuition behind Fourier Transforms and how to handle spectral leakage.

## 🚀 Usage

1. Place your target audio files (e.g., `.wav`) in the `AudioFiles/` directory.
2. Ensure you have the necessary dependencies installed (typically `librosa`, `numpy`, `scipy`, and `matplotlib`).
3. Open the Jupyter Notebooks locally to experiment with the feature extraction algorithms in action.
