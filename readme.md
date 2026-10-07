# Audio-For-ML

This repository contains Jupyter Notebooks focused on extracting basic audio features and understanding audio processing concepts for Machine Learning tasks. 

## 📖 Curriculum

The content is structured as a step-by-step lesson pattern to guide you from the basics of sound to advanced audio transformations and features. 

### Chapter 1: Basics and Waveforms
Understanding the fundamental building blocks of audio signals.
- [`1_Basics_and_Waveforms/sinosuids.ipynb`](1_Basics_and_Waveforms/sinosuids.ipynb)
- [`1_Basics_and_Waveforms/combining_sinosuids.ipynb`](1_Basics_and_Waveforms/combining_sinosuids.ipynb)
- *Related Wiki*: [Sinusoids and Superposition](wiki/Sinusoids-and-Superposition.md)

### Chapter 2: Fourier Transform Concepts
The core intuition and mathematical foundations behind mapping time to frequency.
- [`2_Fourier_Transform_Concepts/Matching_freq.ipynb`](2_Fourier_Transform_Concepts/Matching_freq.ipynb)
- [`2_Fourier_Transform_Concepts/Defining the Fourier Transform Using  Complex Numbers.ipynb`](2_Fourier_Transform_Concepts/Defining%20the%20Fourier%20Transform%20Using%20%20Complex%20Numbers.ipynb)
- [`2_Fourier_Transform_Concepts/FourierCoefficient_manual.ipynb`](2_Fourier_Transform_Concepts/FourierCoefficient_manual.ipynb)
- [`2_Fourier_Transform_Concepts/Manual_DFT.ipynb`](2_Fourier_Transform_Concepts/Manual_DFT.ipynb)
- [`2_Fourier_Transform_Concepts/fft_intuition.ipynb`](2_Fourier_Transform_Concepts/fft_intuition.ipynb)
- [`2_Fourier_Transform_Concepts/spectral_leakage.ipynb`](2_Fourier_Transform_Concepts/spectral_leakage.ipynb)
- *Related Wikis*: [Complex Numbers in Audio](wiki/Complex-Numbers-in-Audio.md), [Discrete Fourier Transform (DFT)](wiki/Discrete-Fourier-Transform-(DFT).md), [Spectral Leakage and Intuition](wiki/Spectral-Leakage-and-Intuition.md)

### Chapter 3: Advanced Transforms
Taking the Fourier transform further with efficient algorithms, time-varying signals, and compression.
- [`3_Advanced_Transforms/FFT_python.ipynb`](3_Advanced_Transforms/FFT_python.ipynb)
- [`3_Advanced_Transforms/Fourier Transform.ipynb`](3_Advanced_Transforms/Fourier%20Transform.ipynb)
- [`3_Advanced_Transforms/STFT_manual.ipynb`](3_Advanced_Transforms/STFT_manual.ipynb)
- [`3_Advanced_Transforms/DCT_Compression.ipynb`](3_Advanced_Transforms/DCT_Compression.ipynb)
- *Related Wikis*: [Fast Fourier Transform (FFT)](wiki/Fast-Fourier-Transform-(FFT).md), [Short-Time Fourier Transform (STFT)](wiki/Short-Time-Fourier-Transform-(STFT).md), [Discrete Cosine Transform (DCT)](wiki/Discrete-Cosine-Transform-(DCT).md), [Fourier Transform with Librosa](wiki/Fourier-Transform-with-Librosa.md)

### Chapter 4: Audio Features
Extracting meaningful attributes from audio in both the time and frequency domains (including spectrograms).
- **Time-Domain**: 
  - [`4_Audio_Features/AmpEnvelope.ipynb`](4_Audio_Features/AmpEnvelope.ipynb)
  - [`4_Audio_Features/RMSandZCR.ipynb`](4_Audio_Features/RMSandZCR.ipynb)
  - *Related Wiki*: [Time-Domain Features](wiki/Time-Domain-Features.md)
- **Frequency-Domain & Spectrograms**:
  - [`spectrograms/powervsmagnitude_spec.ipynb`](spectrograms/powervsmagnitude_spec.ipynb)
  - [`spectrograms/decibels.ipynb`](spectrograms/decibels.ipynb)
  - [`spectrograms/freq_to_mel.ipynb`](spectrograms/freq_to_mel.ipynb)
  - [`spectrograms/mel_spectrogram.ipynb`](spectrograms/mel_spectrogram.ipynb)
  - [`spectrograms/log_mel_spec.ipynb`](spectrograms/log_mel_spec.ipynb)
  - [`spectrograms/MFCC.ipynb`](spectrograms/MFCC.ipynb)
  - [`4_Audio_Features/Zero_padding_and_FFT_size.ipynb`](4_Audio_Features/Zero_padding_and_FFT_size.ipynb)
  - *Related Wikis*: [Decibels and Dynamic Range](wiki/Decibels-and-Dynamic-Range.md), [Zero-Padding and FFT Size](wiki/Zero-Padding-and-FFT-Size.md)

### Chapter 5: General Theory and Observations
Miscellaneous foundational concepts that govern digital signal processing.
- [`5_General_theory_and_observations/window_length_vs_hop_length.ipynb`](5_General_theory_and_observations/window_length_vs_hop_length.ipynb)
- [`5_General_theory_and_observations/Aliasing.ipynb`](5_General_theory_and_observations/Aliasing.ipynb)
- *Related Wikis*: [Window Length vs Hop Length](wiki/Window-Length-vs-Hop-Length.md), [Aliasing](wiki/Aliasing.md)

---

## 📚 Documentation & Wiki

For detailed theoretical explanations, mathematical definitions, and intuitive breakdowns of the code found in these notebooks, please refer to the project's [Wiki](wiki/Home.md). 

## 🎛️ Projects

- **[Mini Audio Analyzer](Mini%20Audio%20Analyzer/)**: A small audio analysis setup/project.

## 🚀 Usage

1. Place your target audio files (e.g., `.wav`) in the `AudioFiles/` directory.
2. Ensure you have the necessary dependencies installed (typically `librosa`, `numpy`, `scipy`, and `matplotlib`).
3. Open the Jupyter Notebooks locally to experiment with the feature extraction algorithms in action.
