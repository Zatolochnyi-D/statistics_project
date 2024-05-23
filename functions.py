def line_intersection(a: tuple[tuple[float]], b: tuple[tuple[float]]) -> tuple[float]:
    a1, b1 = (a[1][1] - a[0][1]) / (a[1][0] - a[0][0]), a[0][1] - (a[0][0] * (a[1][1] - a[0][1])) / (a[1][0] - a[0][0])
    a2, b2 = (b[1][1] - b[0][1]) / (b[1][0] - b[0][0]), b[0][1] - (b[0][0] * (b[1][1] - b[0][1])) / (b[1][0] - b[0][0])

    x = (b2 - b1) / (a1 - a2)
    y = (a1 * b2 - a2 * b1) / (a1 - a2)

    return (x, y)