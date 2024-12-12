import math

# Product of pi and square of radius


def area(r):

    return math.pi * r * r

# Product of 2, pi and radius


def perimeter(r):
    if r < 0:
        raise AssertionError("Error: argument should be positive")
    return 2 * math.pi * r
