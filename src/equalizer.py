import numpy as np


def zero_forcing_equalizer(signal, impulse_response):
    """
    Zero-Forcing Equalizer

    Uses simple inverse filtering in the frequency domain.

    Parameters
    ----------
    signal : ndarray
        Received signal.

    impulse_response : ndarray
        Channel impulse response.

    Returns
    -------
    ndarray
        Equalized signal.
    """

    signal = np.asarray(signal)
    h = np.asarray(impulse_response)

    # FFT size
    n = len(signal)

    # FFT of signal
    Y = np.fft.fft(signal, n)

    # FFT of channel
    H = np.fft.fft(h, n)

    # Prevent division by zero
    H[np.abs(H) < 1e-8] = 1e-8

    # Zero Forcing
    X = Y / H

    # Back to time domain
    x = np.fft.ifft(X)

    # If signal is real, remove tiny imaginary part
    if np.isrealobj(signal):
        x = np.real(x)

    return x