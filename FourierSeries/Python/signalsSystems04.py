import numpy as np
import matplotlib.pyplot as plt
import math
import _ece3210_lab04
import time 


def c_fourier_series(a_0, a_n, b_n, t, T):
    if len(a_n) != len(b_n):
        raise ValueError("Lengths of a_n and b_n arrays must be the same.")

    # Convert Python lists to NumPy arrays
    a_0_np = np.array(a_0, dtype=np.float64)
    a_n_np = np.array(a_n, dtype=np.float64)
    b_n_np = np.array(b_n, dtype=np.float64)
    t_np = np.array(t, dtype=np.float64)

    f_m_np = _ece3210_lab04.c_fourier_series(a_0_np, a_n_np, b_n_np, t_np, T)

    return f_m_np


def py_fourier_series(a_0, a_n, b_n, t, T):
    if len(a_n) != len(b_n):
        raise ValueError("Lengths of a_n and b_n arrays must be the same.")

    f_m = []

    for time in t:
        reconstruction = a_0
        for n in range(1, len(a_n) + 1):
            reconstruction += a_n[n - 1] * math.cos(2 * n * math.pi * time / T)
            reconstruction += b_n[n - 1] * math.sin(2 * n * math.pi * time / T)
        f_m.append(reconstruction)

    return f_m

def solved_analytical(t):
    # Initialize an array to store the final signal values
    final = np.zeros(len(t))

    # Loop through each time point 't'
    for n, t in enumerate(t):
        if 0 <= t < 0.5:
            # Calculate the signal value for the first interval
            final[n] = 2 * t
        elif 0.5 < t < 1.5:
            # Calculate the signal value for the second interval
            final[n] = - 2 * t + 2
        elif 1.5 < t < 2:
            final[n] = 2 * t - 4
        else:
            # For all other times, the signal value is 0
            final[n] = 0

    return final

# left in for debugging purposes
# # Original Function for the Coefficients of the Original Signal
# def function(n):
#     # Check if n is an odd number
#     if n % 2 == 1:
#         # Calculate the coefficient for odd values of n
#         coefficient = (8 / ((np.pi ** 2) * (n ** 2))) * ((-1) ** ((n - 1) / 2))
#     else:
#         # For even values of n, the coefficient is 0
#         coefficient = 0
#     return coefficient

# Tried an if else but would not properly calculate coefficients
# I needed a .where or else it bites the dust and throws error


def function(n):
    

    # Calculate the coefficient for odd values of n
    coefficient = np.where(n % 2 == 1, (8 / ((np.pi ** 2) * (n ** 2))) * ((-1) ** ((n - 1) / 2)), 0)

    return coefficient

def calc_error_power(error_signal, step_size):
    error_power = np.sum(error_signal ** 2) * step_size
    return error_power

def main():
    m_values = [2, 4, 7, 11, 25, 50, 100, 175, 250]
    power_error = np.zeros(len(m_values))
    python_execution_times = []
    c_execution_times = []

    error_power_values = []

    plt.figure(figsize=(14, 11))
    


    for m_index, m in enumerate(m_values):
        n = np.linspace(1, m, m)
        a_0 = 0
        a_n = np.zeros(len(n))
        b_n = function(n)
        T = 2
        t = np.linspace(0, T, 4000)

        # Calculate the Fourier series using Python function
        start_time = time.time()
        python_signal = py_fourier_series(a_0, a_n, b_n, t, T)
        python_execution_time = time.time() - start_time
        python_execution_times.append(python_execution_time)

        # Calculate the Fourier series using C function
        start_time = time.time()
        c_signal = c_fourier_series(a_0, a_n, b_n, t, T)
        c_execution_time = time.time() - start_time
        c_execution_times.append(c_execution_time)  # Append execution time to the list

        # Calculate the analytical solution
        analytical_signal = solved_analytical(t)

        # Calculate the error signal
        # error_signal = analytical_signal - python_signal

        error_signal = analytical_signal - c_signal

        # Calculate error power
        error_power = calc_error_power(error_signal, t[1] - t[0])
        power_error[m_index] = error_power

        # print power error
        # print(f'Error Power (m={m}): {error_power}')

        error_power_values.append(error_power)

        # Plot analytical signal, Python signal, and error signal for each m
        plt.plot(t, analytical_signal, label=f'Analytical (m={m})', linestyle='--', alpha=0.7)
        plt.plot(t, c_signal, label=f'm={m}', linestyle='-', alpha=0.7)
        plt.plot(t, error_signal, label=f'Error (m={m})', linestyle='-.', alpha=0.7)



    # print power error numbers
    for m, error_power in zip(m_values, error_power_values):
        print(f'Error Power (m={m}): {error_power}')


        # plt.xlim(left=0.001)  # Adjust the left limit to avoid log(0)
    # plt.figure(figsize=(14, 11))

    #plt.legend(loc='upper left', bbox_to_anchor=(1,1))

    plt.xlabel('Time')
    plt.ylabel('Signal Value / Error')
    plt.legend()
    plt.title('Triangle Wave Fourier Series')
    plt.grid(True)
    plt.show()

    # Plot the power of error signal vs. m
    plt.figure(figsize=(10, 5))
    plt.plot(m_values, power_error, marker='o', linestyle='-', label='Error Power')
    plt.xlabel('m (Number of Harmonics)')
    plt.ylabel('Error Power')
    plt.title('Error Power vs. Number of Harmonics')
    plt.legend()
    plt.grid(True)
    plt.show()


# Plot execution times
    plt.figure(figsize=(10, 5))
    plt.semilogx(m_values, python_execution_times, marker='o', linestyle='-', label='Python')
    plt.semilogx(m_values, c_execution_times, marker='o', linestyle='-', label='C')
    plt.xlabel('m (Number of Harmonics)')
    plt.ylabel('Execution Time (s)')
    plt.title('Execution Time vs. Number of Harmonics')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
