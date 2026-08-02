import os
import pandas as pd
import matplotlib.pyplot as plt

# Create results folder if it does not exist
os.makedirs("results", exist_ok=True)

# Load experiment results
results = pd.read_csv("results/ber_vs_snr.csv")

# Plot BER vs SNR
plt.figure(figsize=(8, 5))

plt.semilogy(
    results["SNR_dB"],
    results["BER"],
    marker="o",
    linewidth=2
)

plt.grid(True, which="both", linestyle="--")

plt.title("BER vs SNR for BPSK over AWGN")
plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate (BER)")

plt.savefig("results/ber_vs_snr.png", dpi=300)

plt.show()

print("BER plot saved to results/ber_vs_snr.png")