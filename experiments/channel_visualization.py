import os
import sys
import numpy as np
import matplotlib.pyplot as plt

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

# =========================================
# Generate Signal
# =========================================

bits = generate_bits(30)

symbols = bpsk_modulation(bits)

# =========================================
# Channel
# =========================================

h = default_channel()

received = apply_lti_channel(symbols, h)

# =========================================
# Plot
# =========================================

plt.figure(figsize=(12,8))

# -------------------------------
# Input
# -------------------------------

plt.subplot(3,1,1)

plt.stem(symbols)

plt.title("Input BPSK Symbols")

plt.ylabel("Amplitude")

plt.grid(True)

# -------------------------------
# Impulse Response
# -------------------------------

plt.subplot(3,1,2)

plt.stem(h)

plt.title("Channel Impulse Response")

plt.ylabel("Amplitude")

plt.grid(True)

# -------------------------------
# Output
# -------------------------------

plt.subplot(3,1,3)

plt.stem(received)

plt.title("Output After LTI Channel")

plt.ylabel("Amplitude")

plt.xlabel("Sample")

plt.grid(True)

plt.tight_layout()

os.makedirs("results", exist_ok=True)

plt.savefig(
    "results/lti_channel_visualization.png",
    dpi=300
)

plt.show()