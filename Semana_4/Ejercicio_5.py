import math
from math import sqrt


class Complex(object):

    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex((self.real * other.real) - (self.imag * other.imag),
                       (self.imag * other.real) + (self.real * other.imag))

    def __truediv__(self, other):
        r = (other.real ** 2 + other.imag ** 2)
        return Complex((self.real * other.real - self.imag * other.imag) / r,
                       (self.imag * other.real + self.real * other.imag) / r)

    def __abs__(self):
        print('\nAbsolute Value:')
        new = (self.real ** 2 + (self.imag ** 2) * -1)
        return Complex(sqrt(new.real))

    def __str__(self):
        return str(self.real) + "+" + str(self.imag) + "i"

#realizar ej 5
c1 = Complex(1,2)

if not hasattr(c1, "__add_"):
    raise TypeError("El método no está definido")