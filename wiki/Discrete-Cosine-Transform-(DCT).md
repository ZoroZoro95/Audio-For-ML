# Discrete Cosine Transform (DCT)

This page explains the **Discrete Cosine Transform (DCT)** and its applications in data compression and audio feature extraction.

*(Based on `DCT_Compression.ipynb`)*

## 1. What is the DCT?
Similar to the Fourier Transform, the DCT expresses a sequence of data points in terms of a sum of cosine functions oscillating at different frequencies. However, unlike the DFT which uses complex numbers (sines and cosines), the DCT uses **only real-valued cosine functions**.

The DCT of a 1D sequence $x[n]$ of length $N$ is typically defined as:
$$ C[k] = \sum_{n=0}^{N-1} x[n] \cos \left[ \frac{\pi}{N} \left( n + \frac{1}{2} \right) k \right] $$
where $k$ ranges from $0$ to $N-1$.

- $C[0]$ represents the average-like component (DC).
- $C[1]$ represents a slow variation.
- Higher values of $k$ represent faster oscillations.

## 2. Energy Compaction and Compression
One of the most important properties of the DCT is **energy compaction**. For most naturally occurring signals (like audio or images), the DCT tends to concentrate most of the signal's energy (information) into the first few low-frequency coefficients. 

Because the higher-frequency DCT coefficients often contain very little energy (approaching zero), they can be discarded without significantly degrading the reconstructed signal.

### Code Example: Signal Compression
We can use `scipy.fft.dct` to compute the DCT and `scipy.fft.idct` for reconstruction. Using `norm="ortho"` applies an orthonormal scaling, making the transform cleaner and mathematically easier to invert.

```python
import numpy as np
from scipy.fft import dct, idct

# A smooth/gradual signal
signal = np.array([1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7])

# 1. Compute the DCT
coefficients = dct(signal, type=2, norm="ortho")
print("DCT Coefficients:", coefficients)
# Output shows large values in the first few coefficients, near zero later

# 2. Compress by discarding high frequencies
compressed = coefficients.copy()
compressed[3:] = 0  # Zero out coefficients from index 3 onwards

# 3. Reconstruct the signal
reconstructed = idct(compressed, type=2, norm="ortho")
print("Reconstructed:", reconstructed)
```

Even after discarding more than half of the coefficients, the reconstructed signal closely matches the original. This is the fundamental mechanism behind audio formats like MP3 and image formats like JPEG.
