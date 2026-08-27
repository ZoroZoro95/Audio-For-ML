"""
Write tests/test_spectrum.py checking:Both shapes
Complex spectrum
0.3333 Hz spacing
frequencies[0] == 0
"""
from audio_analyzer.signals import generate_synthetic_signal
from audio_analyzer.spectrum import compute_spectrum,compute_spectrum_amplitude
import numpy as np
def test_shape_and_type():
    sample_rate = 16000
    duration = 3.0
    time,signal = generate_synthetic_signal(sample_rate,duration)
    frequencies,spectrum = compute_spectrum(signal,sample_rate)
    expected_shape = (48000,)
    assert frequencies.shape == expected_shape
    assert spectrum.shape == expected_shape
    assert np.iscomplexobj(spectrum)

def test_spacing():
    sample_rate = 16000
    duration = 3.0
    time,signal = generate_synthetic_signal(sample_rate,duration)
    frequencies,spectrum = compute_spectrum(signal,sample_rate)
    expected_spacing = sample_rate / signal.size
    actual_spacing = frequencies[1] - frequencies[0]
    assert np.isclose(actual_spacing, expected_spacing)

def test_zero_freq():
    sample_rate = 16000
    duration = 3.0
    time,signal = generate_synthetic_signal(sample_rate,duration)
    frequencies,_ = compute_spectrum(signal,sample_rate)
    assert np.isclose(frequencies[0],0.0)

def test_compute_spectrum_amplitude():
    """
    Add three calibration tests:
    - Constant signal of ones → DC amplitude must equal 1.
    - Alternating 1, -1, 1, -1... → Nyquist amplitude must equal 1.
    - Full-duration unit-amplitude 200 Hz sine → 200 Hz amplitude must equal 1.
    """
    sample_rate = 16000
    duration = 3.0
    time,signal = generate_synthetic_signal(sample_rate,duration)
    frequencies,amplitudes = compute_spectrum_amplitude(signal,sample_rate)
    assert frequencies.shape == (24001,)
    assert amplitudes.shape == (24001,)
    assert np.isclose(frequencies[0],0.0)
    assert np.isclose(frequencies[-1],8000.0)
    assert np.isclose(amplitudes[0],0.0)
    assert np.isclose(amplitudes[-1],0.0)
    # Constant signal of ones → DC amplitude must equal 1.
    signal = np.ones(sample_rate * 2)
    frequencies, amplitudes = compute_spectrum_amplitude(signal, sample_rate)
    dc_index = np.argmin(np.abs(frequencies))
    assert np.isclose(amplitudes[dc_index], 1.0)

    # Alternating 1, -1, 1, -1... → Nyquist amplitude must equal 1.
    signal = np.array([1, -1] * (sample_rate * 2 // 2))
    frequencies, amplitudes = compute_spectrum_amplitude(signal, sample_rate)
    nyquist_index = np.argmin(np.abs(frequencies - sample_rate / 2))
    assert np.isclose(amplitudes[nyquist_index], 1.0)

    # Full-duration unit-amplitude 200 Hz sine → 200 Hz amplitude must equal 1.
    signal = np.sin(2 * np.pi * 200 * np.arange(sample_rate * 3) / sample_rate)
    frequencies, amplitudes = compute_spectrum_amplitude(signal, sample_rate)
    two_hundred_hz_index = np.argmin(np.abs(frequencies - 200))
    assert np.isclose(amplitudes[two_hundred_hz_index], 1.0)
#run this file : venv/bin/python -m pytest tests/test_spectrum.py -v