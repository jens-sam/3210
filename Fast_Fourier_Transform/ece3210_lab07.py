import _ece3210_lab07
import numpy as np


def dft(x):
    x_real = np.ascontiguousarray(x.real, dtype=np.double)
    x_imag = np.ascontiguousarray(x.imag, dtype=np.double)

    result = _ece3210_lab07.dft(x_real, x_imag)
    N = len(x)

    # Split the result into real and imaginary parts
    out_real = result[:N]
    out_imag = result[N:]

    return out_real + 1j * out_imag
