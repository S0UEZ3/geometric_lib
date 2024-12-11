def area(a, h):
    if a < 0 or h < 0:
        raise AssertionError("Error: arguments should be positive")
    return a * h / 2


def perimeter(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise AssertionError("Error: arguments should be positive")
    return a + b + c
