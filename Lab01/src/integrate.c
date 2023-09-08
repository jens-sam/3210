#include "integrate.h"
#include <stdlib.h>

void cumulative_integrate(array *y, array *y_time, const array *f, const array *f_time) {
	
    double delta_t; // higher precision floating points

    // trapezoidal rule for the integral

    for (int i = 1; i < f->len; ++i) {
        delta_t = f_time->data[i] - f_time->data[i - 1];
        y->data[i-1] = (f->data[i] + f->data[i - 1])* (delta_t / 2); // area of trap and store in array
        y_time->data[i-1] = f_time->data[i-1] + delta_t / 2;  // Midpoint of the interval
    }
    // for loop for cumulative sum like in python function
    for (int s = 1; s < y->len; ++s) {
        y->data[s] = y->data[s-1] + y->data[s];
    }
}
