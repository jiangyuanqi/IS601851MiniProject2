import math
from decimal import Decimal


def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c


def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c


def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = b * a
    return c


def division(a, b):
    a = float(a)
    b = float(b)
    c = b / a
    return Decimal(c).quantize(Decimal('.000000001'))


def square(a):
    a = int(a)
    c = a * a
    return c


def square_root(a):
    a = int(a)
    c = math.sqrt(a)
    return Decimal(c).quantize(Decimal('.000001'))


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiplication(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def division(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def square_root(self, a):
        self.result = square_root(a)
        return self.result