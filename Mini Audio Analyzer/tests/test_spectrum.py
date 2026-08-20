"""
Write tests/test_spectrum.py checking:Both shapes
Complex spectrum
0.3333 Hz spacing
frequencies[0] == 0
"""
from audio_analyzer.signals import generate_synthetic_signal
from audio_analyzer.spectrum import compute_spectrum
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
#run this file : venv/bin/python -m pytest tests/test_spectrum.py -v