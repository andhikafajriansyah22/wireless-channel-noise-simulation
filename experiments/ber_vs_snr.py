import os
import sys
import numpy as np
import pandas as pd

# Allow importing modules from src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.signal_generator import generate_bits, bpsk_modulation
from src.channel import add_awgn
from src.detector import bpsk_demodulation
from src.metrics import calculate_ber

# Create results folder if it does not exist
os.makedirs("results", exist_ok=True)

# Experiment settings
num_bits = 100000

snr_values = [-5, 0, 5, 10, 15, 20]

ber_results = []

print("=" * 50)
print("BPSK over AWGN Simulation")
print("=" * 50)

for snr in snr_values:

    bits = generate_bits(num_bits)

    symbols = bpsk_modulation(bits)

    noisy_signal = add_awgn(symbols, snr)

    detected_bits = bpsk_demodulation(noisy_signal)

    ber = calculate_ber(bits, detected_bits)

    ber_results.append(ber)

    print(f"SNR = {snr:>3} dB   BER = {ber:.6f}")

print("=" * 50)
print("Simulation Finished")

# Save results to CSV
results = pd.DataFrame({
    "SNR_dB": snr_values,
    "BER": ber_results
})

results.to_csv("results/ber_vs_snr.csv", index=False)

print("Results saved to results/ber_vs_snr.csv")