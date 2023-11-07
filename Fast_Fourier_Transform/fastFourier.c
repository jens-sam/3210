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



// most recent fft but not working arrays yet:

//// the last one working
void fft_recursive(const double *in_re, const double *in_im, double *out_re, double *out_im, int N) {
    if (N <= 1) {
        out_re[0] = in_re[0];
        out_im[0] = in_im[0];
        return;
    }

    double *even_re = (double*)malloc(((size_t)N / 2) * sizeof(double));
    double *even_im = (double*)malloc(((size_t)N / 2) * sizeof(double));
    double *odd_re = (double*)malloc(((size_t)N / 2) * sizeof(double));
    double *odd_im = (double*)malloc(((size_t)N / 2) * sizeof(double));

    if (even_re == NULL || even_im == NULL || odd_re == NULL || odd_im == NULL) {
        free(even_re); free(even_im);
        free(odd_re); free(odd_im);
        return; // Handle the memory allocation error properly
    }

    for (int i = 0; i < N / 2; i++) {
        even_re[i] = in_re[i * 2];
        even_im[i] = in_im[i * 2];
        odd_re[i] = in_re[i * 2 + 1];
        odd_im[i] = in_im[i * 2 + 1];
    }

    fft_recursive(even_re, even_im, out_re, out_im, N / 2);
    fft_recursive(odd_re, odd_im, out_re + N / 2, out_im + N / 2, N / 2);

    for (int k = 0; k < N / 2; k++) {
        double angle = -2.0 * M_PI * k / N;
        double t_re = cos(angle) * odd_re[k] - sin(angle) * odd_im[k];
        double t_im = sin(angle) * odd_re[k] + cos(angle) * odd_im[k];

        // Combine even and odd parts
        double even_re_k = out_re[k];
        double even_im_k = out_im[k];
        out_re[k] = even_re_k + t_re;
        out_im[k] = even_im_k + t_im;
        out_re[k + N / 2] = even_re_k - t_re;
        out_im[k + N / 2] = even_im_k - t_im;
    }

    free(even_re); free(even_im);
    free(odd_re); free(odd_im);
}

void fft(const double *in_re, const double *in_im, double *out_re, double *out_im, int N) {
    fft_recursive(in_re, in_im, out_re, out_im, N);
}
