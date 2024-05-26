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
