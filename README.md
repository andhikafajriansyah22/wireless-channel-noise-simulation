# Wireless Channel Noise Simulation

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![NumPy](https://img.shields.io/badge/NumPy-Latest-orange.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Latest-green.svg)

---

# Overview

Wireless communication systems are fundamentally affected by channel impairments such as additive noise, multipath propagation, and intersymbol interference (ISI). Understanding these phenomena is essential for designing reliable digital communication systems.

This repository implements a modular Python framework for simulating wireless communication channels and evaluating digital modulation techniques. The framework includes channel modeling, BER evaluation, equalization, and frequency-domain analysis, serving as a foundation for more advanced communication system research.

Rather than being a single demonstration script, the project is organized as a reusable simulation framework that can be extended toward fading channels, OFDM, MIMO communications, channel coding, and machine learning-based wireless receivers.

---

# Features

- Binary Phase Shift Keying (BPSK)
- Quadrature Phase Shift Keying (QPSK)
- Additive White Gaussian Noise (AWGN)
- Linear Time-Invariant (LTI) Channel
- BER vs SNR Performance Analysis
- Frequency Response Visualization
- Impulse Response Visualization
- Zero-Forcing Equalizer
- Modular Signal Processing Pipeline
- Experiment-Based Project Structure

---

# Repository Structure

```text
wireless-channel-noise-simulation
│
├── src/
│   ├── signal_generator.py
│   ├── channel.py
│   ├── lti_channel.py
│   ├── detector.py
│   ├── equalizer.py
│   ├── metrics.py
│   ├── visualization.py
│   └── plot_ber.py
│
├── experiments/
│   ├── compare_bpsk_qpsk.py
│   ├── ber_vs_snr.py
│   ├── lti_demo.py
│   ├── equalizer_demo.py
│   ├── channel_visualization.py
│   └── frequency_response_demo.py
│
├── results/
│   ├── ber_vs_snr.csv
│   ├── ber_vs_snr.png
│   ├── bpsk_vs_qpsk.csv
│   ├── bpsk_vs_qpsk.png
│   ├── frequency_response.png
│   └── lti_channel_visualization.png
│
├── requirements.txt
├── main.py
└── README.md
```

---

# Communication System Pipeline

```text
Random Bits
     │
     ▼
Modulation
(BPSK / QPSK)
     │
     ▼
Wireless Channel
(AWGN / LTI)
     │
     ▼
Received Signal
     │
     ▼
Equalizer
     │
     ▼
Detector
     │
     ▼
BER Evaluation
```

---

# Implemented Experiments

## 1. BPSK and QPSK Comparison

Evaluates the performance of BPSK and QPSK under identical channel conditions.

Outputs

- BER curve
- CSV results

---

## 2. BER versus SNR

Measures communication reliability over multiple Signal-to-Noise Ratios.

Outputs

- BER vs SNR plot
- Numerical CSV data

---

## 3. LTI Channel Simulation

Demonstrates how an impulse response distorts transmitted symbols through discrete convolution.

Topics

- Linear convolution
- Channel memory
- Intersymbol interference

---

## 4. Zero-Forcing Equalizer

Implements a simple channel inversion equalizer to recover distorted signals.

Topics

- Equalization
- Signal recovery
- Channel compensation

---

## 5. Frequency Response Analysis

Visualizes the characteristics of the simulated LTI channel in the frequency domain.

Includes

- Impulse response
- Magnitude response
- Phase response

---

# Mathematical Background

### Additive White Gaussian Noise

\[
y=x+n
\]

where

- x = transmitted signal
- n = Gaussian noise

---

### Signal-to-Noise Ratio

\[
SNR=10\log_{10}\left(\frac{P_s}{P_n}\right)
\]

---

### Bit Error Rate

\[
BER=\frac{\text{Number of Bit Errors}}
{\text{Total Number of Bits}}
\]

---

### Linear Time-Invariant Channel

\[
y[n]=x[n]*h[n]
\]

where

- \(x[n]\) : transmitted signal

- \(h[n]\) : impulse response

- * : convolution

---

### Frequency Response

\[
H(f)=FFT(h[n])
\]

---

# Installation

Clone repository

```bash
git clone https://github.com/andhikafajriansyah22/wireless-channel-noise-simulation.git
```

Move into repository

```bash
cd wireless-channel-noise-simulation
```

Install required packages

```bash
pip install -r requirements.txt
```

---

# Running Experiments

Compare BPSK and QPSK

```bash
python experiments/compare_bpsk_qpsk.py
```

BER versus SNR

```bash
python experiments/ber_vs_snr.py
```

LTI Demonstration

```bash
python experiments/lti_demo.py
```

Equalizer Demonstration

```bash
python experiments/equalizer_demo.py
```

Channel Visualization

```bash
python experiments/channel_visualization.py
```

Frequency Response

```bash
python experiments/frequency_response_demo.py
```

---

# Current Capabilities

- Digital modulation simulation
- AWGN channel modeling
- BER performance evaluation
- LTI channel simulation
- Frequency-domain analysis
- Zero-Forcing equalization
- Scientific visualization

---

# Future Research Directions

This framework is intentionally designed to be extensible.

Planned future developments include

- Rayleigh Fading Channel
- Rician Fading Channel
- Adaptive LMS Equalizer
- MMSE Equalizer
- OFDM System Simulation
- MIMO Communications
- Channel Coding
- Constellation Diagram Analysis
- Eye Diagram Visualization
- Machine Learning-Based Signal Detection
- Deep Learning Receiver Architectures

---

# References

The implementation is inspired by concepts commonly taught in digital communications, signal processing, and wireless systems courses.

Recommended references

- Simon Haykin — *Communication Systems*
- John G. Proakis — *Digital Communications*
- Bernard Sklar — *Digital Communications: Fundamentals and Applications*
- MIT OpenCourseWare
- Stanford EE Communications Courses

---

# Author

**Andhika Fajriansyah**

GitHub

https://github.com/andhikafajriansyah22

---

# Acknowledgment

This project was independently developed as part of a long-term study in digital communications, wireless signal processing, and communication system simulation. It is intended as an educational and research-oriented framework that will continue to evolve with additional channel models, communication techniques, and signal processing algorithms.
