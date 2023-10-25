import numpy as np
import matplotlib.pyplot as plt
import _ece3210_lab03


def c_convolve(f, t_f, h, t_h):
    if len(f) != len(t_f) or len(h) != len(t_h):
       raise ValueError("Length of input arrays and time arrays must match.")

    # Convert Python lists to NumPy arrays
    f_np = np.array(f, dtype=np.float64)
    t_f_np = np.array(t_f, dtype=np.float64)
    h_np = np.array(h, dtype=np.float64)
    t_h_np = np.array(t_h, dtype=np.float64)

    y, t_y = _ece3210_lab03.c_convolve(f_np, t_f_np, h_np, t_h_np)
    return y, t_y

def analytical_sol(t):
    y = np.zeros(len(t))
    for n, t in enumerate(t):
        if t<= 3:
            y[n] = 0
        elif 3 <= t < 6:
            y[n] = (2 * np.exp((-t/2)-1) - 2 * np.exp(0.5 - t))
        elif 6 < t < 12:
            y[n] = (2 * np.exp(-t)) * (np.exp((t - 2) / 2) - np.exp((t - 5) / 2))
        elif 12 < t < 15:
            y[n] = (2 * np.exp(-t) * (np.exp(10 / 2) - np.exp((t - 5) / 2)))
        elif t >= 15:
            y[n] = 0
    return y


def time_compute_conv(f, t_f, h, t_h, implementation):
    import time
    start_time = time.time()
    if implementation == 'Py':
        py_convolve(f, t_f, h, t_h)
    elif implementation == 'C':
        c_convolve(f, t_f, h, t_h)
    end_time = time.time()
    return end_time - start_time


def py_convolve(f, t_f, h, t_h):

    # Check if the lengths of f and t_f are the same
    if len(f) != len(t_f):
        raise ValueError("Length of f and t_f must be the same.")

    # Check if the lengths of h and t_h are the same
    if len(h) != len(t_h):
        raise ValueError("Length of h and t_h must be the same.")

    # Calculate the sampling period T
    T = t_f[1] - t_f[0]

    # Determine the length of the resulting convolution signal
    len_conv = len(f) + len(h) - 1

    # Initialize arrays to store the output signal y and its time points t_y
    y = np.zeros(len_conv)
    t_y = np.arange(len_conv) * T

    # Determine the correct starting time for t_y based on t_f and t_h
    t_y_start = t_f[0] + t_h[0]

    # Adjust t_y to start with the correct negative values
    t_y = t_y + t_y_start

    # Perform numerical convolution
    for i in range(len_conv):
        for j in range(len(f)):
            if 0 <= i - j < len(h):
                y[i] += f[j] * h[i - j] * T

    return y, t_y


def main():
    # plotting
    t_array = np.linspace(0, 15, 500)
    # analytical solution
    y_analytical = analytical_sol(t_array)
    f = np.exp(-t_array / 2) * (np.heaviside(t_array - 1, 1) - np.heaviside(t_array - 10, 1))
    h = np.exp(-t_array) * (np.heaviside(t_array - 2, 1) - np.heaviside(t_array - 5, 1))
    t_c = t_array
    t_h = t_array
    t_f = t_array

    y_c, t_c = c_convolve(f, t_f, h, t_h)

    plt.figure(figsize=(16, 8))

    # 1. h(t) and f(t)
    # plt.subplot(2, 2, 1)
    plt.plot(t_h, h, label="h(t) = e^(-t/2) [u(t-1) - u(t-10)]")
    plt.plot(t_f, f, label="f(t) = e^(-t) [u(t-2) - u(t-5)]")
    plt.legend()
    plt.xlim(0, 16)
    plt.title("h(t) and f(t) Functions")
    plt.savefig("h(t) and f(t).jpg")
    plt.show()

    plt.figure(figsize=(16, 8))
    # 2. Convolution Python, Convolution C, Analytical
    # plt.subplot(2, 2, 2)
    y_py, t_py = py_convolve(f, t_f, h, t_h)
    plt.plot(t_py, y_py, label="Convolution Python")
    
    y_c, t_c = c_convolve(f, t_f, h, t_h)
    plt.plot(t_c, y_c, label="Convolution C")
    plt.plot(t_array, y_analytical, label="Analytical")
    plt.legend()
    plt.xlim(2, 16)
    plt.title("Convolution Python, Convolution C, Analytical")

    plt.savefig("Overlay 3 Convolutions.jpg")
    plt.show()

    # Timing analysis
    # sampling_periods = [0.01, 0.005, 0.001]
    sampling_periods = [0.01, 0.005, 0.001, 0.0001, 0.0005, 0.00005]
    python_times = []
    c_times = []  # Separate list for C times

    for T in sampling_periods:
        t_f = np.arange(1, 5, T)
        t_h = np.arange(-2, 3, T)
        fh = np.random.uniform(-10, 10, size=len(t_f))
        hh = np.random.uniform(-10, 10, size=len(t_h))

        # Python implementation
        python_time = time_compute_conv(fh, t_f, hh, t_h, 'Py')
        python_times.append(python_time)

        # C implementation
        c_time = time_compute_conv(fh, t_f, hh, t_h, 'C')
        c_times.append(c_time)

    # Separate graph for Python time
    plt.figure(figsize=(10, 6))
    plt.loglog(python_times, sampling_periods, marker='o', label='Python Implementation')
    plt.ylabel('Sampling Rate (T)')
    plt.xlabel('Execution Time (s)')
    plt.legend()
    plt.grid(True)
    plt.title('Python Convolution Comparison')
    plt.savefig("Python_Time.jpg")
    plt.show()

    #Separate graph for C time
    plt.figure(figsize=(10, 6))
    plt.loglog(c_times, sampling_periods, marker='o', label='C Implementation')
    plt.ylabel('Sampling Rate (T)')
    plt.xlabel('Execution Time (s)')
    plt.legend()
    plt.grid(True)
    plt.title('C Convolution Comparison')
    plt.savefig("C_Time.jpg")
    plt.show()


if __name__ == "__main__":
    main()
