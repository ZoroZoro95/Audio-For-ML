"""Functions for visualizing audio signals."""

import matplotlib.pyplot as plt


def plot_waveform(time,signal):
    """Plot signal amplitude against time for the full recording."""
    plt.figure(figsize=(12,8))
    plt.plot(time,signal)

    plt.title("Synthetic Audio Waveform")
    plt.xlabel("Time [seconds]")
    plt.ylabel("Amplitude")
    plt.grid(True)

    # Hundreds of cycles are compressed into the full-duration view, so the
    # waveform appears as dense bands rather than individually visible cycles.
    plt.tight_layout()  # Prevent titles and axis labels from being clipped.
    plt.show()
