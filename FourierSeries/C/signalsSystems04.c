//
// Created by Sam Jensen on 10/8/23.
//

#include <stdio.h>
#include <math.h>

void c_fourier_series(double a_0, double* a_n, double* b_n, double* t, double T, double* f_m, int asize, int tsize) {
    int n;
    for (int i = 0; i < tsize; i++) {
        f_m[i] = a_0;  // Initialize with a_0
        for (n = 1; n <= asize; n++) {
            f_m[i] += a_n[n - 1] * cos(2 * n * M_PI * t[i] / T);
            f_m[i] += b_n[n - 1] * sin(2 * n * M_PI * t[i] / T);
        }
    }
}
