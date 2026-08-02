import numpy as np


def add_awgn(signal, snr_db):
    """
    Add Additive White Gaussian Noise (AWGN).

    Supports:
    - BPSK (real)
    - QPSK (complex)
    """

    snr_linear = 10 ** (snr_db / 10)

    signal_power = np.mean(np.abs(signal) ** 2)

    noise_power = signal_power / snr_linear

    if np.iscomplexobj(signal):

        noise = (
            np.random.randn(*signal.shape)
            + 1j * np.random.randn(*signal.shape)
        ) * np.sqrt(noise_power / 2)

    else:

        noise = np.random.randn(*signal.shape) * np.sqrt(noise_power)

    return signal + noise


# -------------------------------------------------------
# LTI CHANNEL
# -------------------------------------------------------

def apply_lti_channel(signal, impulse_response):
    """
    Pass signal through an LTI channel.

    Parameters
    ----------
    signal : ndarray
        Input transmitted symbols.

    impulse_response : ndarray
        Channel impulse response.

    Returns
    -------
    ndarray
        Output signal after convolution.
    """

    output = np.convolve(signal, impulse_response, mode="same")

    return output


# -------------------------------------------------------
# DEFAULT MULTIPATH CHANNEL
# -------------------------------------------------------

def default_channel():
    """
    Example multipath channel.

    Main path:
        amplitude = 1.0

    Echo:
        amplitude = 0.5

    Second echo:
        amplitude = 0.2
    """

    return np.array([
        1.0,
        0.5,
        0.2
    ])