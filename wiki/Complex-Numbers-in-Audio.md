# Complex Numbers in Audio

This page explores the core mathematical mechanism behind the Fourier Transform: using **Euler's Formula** and **Complex Numbers** to wrap audio signals around a circle and measure frequency correlation.

*(Based on `Defining the Fourier Transform Using Complex Numbers.ipynb`)*

## 1. Euler's Formula
To look for a specific frequency in a signal, the Fourier Transform "wraps" the signal around a circle in the complex plane. This wrapping is achieved using Euler's formula:

$$ e^{i\theta} = \cos(\theta) + i\sin(\theta) $$

By setting $\theta = -2\pi f t$, we create a "complex test wave" that rotates clockwise around the complex plane at exactly frequency $f$.

$$ e^{-i 2\pi f t} = \cos(-2\pi f t) + i\sin(-2\pi f t) $$

### Why complex numbers?
Using complex exponentials instead of just sine or cosine serves two purposes:
1. It handles both amplitude and **phase** simultaneously.
2. It's mathematically much more compact and computationally efficient.

## 2. Wrapping the Signal
If we take an audio signal $x(t)$ and multiply it point-by-point by our complex test wave, we effectively "wrap" the signal around the origin of the complex plane. 

$$ \text{Wrapped Signal} = x(t) \cdot e^{-i 2\pi f t} $$

## 3. Center of Gravity (Correlation)
Once the signal is wrapped around the origin at a specific test frequency $f$, we calculate the **Center of Mass** (or center of gravity) of this shape by taking the average (or sum) of all the points.

- **If the signal DOES NOT contain frequency $f$:** The positive and negative areas cancel out, and the center of mass will be at or very close to `(0, 0)`.
- **If the signal DOES contain frequency $f$:** The peaks of the signal align on one side of the complex plane, pulling the center of mass heavily away from the origin.

The distance from the origin to this center of mass represents the **amplitude** of that frequency in the signal, and the angle represents the **phase**.

### Code Example
```python
import numpy as np

def create_pure_tone(frequency, time):
    angle = -2 * np.pi * frequency * time
    # e^(i * angle)
    return np.cos(angle) + 1j * np.sin(angle)

def calculate_centre_of_gravity(mult_signal):
    x_centre = np.mean([x.real for x in mult_signal])
    y_centre = np.mean([x.imag for x in mult_signal])
    return x_centre, y_centre

# Create test wave and multiply with original signal
pure_tone = create_pure_tone(test_frequency, time)
mult_signal = pure_tone * signal

# If 'center_of_gravity' is far from 0, the test_frequency is present!
center_of_gravity = calculate_centre_of_gravity(mult_signal)
```
