import os
import sys
import numpy as np
import matplotlib.pyplot as plt

# Allow import from src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.signal_generator import (
    generate_bits,
    bpsk_modulation,
    qpsk_modulation
)

from src.channel import add_awgn

from src.detector import (
    bpsk_demodulation,
    qpsk_demodulation
)

from src.metrics import calculate_ber


# ======================================
# Experiment Settings
# ======================================

NUM_BITS = 100000

snr_values = np.arange(-5, 13, 2)

ber_bpsk = []
ber_qpsk = []

print("=" * 60)
print("BPSK vs QPSK over AWGN")
print("=" * 60)

for snr in snr_values:

    ###################################
    # BPSK
    ###################################

    bits = generate_bits(NUM_BITS)

    tx = bpsk_modulation(bits)

    rx = add_awgn(tx, snr)

    detected = bpsk_demodulation(rx)

    ber = calculate_ber(bits, detected)

    ber_bpsk.append(ber)


    ###################################
    # QPSK
    ###################################

    bits = generate_bits(NUM_BITS)

    tx = qpsk_modulation(bits)

    # PENTING!
    # Noise HARUS ditambahkan ke simbol QPSK
    rx = add_awgn(tx, snr)

    detected = qpsk_demodulation(rx)

    ber = calculate_ber(bits, detected)

    ber_qpsk.append(ber)


    print(
        f"SNR = {snr:>2} dB | "
        f"BPSK BER = {ber_bpsk[-1]:.6f} | "
        f"QPSK BER = {ber_qpsk[-1]:.6f}"
    )

print("=" * 60)


# ======================================
# Save CSV
# ======================================

os.makedirs("results", exist_ok=True)

data = np.column_stack((snr_values, ber_bpsk, ber_qpsk))

np.savetxt(
    "results/bpsk_vs_qpsk.csv",
    data,
    delimiter=",",
    header="SNR,BPSK,QPSK",
    comments=""
)

print("Results saved to results/bpsk_vs_qpsk.csv")


# ======================================
# Plot
# ======================================

plt.figure(figsize=(8,5))

plt.semilogy(
    snr_values,
    ber_bpsk,
    marker="o",
    linewidth=2,
    label="BPSK"
)

plt.semilogy(
    snr_values,
    ber_qpsk,
    marker="s",
    linewidth=2,
    label="QPSK"
)

plt.grid(True, which="both")

plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate (BER)")

plt.title("BPSK vs QPSK over AWGN")

plt.legend()

plt.tight_layout()

plt.savefig("results/bpsk_vs_qpsk.png", dpi=300)

plt.show()