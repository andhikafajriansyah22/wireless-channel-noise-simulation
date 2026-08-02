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
    bpsk_modulation
)

from src.channel import (
    apply_lti_channel,
    default_channel
)

from src.equalizer import (
    zero_forcing_equalizer
)

np.set_printoptions(precision=3, suppress=True)

bits = generate_bits(20)

symbols = bpsk_modulation(bits)

channel = default_channel()

received = apply_lti_channel(symbols, channel)

equalized = zero_forcing_equalizer(
    received,
    channel
)

print("="*60)
print("Original")
print("="*60)
print(symbols)

print()

print("="*60)
print("After Channel")
print("="*60)
print(received)

print()

print("="*60)
print("After Equalizer")
print("="*60)
print(equalized)