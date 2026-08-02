import numpy as np


def generate_bits(num_bits):
    """
    Generate random binary bits.

    Parameters
    ----------
    num_bits : int
        Number of bits to generate.

    Returns
    -------
    numpy.ndarray
        Random bits (0 or 1).
    """

    return np.random.randint(0, 2, num_bits)


def bpsk_modulation(bits):
    """
    BPSK Modulation

    Mapping:
        0 -> -1
        1 -> +1

    Parameters
    ----------
    bits : numpy.ndarray

    Returns
    -------
    numpy.ndarray
        BPSK symbols.
    """

    return np.where(bits == 0, -1, 1)


def qpsk_modulation(bits):
    """
    QPSK Modulation

    Every two bits become one complex symbol.

    Mapping (Gray Coding)

        00 ->  ( 1 + 1j)/sqrt(2)
        01 -> (-1 + 1j)/sqrt(2)
        11 -> (-1 - 1j)/sqrt(2)
        10 -> ( 1 - 1j)/sqrt(2)

    Parameters
    ----------
    bits : numpy.ndarray

    Returns
    -------
    numpy.ndarray
        Complex QPSK symbols.
    """

    # Ensure even number of bits
    if len(bits) % 2 != 0:
        bits = np.append(bits, 0)

    symbols = []

    for i in range(0, len(bits), 2):

        b1 = bits[i]
        b2 = bits[i + 1]

        if b1 == 0 and b2 == 0:
            symbol = 1 + 1j

        elif b1 == 0 and b2 == 1:
            symbol = -1 + 1j

        elif b1 == 1 and b2 == 1:
            symbol = -1 - 1j

        elif b1 == 1 and b2 == 0:
            symbol = 1 - 1j

        symbols.append(symbol / np.sqrt(2))

    return np.array(symbols, dtype=complex)


if __name__ == "__main__":

    bits = generate_bits(20)

    print("Random Bits:")
    print(bits)

    print()

    bpsk = bpsk_modulation(bits)

    print("BPSK Symbols:")
    print(bpsk)

    print()

    qpsk = qpsk_modulation(bits)

    print("QPSK Symbols:")
    print(qpsk)