#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include <time.h>

void fft(complex double* x, int N) {
    if (N <= 1) {
        return;
    }

    // Divide the array into two parts: even and odd indices
    complex double* even = malloc(N / 2 * sizeof(complex double));
    complex double* odd = malloc(N / 2 * sizeof(complex double));

    for (int i = 0; i < N / 2; ++i) {
        even[i] = x[2 * i];
        odd[i] = x[2 * i + 1];
    }

    // Recursive calls
    fft(even, N / 2);
    fft(odd, N / 2);

    // Combine
    for (int k = 0; k < N / 2; ++k) {
        complex double t = cexp(-2 * I * M_PI * k / N) * odd[k];
        x[k] = even[k] + t;
        x[k + N / 2] = even[k] - t;
    }

    free(even);
    free(odd);
}


/// initial run with a random N to make sure function works. needed to change to malloc to account for memory issues on big N
int main() {
    // Example usage and speed test
    int N = 1024; // Size of the input, ideally a power of two
    complex double* x = malloc(N * sizeof(complex double));

    // Initialize the input with some values
    for (int i = 0; i < N; ++i) {
        x[i] = cos(2 * M_PI * i / N) + I * sin(2 * M_PI * i / N);
    }

    // Measure the execution time
    clock_t start = clock();
    fft(x, N);
    clock_t end = clock();
    double runtime = (double)(end - start) / CLOCKS_PER_SEC;
    
    printf("FFT runtime: %f seconds\n", runtime);

    free(x);
    return 0;
}


/// clocking the function after using malloc for memory issues
// int main() {
//     //test_fft();

//     const int N = 1 << 22;  // 2^22
//     double complex *x = malloc(N * sizeof(double complex));

//     if (x == NULL) {
//         printf("Memory allocation failed.\n");
//         return 1;
//     }

//     // Initialize x with values for a cosine wave
//     for (int i = 0; i < N; i++) {
//         x[i] = cos(M_PI * 0.1 * i);
//     }

//     // Measure the start time
//     clock_t start = clock();

//     // Call your FFT function
//     fft(x, N);

//     // Measure the end time
//     clock_t end = clock();

//     // Calculate the runtime in seconds
//     double runtime = (double)(end - start) / CLOCKS_PER_SEC;

//     printf("FFT execution time: %f seconds\n", runtime);

//     // Check if runtime is less than 5 seconds
//     if (runtime < 5) {
//         printf("Success: FFT is sufficiently fast.\n");
//     } else {
//         printf("Failure: FFT is too slow.\n");
//     }

//     free(x);
//     return 0;
// }




// void fft(double complex *x, int N) {
//     if (N <= 1) return;

//     double complex even[N/2];
//     double complex odd[N/2];

//     for (int i = 0; i < N / 2; i++) {
//         even[i] = x[i * 2];
//         odd[i] = x[i * 2 + 1];
//     }

//     fft(even, N / 2);
//     fft(odd, N / 2);

//     for (int k = 0; k < N / 2; k++) {
//         double complex t = cexp(-I * M_PI * k / N) * odd[k];
//         x[k] = even[k] + t;
//         x[k + N / 2] = even[k] - t;
//     }
// }
