import numpy as np
from audio_analyzer.signals import apply_window, generate_synthetic_signal

def test_signal_shape():
    sample_rate = 16000
    duration = 3.0

    time,signal = generate_synthetic_signal(sample_rate, duration)
    expected_samples = int(sample_rate * duration)
    assert time.shape == (expected_samples,)
    assert signal.shape == (expected_samples,)

def test_time_value():
    sample_rate = 16_000
    duration = 3.0

    time, _ = generate_synthetic_signal(sample_rate, duration)

    assert time[0] == 0.0
    assert time[-1] == 2.9999375

def test_first_segment():
    sample_rate = 16000
    duration = 3.0

    time,signal = generate_synthetic_signal(sample_rate,duration)

    expected = np.sin(2 * np.pi * 200 * time[:sample_rate])

    np.testing.assert_allclose(signal[:sample_rate], expected)

def test_second_segment():
    sample_rate = 16000
    duration = 3.0

    time,signal = generate_synthetic_signal(sample_rate,duration)

    expected = np.sin(2 * np.pi * 500 * time[sample_rate:2*sample_rate])

    np.testing.assert_allclose(signal[sample_rate:2*sample_rate], expected)

def test_third_segment():
    sample_rate = 16000
    duration = 3.0

    time,signal = generate_synthetic_signal(sample_rate,duration)

    expected = np.sin(
            2 * np.pi * 200 * time[2 * sample_rate:]
        )+ 0.5 * np.sin(
            2 * np.pi * 500 * time[2 * sample_rate:]
        )

    np.testing.assert_allclose(signal[2*sample_rate:], expected)


def test_hann_window_length_matches_signal():
    signal = np.ones(1024)

    windowed_signal, window = apply_window(signal, "hann")

    assert len(window) == len(signal)
    assert len(windowed_signal) == len(signal)


def test_hann_window_endpoints_are_zero():
    signal = np.ones(1024)

    _, window = apply_window(signal, "hann")

    assert np.isclose(window[0], 0.0)
    assert np.isclose(window[-1], 0.0)
