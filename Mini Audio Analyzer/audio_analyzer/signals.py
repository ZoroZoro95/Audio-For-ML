import numpy as np

def generate_synthetic_signal(sample_rate:int, duration:float)-> tuple[np.ndarray,np.ndarray]:
    """
    This function generates the synthetic signal.
    Returns:
        time : sampling times in seconds, shape(number of samples,)
        signal : Signal Amplitudes , shape(number of samples,)
    """
    #No of samples
    N = int(sample_rate*duration) #48000 samples
    #sample indices
    n = np.arange(N)

    time = n/sample_rate

    signal = np.zeros(N)
    # 0–1 sec -> 200 Hz
    signal[:sample_rate] = np.sin(
        2 * np.pi * 200 * time[:sample_rate]
    )

    # 1–2 sec -> 500 Hz
    signal[sample_rate:2 * sample_rate] = np.sin(
        2 * np.pi * 500 * time[sample_rate:2 * sample_rate]
    )

    # 2–3 sec -> 200 Hz + 500 Hz
    signal[2 * sample_rate:] = (
        np.sin(
            2 * np.pi * 200 * time[2 * sample_rate:]
        )
        +
        0.5 * np.sin(
            2 * np.pi * 500 * time[2 * sample_rate:]
        )
    )
    return time,signal