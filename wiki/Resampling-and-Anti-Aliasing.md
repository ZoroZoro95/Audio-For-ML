# Resampling and Anti-Aliasing

## 1. Downsampling

Downsampling means reducing the sampling rate of a digital signal.

**Example:**
- 48000 Hz -> 16000 Hz

For a 1-second signal:
- 48000 Hz -> 48000 samples
- 16000 Hz -> 16000 samples

The signal duration remains the same, but fewer samples are used to represent it. A simple way to think about it is keeping fewer samples per second.

However, proper downsampling usually requires filtering before samples are removed, otherwise high-frequency components may alias into lower frequencies.

## 2. Upsampling

Upsampling means increasing the sampling rate of a digital signal.

**Example:**
- 16000 Hz -> 48000 Hz

For a 1-second signal:
- 16000 Hz -> 16000 samples
- 48000 Hz -> 48000 samples

The duration remains the same, but more samples are now required. The original recording does not contain these extra sample values, so they must be estimated from the existing samples. This estimation process is called **interpolation**.

## 3. Interpolation

Interpolation estimates new sample values between existing samples.

Suppose the original samples are:
`1       3       5`

After increasing the sampling rate, we may need additional values:
`1   ?   3   ?   5`

A simple linear interpolation method could estimate:
`1   2   3   4   5`

The values 2 and 4 were not originally recorded. They were estimated from neighboring samples. Real audio resampling uses more sophisticated interpolation and filtering than this simple linear example.

**Important Idea:** Upsampling creates more sample points, but it does not create new original audio information. For example, upsampling from 16 kHz to 48 kHz increases the number of samples, but it does not magically recover frequency content that was missing from the original 16 kHz recording.

## 4. Naive Downsampling vs Proper Resampling

A naive way to downsample from 48kHz to 16kHz would be to simply take every 3rd sample:
```python
naive_downsampled = signal[::3]
```
This is dangerous! If the original signal contains frequencies above the new Nyquist frequency (8 kHz for a 16 kHz sample rate), they will alias into the new signal.

The proper way to resample is to use an **anti-aliasing filter** before downsampling. Libraries like `librosa` handle this automatically:
```python
import librosa
safe_signal = librosa.resample(signal, orig_sr=48000, target_sr=16000)
```

## 5. Understanding Aliasing: Why does 10 kHz alias to 6 kHz?

Suppose we sample a 10,000 Hz signal at 16,000 Hz.
The Nyquist frequency is 16,000 / 2 = 8,000 Hz.
Since 10,000 Hz is above the Nyquist limit, it cannot be represented uniquely.

**Mathematical Intuition:**
In discrete-time signals, frequencies repeat every sampling rate ($f_s$):
$f$ is equivalent to $f \pm k \cdot f_s$

So for our 10 kHz signal:
$10\text{ kHz} - 16\text{ kHz} = -6\text{ kHz}$

The sampled system sees 10 kHz as -6 kHz. For a real-valued sinusoid, -6 kHz and +6 kHz represent the same oscillation frequency, differing only in phase/sign. That is why the observed alias is 6 kHz.

**Nyquist Folding Intuition:**
Nyquist is the folding point. For $f_s = 16\text{ kHz}$, Nyquist is 8 kHz.
The 10 kHz signal is 2 kHz *above* Nyquist.
So it reflects 2 kHz *below* Nyquist:
$8\text{ kHz} - 2\text{ kHz} = 6\text{ kHz}$.

Both interpretations show that a 10 kHz signal sampled at 16 kHz will be incorrectly captured as a 6 kHz signal!
