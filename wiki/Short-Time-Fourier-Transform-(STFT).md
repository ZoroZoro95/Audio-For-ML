# Short-Time Fourier Transform (STFT)

This page explains the **Short-Time Fourier Transform (STFT)**, which provides a way to analyze how the frequency content of a signal changes over time.

*(Based on `STFT_manual.ipynb`)*

## 1. The Problem with the Standard FFT
While the standard Fast Fourier Transform (FFT) shows us all the frequencies present in a signal, it loses all information about **when** those frequencies occurred. For dynamic audio signals (like speech or music), frequency content changes rapidly over time.

## 2. How STFT Works
The STFT addresses this by slicing the signal into short, overlapping segments (called frames) and computing the FFT for each segment.

Mathematically, the discrete STFT is expressed as:
$$ \text{STFT}\{x[n]\}(m, \omega) = \sum_{n=-\infty}^{\infty} x[n] \cdot w[n - mR] \cdot e^{-i \omega n} $$
Where:
- $x[n]$ is the original signal.
- $w[n]$ is the window function (e.g., Hanning window) of length $M$.
- $m$ is the frame index.
- $R$ is the hop length (number of samples between consecutive frames).
- $\omega$ is the frequency bin.

### Key Concepts:
1. **Frame Length / Windowing**: A mathematical window (like `np.hanning`) is applied to each frame to reduce spectral leakage at the edges.
2. **Hop Length**: The window slides forward by a set number of samples ($R$). A smaller hop length creates more overlap and higher time resolution.
3. **Spectrogram**: The resulting sequence of FFT magnitudes is stacked side-by-side to create a 2D matrix (Time vs. Frequency).

## 3. Calculating the STFT Manually
We can implement this by manually sliding a window across our signal in Python.

```python
import numpy as np
import matplotlib.pyplot as plt

frame_length = 256
hop_length = 128
window = np.hanning(frame_length)

frames = [] # stores the amplitude spectrum for each frame

# Slide the window across the signal
for start in range(0, len(signal) - frame_length + 1, hop_length):
    frame = signal[start : start + frame_length]
    windowed_frame = frame * window
    
    # Compute the real FFT for the windowed frame
    windowed_fft = np.fft.rfft(windowed_frame)
    frames.append(np.abs(windowed_fft))

# shape: frames_magnitude × frequency_bins -> transpose to frequency_bins × frames
stft = np.array(frames).T 

# Calculate the actual time values for the center of each frame
frame_times = np.arange(stft.shape[1]) * hop_length / sample_rate + (frame_length / 2 / sample_rate)
frequencies = np.fft.rfftfreq(frame_length, d=1/sample_rate)

# Plotting the Spectrogram
plt.figure(figsize=(10,6))
plt.pcolormesh(frame_times, frequencies, stft, shading='gouraud', cmap='magma')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.colorbar(label='Magnitude')
plt.show()
```

## 4. Time-Frequency Resolution Trade-off
The STFT is governed by the Heisenberg uncertainty principle for signal processing. You cannot have perfect resolution in both time and frequency simultaneously:
- **Longer frames (e.g., 2048 samples)** provide excellent **frequency resolution** (narrow frequency bins) but poor **time resolution** (smearing rapid events).
- **Shorter frames (e.g., 256 samples)** provide excellent **time resolution** (pinpointing exactly when a sound occurs) but poor **frequency resolution** (wide frequency bands).
