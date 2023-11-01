# import numpy as np

# # Define the input array
# input_array = np.arange(1, 17)

# # Compute the DFT using NumPy's FFT function
# dft_result = np.fft.fft(input_array)

# # Print the result
# print("DFT of the array from 1 to 16 is:")
# print(dft_result)

# import numpy as np

# def simulated_fft(x):
#     N = len(x)
#     if N <= 1:
#         return x
#     even = simulated_fft(x[0::2])
#     odd = simulated_fft(x[1::2])
#     T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
#     return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

# # Test the function with a random array
# N = 16  # Make sure N is a power of 2 for radix-2 FFT
# x = np.random.rand(N) + 1j * np.random.rand(N)

# # Compare the simulated FFT with NumPy's FFT
# X_my = simulated_fft(x)
# X_np = np.fft.fft(x)

# # Check if the outputs are almost equal
# np.testing.assert_array_almost_equal(X_my, X_np)
# print("Outputs are almost equal!")

import numpy as np

def test_fft_python(N):
    # Initialize a test array with the same values used in the C implementation
    x = [np.exp(2j * np.pi * i / N) for i in range(N)]

    # Apply FFT using NumPy's FFT function
    fft_result = np.fft.fft(x)

    # Print the results
    print(f"Python FFT Results for N = {N}:")
    for value in fft_result:
        print(f"{value.real} + {value.imag}i")

if __name__ == "__main__":
    N = 16  # Same size used in the C test
    test_fft_python(N)
