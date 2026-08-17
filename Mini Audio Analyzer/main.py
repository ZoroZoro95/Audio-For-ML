from audio_analyzer.signals import generate_synthetic_signal
from audio_analyzer.plotting import plot_waveform

def main():
    sample_rate = 16000
    duration = 3.0

    time,signal = generate_synthetic_signal(sample_rate,duration)
    print(f"Sample rate: {sample_rate} Hz")
    print(f"Duration: {duration} seconds")
    print(f"Number of samples: {signal.size}")
    print(f"Time shape: {time.shape}")
    print(f"Signal shape: {signal.shape}")
    print(f"First time value: {time[0]}")
    print(f"Last time value: {time[-1]}")

    plot_waveform(time,signal)

if __name__ == "__main__":
    main()