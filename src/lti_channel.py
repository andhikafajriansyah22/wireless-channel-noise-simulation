import numpy as np


class LTIChannel:
    """
    Linear Time-Invariant (LTI) Channel

    y[n] = x[n] * h[n]

    where

    x = transmitted signal
    h = impulse response
    * = convolution
    """

    def __init__(self, impulse_response):

        self.h = np.array(impulse_response)

    def transmit(self, signal):

        signal = np.array(signal)

        output = np.convolve(signal, self.h, mode="same")

        return output