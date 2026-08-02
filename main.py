from src.signal_generator import generate_bits
from src.signal_generator import qpsk_modulation

bits = generate_bits(20)

symbols = qpsk_modulation(bits)

print("Bits:")
print(bits)

print()

print("QPSK Symbols:")
print(symbols)