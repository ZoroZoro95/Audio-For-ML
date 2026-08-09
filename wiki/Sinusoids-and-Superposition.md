# Sinusoids and Superposition

This page explains the fundamental building blocks of all audio signals: **Sinusoids** (pure tones) and how they can be **superimposed** (combined) to form any complex wave.

*(Based on `sinosuids.ipynb` and `combining_sinosuids.ipynb`)*

## 1. Pure Tones (Sinusoids)
A pure tone is a sound with a single, specific frequency. Mathematically, it is represented as a sine or cosine wave.

A sinusoid is defined by three parameters:
1. **Frequency ($f$):** How many cycles occur per second (measured in Hertz, Hz). Determines pitch.
2. **Amplitude ($A$):** The maximum height of the wave. Determines loudness.
3. **Phase ($\phi$):** The starting position of the wave (measured in radians).

### Mathematical Formula
$$ y(t) = A \sin(2\pi f t + \phi) $$

### Code Example
Creating a 5 Hz sine wave in Python:
```python
import numpy as np
import matplotlib.pyplot as plt

sample_rate = 1000
duration = 1.0
t = np.arange(sample_rate * duration) / sample_rate

# A 5 Hz wave with amplitude 1.0 and 0 phase
frequency = 5
wave = np.sin(2 * np.pi * frequency * t)
```

## 2. Superposition (Combining Signals)
According to Fourier's theorem, **any complex signal can be represented as a sum of simple sinusoids** of varying frequencies, amplitudes, and phases. 

When you play multiple notes at the same time (like a chord on a piano), their sound waves simply add up together. This is called **superposition**.

### Superimposing Waves in Python
If we take three distinct sine waves:
- $x_1(t) = 1.0 \cdot \sin(2\pi \cdot 5 \cdot t)$ (5 Hz, amplitude 1.0)
- $x_2(t) = 0.6 \cdot \sin(2\pi \cdot 12 \cdot t)$ (12 Hz, amplitude 0.6)
- $x_3(t) = 0.3 \cdot \sin(2\pi \cdot 25 \cdot t)$ (25 Hz, amplitude 0.3)

We can combine them by simple addition:
```python
x1 = np.sin(2 * np.pi * 5 * t)
x2 = 0.6 * np.sin(2 * np.pi * 12 * t)
x3 = 0.3 * np.sin(2 * np.pi * 25 * t)

combined_signal = x1 + x2 + x3
```

### The Reverse Process: The Fourier Transform
While superposition adds simple waves to create a complex wave, the **Fourier Transform** does the exact opposite: it takes a complex, combined signal and *deconstructs* it back into its original simple sine wave components ($x_1, x_2, x_3$). 

By analyzing the resulting array of frequencies and amplitudes, we move from the **time domain** to the **frequency domain**.
