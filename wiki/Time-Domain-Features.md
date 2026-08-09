# Time-Domain Features

This page covers the extraction and meaning of three fundamental time-domain audio features: **Amplitude Envelope (AE)**, **Root Mean Square (RMS) Energy**, and **Zero-Crossing Rate (ZCR)**.

*(Based on `AmpEnvelope.ipynb` and `RMSandZCR.ipynb`)*

## 1. Frames and Hop Length
Audio files often contain tens of thousands of samples per second (e.g., a sample rate of 44.1 kHz means 44,100 samples every second). Analyzing the entire signal as a whole doesn't tell us how the sound changes over time. Instead, we divide the audio signal into small overlapping segments called **frames**.

- **Frame Size:** The number of audio samples contained in a single frame. For example, a frame size of `1024` samples.
- **Hop Length:** The number of samples we shift to the right to start the next frame. For example, a hop length of `512`. If frame 1 is samples 0-1024, frame 2 will be samples 512-1536. This creates overlapping frames which provide a smoother sequence of features.

## 2. Amplitude Envelope (AE)
The Amplitude Envelope represents the maximum amplitude value within a given frame. It gives a rough idea of the "loudness" or "attack" of the sound, and is heavily used for **onset detection** (finding where a musical note starts).

### Mathematical Definition
For the $t$-th frame starting at index $i$, containing samples $x[i], x[i+1], ..., x[i+K-1]$ (where $K$ is the frame size):

$$ \text{AE}_t = \max_{k=0}^{K-1} |x[i + k]| $$

### Code Example
```python
import numpy as np

def amplitude_envelope(signal, frame_size, hop_length):
    amplitude_envelope = []
    
    # Iterate through the signal, jumping by 'hop_length'
    for i in range(0, len(signal), hop_length):
        # Find the maximum amplitude in the current frame
        current_frame = signal[i:i+frame_size]
        amplitude_envelope.append(max(current_frame))
        
    return np.array(amplitude_envelope)
```

## 3. Root Mean Square (RMS) Energy
While Amplitude Envelope takes the maximum value, **RMS** provides an average measure of power within a frame. It is generally a better indicator of the *perceived loudness* of a sound compared to AE because it accounts for all the energy in the frame, not just the single highest peak.

### Mathematical Definition
For a frame containing $K$ samples:

$$ \text{RMS} = \sqrt{ \frac{1}{K} \sum_{k=0}^{K-1} x[i+k]^2 } $$

### Usage
In `librosa`, you can calculate RMS easily:
```python
import librosa
rms = librosa.feature.rms(y=signal, frame_length=1024, hop_length=512)
```

## 4. Zero-Crossing Rate (ZCR)
The Zero-Crossing Rate is the rate at which the signal changes sign—from positive to negative or from negative to positive. 

### Why is ZCR useful?
ZCR is a key feature in distinguishing between different types of sounds:
- **Percussive and Noisy sounds** (like a snare drum, cymbal, or a "shh" consonant) fluctuate wildly around the zero axis, yielding a **high ZCR**.
- **Tonal and Pitched sounds** (like a piano note or a vowel sound) have smoother, more periodic waveforms, yielding a **low ZCR**.

### Mathematical Definition
For a frame containing $K$ samples:

$$ \text{ZCR} = \frac{1}{2K} \sum_{k=1}^{K-1} |\text{sgn}(x[i+k]) - \text{sgn}(x[i+k-1])| $$
where $\text{sgn}()$ is the signum function (returns $1$ for positive, $-1$ for negative).

### Usage
In `librosa`:
```python
zcr = librosa.feature.zero_crossing_rate(y=signal, frame_length=1024, hop_length=512)
```
