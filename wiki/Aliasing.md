# Aliasing in Audio Processing

In digital audio, **Aliasing** is a phenomenon that occurs when a continuous-time signal (analog audio) is sampled at a rate that is too low to capture its highest frequency components accurately. 

## The Nyquist-Shannon Sampling Theorem
To perfectly reconstruct a continuous signal from its discrete samples, the sampling rate must be strictly greater than twice the highest frequency present in the signal. This minimum required rate is known as the **Nyquist rate**.

- **Nyquist Frequency**: Half of the sampling rate ($f_s / 2$). It represents the maximum frequency that can be represented correctly in the digital signal.
  - For example, standard CD audio has a sampling rate of 44.1 kHz, meaning the Nyquist frequency is 22.05 kHz. Since human hearing caps out around 20 kHz, this sampling rate safely captures all audible frequencies.

## What Happens During Aliasing?
If a continuous audio signal contains frequencies higher than the Nyquist frequency, those frequencies are not correctly digitized. Instead, they "fold back" or "alias" into the lower, valid frequency range ($0$ to Nyquist frequency). 

This results in unwanted, inharmonic artifacts and distortion in the digital signal. Once a signal is aliased, there is no way to perfectly separate the true low frequencies from the folded-back high frequencies.

## Preventing Aliasing
To prevent aliasing, an **Anti-Aliasing Filter** is used during the analog-to-digital conversion (ADC) process. 
- This is a steep low-pass filter placed *before* the sampler.
- It removes or heavily attenuates all frequencies above the Nyquist frequency, ensuring that no high-frequency content can alias back into the audible spectrum.

Similarly, when downsampling (lowering the sample rate) a digital audio file, a digital low-pass filter must be applied before discarding samples to prevent the existing high frequencies from aliasing at the new, lower Nyquist frequency.
