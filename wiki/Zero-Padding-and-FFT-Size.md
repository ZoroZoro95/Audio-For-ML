# Zero-Padding and FFT Size

If you zero-pad a signal before taking the FFT:
- You DO NOT increase the actual physical frequency resolution (which is determined by the length of your original data window).
- You DO increase the frequency interpolation, creating a smoother looking spectrum.
