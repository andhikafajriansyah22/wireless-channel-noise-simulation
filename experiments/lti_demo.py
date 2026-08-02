import os
import sys
import numpy as np

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.signal_generator import (
    generate_bits,
    bpsk_modulation,
)

from src.channel import (
    apply_lti_channel,
    default_channel,
)

np.set_printoptions(precision=3, suppress=True)

bits = generate_bits(20)

symbols = bpsk_modulation(bits)

h = default_channel()

received = apply_lti_channel(symbols, h)

print("=" * 50)
print("Impulse Response")
print("=" * 50)
print(h)

print()

print("=" * 50)
print("Original Symbols")
print("=" * 50)
print(symbols)

print()

print("=" * 50)
print("After LTI Channel")
print("=" * 50)
print(received)