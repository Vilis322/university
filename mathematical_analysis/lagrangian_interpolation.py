def basis_polynomial(i, t, points):
    xi, _ = points[i]
    result = 1
    for j, (xj, _) in enumerate(points):
        if i != j:
            result *= (t - xj) / (xi - xj)
    return result


def lagrange_polynomial(points, t):
    return sum(yi * basis_polynomial(i, t, points) for i, (xi, yi) in enumerate(points))


def main():
    points = [(0, 1), (1, 3), (2, 2)]
    t = 1.5
    print(f"Значение полинома в точке {t}: {lagrange_polynomial(points, t)}")


if __name__ == "__main__":
    main()
