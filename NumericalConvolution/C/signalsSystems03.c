#include <stdio.h>
#include <stdlib.h>

void c_convolve(const double* f, const double* t_f, int len_f, const double* h, const double* t_h, int len_h, double* y, double* t_y) {
    // Calculate the sampling period T
    double T = t_f[1] - t_f[0];

    // Determine the length of the resulting convolution signal
    int len_conv = len_f + len_h - 1;

    // Initialize arrays to store the output signal y and its time points t_y
    for (int i = 0; i < len_conv; i++) {
        y[i] = 0.0;
        t_y[i] = t_f[0] + t_h[0] + i * T;
    }

    // Perform numerical convolution
    for (int i = 0; i < len_conv; i++) {
        for (int j = 0; j < len_f; j++) {
            if (i - j >= 0 && i - j < len_h) {
                y[i] += f[j] * h[i - j] * T;
            }
        }
    }
}
