import numpy as np


def bpsk_demodulation(received_signal):
    """
    BPSK Demodulation

    Decision Rule:
        received >= 0  -> bit 1
        received < 0   -> bit 0

    Parameters
    ----------
    received_signal : numpy.ndarray

    Returns
    -------
    numpy.ndarray
        Detected bits.
    """

    detected_bits = np.where(received_signal >= 0, 1, 0)

    return detected_bits


def qpsk_demodulation(received_symbols):
    """
    QPSK Demodulation (Gray Coding)

    Mapping

        Re >= 0 and Im >= 0  -> 00
        Re <  0 and Im >= 0  -> 01
        Re <  0 and Im <  0  -> 11
        Re >= 0 and Im <  0  -> 10

    Parameters
    ----------
    received_symbols : numpy.ndarray
        Complex received symbols.

    Returns
    -------
    numpy.ndarray
        Detected bits.
    """

    bits = []

    for symbol in received_symbols:

        real = symbol.real
        imag = symbol.imag

        # 00
        if real >= 0 and imag >= 0:
            bits.extend([0, 0])

        # 01
        elif real < 0 and imag >= 0:
            bits.extend([0, 1])

        # 11
        elif real < 0 and imag < 0:
            bits.extend([1, 1])

        # 10
        else:
            bits.extend([1, 0])

    return np.array(bits)


if __name__ == "__main__":

    from signal_generator import generate_bits
    from signal_generator import bpsk_modulation
    from signal_generator import qpsk_modulation

    # ==========================
    # BPSK TEST
    # ==========================
    print("=" * 50)
    print("BPSK TEST")
    print("=" * 50)

    bits = generate_bits(20)

    symbols = bpsk_modulation(bits)

    recovered_bits = bpsk_demodulation(symbols)

    print("Original Bits:")
    print(bits)

    print()

    print("Recovered Bits:")
    print(recovered_bits)

    print()

    print("Perfect Recovery:", np.array_equal(bits, recovered_bits))

    print()

    # ==========================
    # QPSK TEST
    # ==========================
    print("=" * 50)
    print("QPSK TEST")
    print("=" * 50)

    bits = generate_bits(20)

    symbols = qpsk_modulation(bits)

    recovered_bits = qpsk_demodulation(symbols)

    print("Original Bits:")
    print(bits)

    print()

    print("QPSK Symbols:")
    print(symbols)

    print()

    print("Recovered Bits:")
    print(recovered_bits)

    print()

    print("Perfect Recovery:", np.array_equal(bits, recovered_bits))