import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
# T0 = 1 / 20e3  # Period (1/frequency)
T0 = 5 * 10**-5
m = 35  # Number of harmonics
omega0 = 4 * np.pi * 1e4  # Angular frequency

# Calculate the Fourier coefficients
Dn_values = np.zeros(2 * m + 1, dtype=complex)

for n in range(-m, m + 1):
    if n == 0:
        # Dn_values[m] = -4  # DC component
        Dn_values[m] = (8 / (np.pi * n)) * np.sin(0.52 * np.pi) - 4  # DC component
    else:
        Dn_values[m + n] = (4 / (n * np.pi)) * (1 - (-1) ** n)
        # Dn_values[m + n] = (8 / (n * np.pi)) * (np.sin(0.52*np.pi*t))

# Time array over one period (0 to T0) with a high sampling rate
t = np.linspace(0, T0, 10000)

# Initialize the square wave signal
square_wave = np.zeros_like(t, dtype=complex)

# Calculate the square wave using the analytically calculated Dn coefficients
for n in range(-m, m + 1):
    square_wave += Dn_values[m + n] * np.exp(1j * n * omega0 * t)

# Plot the square wave
plt.figure(figsize=(12, 8))
plt.plot(t, np.real(square_wave), label="Real Part")
plt.plot(t, np.imag(square_wave), label="Imaginary Part")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Square Wave Reconstruction from Analytical Dn")
plt.legend()
plt.grid(True)
plt.show()
