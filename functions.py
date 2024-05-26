import math
from scipy.stats import norm

def line_intersection(a: tuple[tuple[float]], b: tuple[tuple[float]]) -> tuple[float]:
    a1, b1 = (a[1][1] - a[0][1]) / (a[1][0] - a[0][0]), a[0][1] - (a[0][0] * (a[1][1] - a[0][1])) / (a[1][0] - a[0][0])
    a2, b2 = (b[1][1] - b[0][1]) / (b[1][0] - b[0][0]), b[0][1] - (b[0][0] * (b[1][1] - b[0][1])) / (b[1][0] - b[0][0])

    x = (b2 - b1) / (a1 - a2)
    y = (a1 * b2 - a2 * b1) / (a1 - a2)

    return (x, y)

def laplace_function(t) -> float:
    return 2 * norm.cdf(t) - 1

def inverse_laplace_function(x, accuracy = 0.001) -> float:
    a = 0
    b = 5
    c: float
    iterations_count = math.ceil(math.log2((b - a)/accuracy))
    for i in range(iterations_count + 1):
        c = (b - a) / 2 + a
        if laplace_function(c) > x:
            b = c
        else:
            a = c

    return c

def division_method_equation_solve(func, borders: tuple[float] | list[float],  accuracy: float = 0.001) -> float:
    left, right = borders
    center: float
    iterations_count = math.ceil(math.log2((right - left) / accuracy))

    for i in range(iterations_count):
        center = (right - left) / 2 + left
        value_at_left = func(left)
        value_at_right = func(right)
        value_at_center = func(center)

        if value_at_center * value_at_left < 0:
            right = center
        elif value_at_center * value_at_right < 0:
            left = center
        else:
            return center

    return center