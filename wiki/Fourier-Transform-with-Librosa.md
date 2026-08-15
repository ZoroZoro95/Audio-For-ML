# Fourier Transform with Librosa

This page covers the practical application of Fourier Transforms using the widely-used Python audio library, **Librosa**.

*(Based on `Fourier Transform.ipynb`)*

## 1. Why Librosa?
While manual Python implementations of the DFT and FFT (using raw `numpy`) are excellent for building intuition, real-world machine learning tasks require optimized and battle-tested libraries. `librosa` provides robust tools for audio loading, manipulation, and frequency analysis.

## 2. Computing the STFT
Instead of manually windowing and iterating over a signal, we can use `librosa.stft`. The mathematics remain the same:
$$ X(m, \omega) = \sum_{n=-\infty}^{\infty} x[n] \cdot w[n - mR] \cdot e^{-i \omega n} $$
Where $R$ is the hop length and $w$ is the window function.

### Code Example:
```python
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# 1. Load Audio
# sr=None preserves the original sample rate
signal, sample_rate = librosa.load("audio_file.wav", sr=None)

# 2. Define Parameters
n_fft = 2048      # Frame length (window size)
hop_length = 512  # Amount of samples to shift each frame

# 3. Compute STFT
# Returns a complex matrix of shape (1 + n_fft/2, n_frames)
stft_complex = librosa.stft(signal, n_fft=n_fft, hop_length=hop_length)

# 4. Extract Magnitude and Phase
magnitude = np.abs(stft_complex)
phase = np.angle(stft_complex)
```

## 3. Decibel (dB) Scaling
Human perception of loudness is logarithmic, not linear. A spectrogram plotted with raw magnitude values will often look mostly black because a few loud frequencies dwarf everything else. We convert magnitude to a decibel (dB) scale:
$$ L_{dB} = 20 \log_{10} \left( \frac{A}{A_{\text{ref}}} \right) $$

In `librosa`, this is done via `librosa.amplitude_to_db`:
```python
# Convert magnitude to Decibels
spectrogram_db = librosa.amplitude_to_db(magnitude, ref=np.max)
```

## 4. Visualizing the Spectrogram
We can quickly plot the resulting spectrogram using `librosa.display.specshow`, which automatically handles time and frequency axis scaling.

```python
plt.figure(figsize=(10, 6))
librosa.display.specshow(
    spectrogram_db, 
    sr=sample_rate, 
    hop_length=hop_length, 
    x_axis='time', 
    y_axis='hz', 
    cmap='magma'
)
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram (dB)')
plt.show()
```

### Mel Spectrograms
Often, instead of a linear frequency axis (`hz`), we use a Mel scale which more closely mimics how the human ear perceives pitch differences (more sensitive to low frequencies). `librosa.feature.melspectrogram` combines the STFT and Mel-filterbank application into a single step.
