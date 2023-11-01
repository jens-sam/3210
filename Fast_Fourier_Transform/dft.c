// #include "ece3210_lab07.h"
#include <stdio.h>
#include <complex.h>
#define PI 3.14159265358979323846

void dft(double complex *x, double complex *X, int N) {
    for (int k = 0; k < N; k++) {
        X[k] = 0;
        for (int n = 0; n < N; n++) {
            double angle = -2 * PI * k * n / N;
            X[k] += x[n] * cexp(I * angle);
        }
    }
}

// Function to print complex array
void print_complex_array(const double complex *arr, int size) {
    for (int i = 0; i < size; i++) {
        printf("(%g + %gi) ", creal(arr[i]), cimag(arr[i]));
    }
    printf("\n");
}

// Test function for DFT
void test_dft() {
    int N = 16;
    double complex x[N];
    double complex X[N];

    // Initialize the input array (1, 2, 3, ..., 16)
    for (int i = 0; i < N; i++) {
        x[i] = i + 1;
    }

    printf("Input array:\n");
    print_complex_array(x, N);

    // Perform DFT
    dft(x, X, N);

    printf("Output DFT array:\n");
    print_complex_array(X, N);
}

int main() {
    test_dft();
    return 0;
}
