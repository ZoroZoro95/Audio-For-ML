# Window Length vs Hop Length Trade-offs

When computing a Short-Time Fourier Transform (STFT) or a spectrogram, two of the most important parameters are the **Window Length** (also known as frame size) and the **Hop Length**. The choice of these parameters fundamentally affects the time and frequency resolution of your audio representation due to the Heisenberg-Gabor limit.

## Window Length (Frame Size)
The window length dictates how many audio samples are included in a single chunk (frame) before applying the Fourier Transform. 

- **Long Window (e.g., 2048 or 4096 samples)**:
  - **High Frequency Resolution**: A longer window captures more cycles of low-frequency waves, allowing the FFT to precisely distinguish between closely spaced frequencies.
  - **Low Time Resolution**: Because the window spans a longer duration, short, transient sounds (like a drum hit or a consonant in speech) get "smeared" across time. It becomes difficult to pinpoint exactly *when* an event occurred.

- **Short Window (e.g., 256 or 512 samples)**:
  - **High Time Resolution**: A shorter window captures brief acoustic events very well, preserving the exact timing of transients.
  - **Low Frequency Resolution**: The FFT has fewer samples to work with, meaning it cannot distinguish closely spaced frequencies well, and lower frequencies might not be captured accurately.

## Hop Length
The hop length is the number of samples you advance the window for the next frame. It determines the overlap between consecutive windows.

- **Small Hop Length (Large Overlap)**:
  - Creates a smoother, denser spectrogram with a higher frame rate.
  - Useful for precise temporal tracking (e.g., pitch tracking, onset detection).
  - Computationally more expensive and uses more memory.

- **Large Hop Length (Small Overlap)**:
  - Creates a blockier spectrogram with a lower frame rate.
  - Computationally efficient.
  - May miss rapid changes if the hop is too large (e.g., larger than the window itself).

Typically, a hop length that results in a **50% to 75% overlap** (e.g., a window of 2048 and a hop of 512) provides a good balance between a smooth representation and reasonable computational cost.
