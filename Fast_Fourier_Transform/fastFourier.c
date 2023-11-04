#include "../include/fastFourier.h"
#include <math.h>

void dft(const double *in_real, const double *in_imag, double *out_real, double *out_imag, int N) {
    for (int k = 0; k < N; k++) {  // For each output element
        out_real[k] = 0;
        out_imag[k] = 0;
        for (int n = 0; n < N; n++) {  // For each input element
            double angle = 2 * M_PI * k * n / N;
            out_real[k] += in_real[n] * cos(angle) + in_imag[n] * sin(angle);
            out_imag[k] -= in_real[n] * sin(angle) - in_imag[n] * cos(angle);
        }
    }
}
