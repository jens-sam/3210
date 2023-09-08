#ifndef INTEGRATE_H
#define INTEGRATE_H

#include <stddef.h>

typedef struct {
    size_t len;
    double *data;
} array;

void cumulative_integrate(array *y, array *y_time, const array *f, const array *f_time);

#endif
