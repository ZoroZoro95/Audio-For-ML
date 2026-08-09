# Fast Fourier Transform (FFT)

This page explains how to efficiently calculate the Fourier Transform using Python's NumPy library and how to interpret the resulting spectrum.

*(Based on `FFT_python.ipynb` and `Fourier Transform.ipynb`)*

## 1. What is the FFT?
The **Fast Fourier Transform (FFT)** is an optimized algorithmic implementation of the Discrete Fourier Transform (DFT). While the standard DFT formula requires $O(N^2)$ operations, the FFT reduces this to $O(N \log N)$ operations. This massive speedup makes it possible to process audio in real-time.

## 2. Using `np.fft.fft`
The `np.fft.fft` function computes the complete (two-sided) Fourier spectrum.

```python
import numpy as np

# Calculate the spectrum
spectrum = np.fft.fft(signal)

# Extract frequency bins
frequencies = np.fft.fftfreq(N, d=1/sample_rate)

# Calculate raw magnitude
magnitude = np.abs(spectrum)
```

### Two-Sided vs. One-Sided Spectrum
When applying the FFT to real-valued signals (like standard audio), the resulting spectrum is symmetrical. The negative frequencies are simply a mirrored version of the positive frequencies.
Because of this redundancy, we usually discard the negative half and only plot frequencies from $0$ Hz up to the **Nyquist frequency** (which is exactly half of the sample rate, $f_s / 2$).

## 3. Using `np.fft.rfft` for Audio
NumPy provides a dedicated function for real-valued inputs called `rfft` (Real Fast Fourier Transform). It automatically computes only the positive (one-sided) frequencies, saving memory and computation time.

### Code Example: Proper Scaling
The raw magnitudes outputted by the FFT scale with the number of samples ($N$). To get the *true* amplitude of the original sinusoids, we must mathematically scale the result. For a one-sided spectrum, the actual amplitude is calculated as:
$$ \text{Amplitude} \approx 2 \times \frac{|X[k]|}{N} $$

Here is how to compute a fully scaled, one-sided amplitude spectrum:

```python
import numpy as np
import matplotlib.pyplot as plt

# 1. Compute one-sided FFT
spectrum = np.fft.rfft(signal)

# 2. Get corresponding frequencies
frequencies = np.fft.rfftfreq(N, d=1/sample_rate)

# 3. Calculate raw magnitude and divide by N
amplitude_spectrum = np.abs(spectrum) / N

# 4. Multiply by 2 to account for the discarded negative frequencies 
# (excluding the DC offset bin at index 0 and Nyquist bin at index -1)
amplitude_spectrum[1:-1] *= 2 

# Plot the result
plt.stem(frequencies, amplitude_spectrum)
plt.xlabel("Frequency in Hz")
plt.ylabel("True Amplitude")
plt.show()
```

## 4. Interpreting the Data
When working with FFT outputs, you'll encounter several interconnected arrays:

- **`signal[n]`**: The amplitude of the audio waveform at sample index `n`.
- **`spectrum[k]`**: The complex Fourier coefficient for frequency bin `k`.
- **`frequencies[k]`**: The actual frequency (in Hz) represented by bin `k`.
- **`np.abs(spectrum[k])`**: The magnitude of the complex coefficient at bin `k`.
- **`np.angle(spectrum[k])`**: The phase angle of the coefficient at bin `k`.
