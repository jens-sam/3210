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



# a couple fft wrappers but not working with arrays

"""the best so far
# def fft(x):
#     # Get the original length of the input array
#     N = len(x)
# 
#     # Calculate the next power of 2 for zero-padding if necessary
#     # N_adjust = int(2 ** np.ceil(np.log2(N)))
#     N_adjust = int(2 **np.ceil(np.log2(N)))
#     # Zero-pad the input array if necessary
#     x_padded = np.zeros(N_adjust, dtype=complex)
#     x_padded[:N] = x
# 
#     # Call the C extension function. This function should return a single array
#     # with real and imaginary parts interlaced, i.e., [re0, im0, re1, im1, ...]
#     X_interlaced = _ece3210_lab07.fft(x_padded.real, x_padded.imag)
# 
#     # Now, we need to re-structure this interlaced output into a complex array
#     # Take every second element starting from 0 as real part and from 1 as imaginary part
#     X_my = X_interlaced[::2] + 1j * X_interlaced[1::2]
# 
#     return X_my  # Return the complex FFT result
"""


def fft(x):
    N = len(x)  # Original length of the input array
    N_adjust = int(2 ** np.ceil(np.log2(N)))  # Next power of two

    # Pad the input array with zeros if necessary to get the size to N_adjust
    x_padded = np.zeros(N_adjust, dtype=complex)
    x_padded[:N] = x

    # Call the C++ extension function
    X_interlaced = _ece3210_lab07.fft(x_padded.real, x_padded.imag)

    # Reconstruct the complex array from the interlaced real and imaginary parts
    X_my = X_interlaced[::2] + 1j * X_interlaced[1::2]

    # Make sure to return only the first N/2 + 1 elements which correspond to the FFT of a real signal
    return X_my[:N//2 + 1]

