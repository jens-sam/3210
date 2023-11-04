#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include "fastFourier.h"

namespace py = pybind11;

PYBIND11_MODULE(_ece3210_lab07, m) {
    m.def("dft", [](py::array_t<double> in_real, py::array_t<double> in_imag) {
        py::buffer_info buf_real = in_real.request(), buf_imag = in_imag.request();

        if (buf_real.size != buf_imag.size) {
            throw std::runtime_error("Input sizes must match");
        }

        auto result = py::array_t<double>(buf_real.size * 2);
        py::buffer_info buf_result = result.request();

        double *ptr_real = static_cast<double *>(buf_real.ptr);
        double *ptr_imag = static_cast<double *>(buf_imag.ptr);
        double *ptr_result_real = static_cast<double *>(buf_result.ptr);
        double *ptr_result_imag = ptr_result_real + buf_real.size;

        dft(ptr_real, ptr_imag, ptr_result_real, ptr_result_imag, static_cast<int>(buf_real.size));

        return result;
    });
}
