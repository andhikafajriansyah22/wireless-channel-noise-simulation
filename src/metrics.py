import numpy as np


def calculate_ber(original_bits, recovered_bits):
    """
    Calculate Bit Error Rate (BER).

    Parameters
    ----------
    original_bits : numpy.ndarray
        Original transmitted bits.

    recovered_bits : numpy.ndarray
        Detected bits.

    Returns
    -------
    float
        Bit Error Rate.
    """

    errors = np.sum(original_bits != recovered_bits)

    ber = errors / len(original_bits)

    return ber