#ifndef FAST_FOURIER_H
#define FAST_FOURIER_H

#ifdef __cplusplus
extern "C" {
#endif

void dft(const double *in_real, const double *in_imag, double *out_real, double *out_imag, int N);

#ifdef __cplusplus
}
#endif

#endif // FAST_FOURIER_H
