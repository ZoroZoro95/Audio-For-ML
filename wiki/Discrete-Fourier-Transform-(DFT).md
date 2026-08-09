# Discrete Fourier Transform (DFT)

This page breaks down the mathematical definition of the **Discrete Fourier Transform (DFT)** and demonstrates how to manually calculate Fourier coefficients using Python.

*(Based on `Manual_DFT.ipynb`, `FourierCoefficient_manual.ipynb`, and `Matching_freq.ipynb`)*

## 1. Mathematical Definition

The DFT converts a finite sequence of equally-spaced samples of a function into a same-length sequence of equally-spaced samples of the discrete-time Fourier transform (DTFT), which is a complex-valued function of frequency.

The formula for the Discrete Fourier Transform is:

$$ X[k] = \sum_{n=0}^{N-1} x[n] \cdot e^{-i \cdot 2\pi \cdot \frac{k}{N} \cdot n} $$

Where:
- $X[k]$ is the complex Fourier coefficient for the $k$-th frequency bin.
- $N$ is the total number of samples.
- $n$ is the current sample index (time domain).
- $x[n]$ is the value of the signal at time index $n$.
- $k$ is the current frequency bin (ranging from $0$ to $N-1$).
- $e^{-i \cdot 2\pi \cdot \frac{k}{N} \cdot n}$ is the complex test wave at frequency $k$.

## 2. Calculating the DFT Manually
Instead of relying on optimized libraries, we can implement the formula above using standard Python loops. This demonstrates exactly how every frequency bin is calculated by iterating over the entire time signal.

### Code Example
```python
import numpy as np

def calculate_dft(signal):
    signal = np.asarray(signal, dtype=float)
    N = len(signal)
    
    # Initialize an array of zeros to hold the complex coefficients
    spectrum = np.zeros(N, dtype=complex) 
    
    # Loop over each frequency bin k
    for k in range(N):
        coefficient = 0j
        
        # Loop over each time step n
        for n in range(N):
            # Calculate the complex angle
            angle = -2j * np.pi * k * n / N
            test_wave_value = np.exp(angle)
            
            # Multiply signal by test wave and add to the running sum
            product = signal[n] * test_wave_value
            coefficient += product
            
        # Store the complex sum in the spectrum
        spectrum[k] = coefficient
        
    return spectrum

# Test with a simple signal
signal = np.array([1, 0, -1, 0], dtype=float)
dft_result = calculate_dft(signal)
print(dft_result)
```

## 3. Extracting Magnitude and Phase
Each coefficient in `dft_result` is a complex number (e.g., `2.0 + 0.0j`). 
- **Magnitude:** The absolute value of the complex coefficient, representing the strength of that frequency. Computed using `np.abs(coefficient)`.
- **Phase:** The angle of the complex coefficient, representing the shift of the wave. Computed using `np.angle(coefficient)`.

*Note: While manual calculation helps build intuition, it operates in $O(N^2)$ time complexity, making it far too slow for real audio processing. This is why the Fast Fourier Transform (FFT) was invented.*
