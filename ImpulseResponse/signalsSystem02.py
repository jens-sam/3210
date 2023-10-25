import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = "20230912-ece3210-lab03.csv"
data = pd.read_csv(file_path, skiprows=3)

# Extract the relevant columns
# iloc : used to select specific rows and columns from the DataFrame
x = data.iloc[:, :1]
y = 10 * data.iloc[:, 1:]

start_index = 1003
end_index = 1603

# Extract the data for the specified range
new_x = x.iloc[start_index:end_index + 1]
new_y = y.iloc[start_index:end_index + 1]


def analytical_solution(t):
    a = 15151.5  # alpha
    b = 173417  # beta
    c = 0.174727  # constant
    return ((c * np.exp(-a * t)) * (b * np.cos(b * t) - a * np.sin(b * t))) * (10 ** -5)

# tried plotting with complex without solving for the full h(t)
# def complex_analytical_sol(x):  # x in replace of t since i've already used it
#     r = 1000
#     c = 0.033 * 10 ** -6
#     d = 1/(r*c)
#     a = 15151
#     b = 173417*1j
#     c0 = 2.88 * 10 ** -6
#
#     return d*((c0 * (-a + b) * np.exp((-a + b) * x))/1j - (c0 * (-a + b) * np.exp((-a + b) * x))/1j) * 10**-5


solution = analytical_solution(new_x)


# Plot the measured data and the analytical solution overlay
plt.plot(new_x, new_y, color='green', label="Measured Data")
plt.plot(new_x, solution, color='blue', label="Analytical Solution")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.title("Measured Data vs. Analytical Solution")
plt.grid(True)

plt.savefig("Lab02.jpg", format="jpg")
plt.show()
