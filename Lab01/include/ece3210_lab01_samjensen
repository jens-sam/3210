import numpy as np
import matplotlib.pyplot as plt
import _ece3210_lab01


def c_cumtrapz(f, f_time):
    if len(f) != len(f_time):
        raise ValueError("Input arrays f and f_time must have the same length.")

    y, y_t = _ece3210_lab01.cumtrapz(f, f_time)
    return y, y_t

def py_cumtrapz(f, f_time):
    """ This is a cumulative integral function implemented
    solely using Python / NumPy ."""

    if len(f) != len(f_time):
        raise ValueError("Input arrays f and f_time must have the same length.")

    #delta_t = np.diff(f_time)
    #avg=(f[:-1]+f[1:])/2
    #y = np.cumsum(avg * delta_t)
    # y_time = f_time[:-1] + delta_t / 2
    #y_time = (f_time[:-1] + f[1:]) / 2

    delta_t = np.diff(f_time)
    trap_avg = (f[:-1] + f[1:]) / 2
    y_time = (f_time[:-1] + f_time[1:]) / 2  # Corrected calculation for midpoint
    y = np.cumsum(trap_avg*delta_t)

    return y, y_time

def main():
    t = np.linspace(0, 10, 10000)
    f = t * np.exp(-2 * t) * (t >= 1)
    analytical_eq_ = (3 / (4 * np.exp(2)) - ((1 / 4) * np.exp(-2 * t)) * (2 * t + 1)) * (t >= 1)

    y, y_time = py_cumtrapz(f, t)

    plt.figure(figsize=(10, 6))
    plt.plot(t, f, label='f(t)')
    plt.plot(t, analytical_eq_, label='Analytical y(t)')
    plt.plot(y_time, y, label='Python py_cumtrapz' )
    
    y, y_time = c_cumtrapz(f, t)
    plt.plot(y_time, y, label='C_cumtrapz')

    plt.xlabel('Time (t)')
    plt.ylabel('Value')
    plt.title('Cumulative Integration and Analytical Solution')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
