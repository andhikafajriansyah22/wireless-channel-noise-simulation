import os
import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.channel import default_channel

# ====================================
# Channel
# ====================================

h = default_channel()

# ====================================
# FFT
# ====================================

N = 512

H = np.fft.fft(h, N)

freq = np.linspace(0, 1, N)

magnitude = np.abs(H)

phase = np.angle(H)

# ====================================
# Plot
# ====================================

plt.figure(figsize=(12,8))

plt.subplot(3,1,1)

plt.stem(h)

plt.title("Impulse Response")

plt.ylabel("Amplitude")

plt.grid(True)

plt.subplot(3,1,2)

plt.plot(freq, magnitude)

plt.title("Magnitude Response")

plt.ylabel("|H(f)|")

plt.grid(True)

plt.subplot(3,1,3)

plt.plot(freq, phase)

plt.title("Phase Response")

plt.xlabel("Normalized Frequency")

plt.ylabel("Phase (rad)")

plt.grid(True)

plt.tight_layout()

os.makedirs("results", exist_ok=True)

plt.savefig(
    "results/frequency_response.png",
    dpi=300
)

plt.show()