#ifndef FAST_FOURIER_H
#define FAST_FOURIER_H

#ifdef __cplusplus
extern "C" {
#endif

void dft(const double *in_real, const double *in_imag, double *out_real, double *out_imag, int N);
// not working fft
void fft(const double *in_re, const double *in_im, double *out_re, double *out_im, int N);



#ifdef __cplusplus
}
#endif

#endif // FAST_FOURIER_H
