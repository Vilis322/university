def derivative(y, step):
    return [
        (-y[i+2] + 4 * y[i+1] - 3 * y[i]) / (2*step) if i == 0 else
        (y[i+1] - y[i-1]) / (2*step) if 0 < i < len(y) - 1 else
        (y[i-2] - 4 * y[i-1] + 3 * y[i]) / (2*step)
        for i in range(len(y))
    ]


def main():
    x = list(range(1, 7))
    y = [i**3 for i in x]
    first_derivative = derivative(y, step=1)
    print(f"Первая производная: {first_derivative}\nВторая производная: {derivative(first_derivative, step=1)}")


if __name__ == '__main__':
    main()


