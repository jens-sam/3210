import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


file_path = "scope_4.csv"

data = pd.read_csv(file_path, skiprows=3)

x = data.iloc[:, :1]
y = data.iloc[:, 1:]

# indexed for the entire CSV file
start_index = 3
end_index = 2000

# Extract the data for the specified range
new_x = x.iloc[start_index:end_index + 1]
new_y = y.iloc[start_index:end_index + 1]


def generate_shifted_square_wave(m=35):


    T0 = 1 / 20e3  # Period (1/frequency)
    omega0 = 4 * np.pi * 1e4  # Angular frequency

    # Calculate the Fourier coefficients
    Dn_values = np.zeros(2 * m + 1, dtype=complex)

    for n in range(-m, m + 1):
        if n == 0:
            Dn_values[m] = 0  # DC component
        else:
            Dn_values[m + n] = (8 / (n * np.pi)) * np.sin(0.5 * np.pi * n)

    # Time array over one period (0 to T0) with a high sampling rate
    t = np.linspace(-T0, T0, 10000)

    # Initialize the square wave signal
    square_wave = np.zeros_like(t, dtype=complex)

    # Calculate the square wave using the analytically calculated Dn coefficients
    for n in range(-m, m + 1):
        square_wave += Dn_values[m + n] * np.exp(1j * n * omega0 * t)

    return t, square_wave


def generate_input_pulse_signal(amplitude=4, T0=1 / 20e3):
    # Time array for one period (0 to T0) with a high sampling rate
    t = np.linspace(-T0/2, T0/2, 10000)

    # Generate the input pulse signal (step function)
    input_signal = np.where(np.abs(t) <= T0 / 4, amplitude, -4)

    return t, input_signal


def calculate_y(m=35):  # repeat Dn calc for y(t)

    T0 = 1 / 20e3  # Period (1/frequency)
    omega0 = 4 * np.pi * 1e4  # Angular frequency

    # Calculate the analytical Fourier coefficients Dn
    Dn_values = np.zeros(2 * m + 1, dtype=complex)
    for n in range(-m, m + 1):
        if n == 0:
            Dn_values[m] = 0  # DC component
        else:
            Dn_values[m + n] = (8 / (n * np.pi)) * np.sin(0.5 * np.pi * n)

    # Time array over one period (0 to T0) with a high sampling rate
    t = np.linspace(-T0, T0, 10000)

    # Initialize y(t)
    y_t = np.zeros_like(t, dtype=complex)

    # Calculate y(t) using the provided formula
    for n in range(-m, m + 1):
        H_jn_omega0 = -((30303 * 1j * omega0 * n) / (-(n**2 * omega0**2) + (30.303 * 1j * omega0 * n) + 30.303e9))
        y_t += H_jn_omega0 * Dn_values[m + n] * np.exp(1j * n * omega0 * t)

    return t, y_t

def main():

    t, square_wave = generate_shifted_square_wave()

    # Generate the input pulse signal (step function)
    t_pulse, input_signal = generate_input_pulse_signal()

    # Simulate the circuit response for m = 35

    t, y_t = calculate_y()

    plt.figure(figsize=(12, 6))
    plt.plot(t, np.real(square_wave), label="F(t) Input")
    # plt.plot(t, np.imag(square_wave), label="Imaginary Part")
    plt.plot(t_pulse, input_signal, label="f(t) Impulse")
    plt.plot(new_x, new_y, label="Circuit Data", color="red")
    # plt.plot(np.real(output_signal), label="Output Signal (convolved)", color="green")

    plt.plot(t, np.real(y_t), label="y(t) Output")
    #plt.plot(t, np.imag(y_t), label="Imaginary Part")

    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("LTI System Response")
    plt.legend()
    plt.grid(True)
    plt.savefig('Lab05.jpg')
    plt.show()


if __name__ == "__main__":
    main()
