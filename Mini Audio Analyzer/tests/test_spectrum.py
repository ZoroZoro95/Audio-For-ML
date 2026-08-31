"""
Write tests/test_spectrum.py checking:Both shapes
Complex spectrum
0.3333 Hz spacing
frequencies[0] == 0
"""
import pytest
import numpy as np
from audio_analyzer.signals import (
    apply_window,
    generate_sine_wave,
    generate_synthetic_signal,
)
from audio_analyzer.spectrum import compute_spectrum,compute_spectrum_amplitude
from audio_analyzer.spectrum import find_dominant_frequencies

@pytest.fixture
def audio_data():
    sample_rate = 16000
    duration = 3.0
    time, signal = generate_synthetic_signal(sample_rate, duration)
    frequencies, spectrum = compute_spectrum(signal, sample_rate)
    amp_frequencies, amplitudes = compute_spectrum_amplitude(signal, sample_rate)
    return {
        "sample_rate": sample_rate,
        "signal": signal,
        "frequencies": frequencies,
        "spectrum": spectrum,
        "amp_frequencies": amp_frequencies,
        "amplitudes": amplitudes
    }

def test_shape_and_type(audio_data):
    frequencies = audio_data["frequencies"]
    spectrum = audio_data["spectrum"]
    expected_shape = (48000,)
    assert frequencies.shape == expected_shape
    assert spectrum.shape == expected_shape
    assert np.iscomplexobj(spectrum)

def test_spacing(audio_data):
    sample_rate = audio_data["sample_rate"]
    signal = audio_data["signal"]
    frequencies = audio_data["frequencies"]
    expected_spacing = sample_rate / signal.size
    actual_spacing = frequencies[1] - frequencies[0]
    assert np.isclose(actual_spacing, expected_spacing)

def test_zero_freq(audio_data):
    frequencies = audio_data["frequencies"]
    assert np.isclose(frequencies[0],0.0)

def test_compute_spectrum_amplitude(audio_data):
    """
    Add three calibration tests:
    - Constant signal of ones → DC amplitude must equal 1.
    - Alternating 1, -1, 1, -1... → Nyquist amplitude must equal 1.
    - Full-duration unit-amplitude 200 Hz sine → 200 Hz amplitude must equal 1.
    """
    amp_frequencies = audio_data["amp_frequencies"]
    amplitudes = audio_data["amplitudes"]
    sample_rate = audio_data["sample_rate"]

    assert amp_frequencies.shape == (24001,)
    assert amplitudes.shape == (24001,)
    assert np.isclose(amp_frequencies[0],0.0)
    assert np.isclose(amp_frequencies[-1],8000.0)
    assert np.isclose(amplitudes[0],0.0)
    assert np.isclose(amplitudes[-1],0.0)

    # Constant signal of ones → DC amplitude must equal 1.
    signal = np.ones(sample_rate * 2)
    frequencies, amps = compute_spectrum_amplitude(signal, sample_rate)
    dc_index = np.argmin(np.abs(frequencies))
    assert np.isclose(amps[dc_index], 1.0)

    # Alternating 1, -1, 1, -1... → Nyquist amplitude must equal 1.
    signal = np.array([1, -1] * (sample_rate * 2 // 2))
    frequencies, amps = compute_spectrum_amplitude(signal, sample_rate)
    nyquist_index = np.argmin(np.abs(frequencies - sample_rate / 2))
    assert np.isclose(amps[nyquist_index], 1.0)

    # Full-duration unit-amplitude 200 Hz sine → 200 Hz amplitude must equal 1.
    signal = np.sin(2 * np.pi * 200 * np.arange(sample_rate * 3) / sample_rate)
    frequencies, amps = compute_spectrum_amplitude(signal, sample_rate)
    two_hundred_hz_index = np.argmin(np.abs(frequencies - 200))
    assert np.isclose(amps[two_hundred_hz_index], 1.0)

def test_find_dominant_frequencies_bug():
    frequencies = [0, 10, 20]
    amplitudes = [0, 4, 5]
    largest_freq, second_freq, l_idx, s_idx, l_amp, s_amp = find_dominant_frequencies(frequencies, amplitudes)
    assert second_freq == 10

def test_find_dominant_frequencies_audio_data(audio_data):
    frequencies = audio_data["amp_frequencies"]
    amplitudes = audio_data["amplitudes"]
    largest_freq, second_freq, l_idx, s_idx, l_amp, s_amp = find_dominant_frequencies(frequencies, amplitudes)

    # We expect 200 Hz to be the strongest (amplitude ~2/3) and 500 Hz to be second strongest (amplitude ~0.5)
    assert np.isclose(largest_freq, 200.0)
    assert np.isclose(second_freq, 500.0)
    assert np.isclose(l_amp, 2/3)
    assert np.isclose(s_amp, 0.5)


def test_hann_window_normalization_preserves_sine_amplitude():
    sample_rate = 16000
    signal = generate_sine_wave(1000, sample_rate, 1024)
    windowed_signal, window = apply_window(signal, "hann")

    frequencies, amplitudes = compute_spectrum_amplitude(
        windowed_signal,
        sample_rate,
        normalization_factor=window.sum(),
    )
    peak_index = np.argmax(amplitudes)

    assert np.isclose(frequencies[peak_index], 1000.0)
    assert np.isclose(amplitudes[peak_index], 1.0, atol=1e-6)


#run this file : venv/bin/python -m pytest tests/test_spectrum.py -v
