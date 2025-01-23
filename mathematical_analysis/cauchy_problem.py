def function(x, y):
    return x + y


def modified_euler(function, x0, y0, h, n):
    x_values = [x0]
    y_values = [y0]

    for i in range(n):
        x_current = x_values[-1]
        y_current = y_values[-1]

        y1_next = y_current + h * function(x_current, y_current)
        x_next = x_current + h

        y_next = y_current + (h / 2) * (function(x_current, y_current) + function(x_next, y1_next))

        x_values.append(round(x_next, 2))
        y_values.append(round(y_next, 2))

    return x_values, y_values


def main():
    x0 = 0
    y0 = 1
    h = 0.1
    n = 5

    x_values, y_values = modified_euler(function, x0, y0, h, n)

    print("x-values:", x_values)
    print("y-values:", y_values)


if __name__ == "__main__":
    main()
