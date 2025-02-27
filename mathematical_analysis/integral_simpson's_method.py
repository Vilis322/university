def function_of_x(list_of_x):
    return [i**2 for i in list_of_x]


def calculation_of_step(a, b, n):
    return (b-a) / n


def simpson_points(a, h, n):
    return [a + i * h for i in range(n+1)] if n % 2 == 0 else "Данный метод работает только для чётного разбиения!"


def integral_simpson(a, b, n, list_of_x, h):
    return (h/3) * ((a**2)+(b**2) + 4 * sum(list_of_x[i] for i in range(2, n, 2)) + 2 * sum(list_of_x[i] for i in range(1, n, 2)))


def main():
    start_point_a = 0
    end_point_b = 5
    step_intervals = 100
    step_h = calculation_of_step(start_point_a, end_point_b, step_intervals)
    list_of_simpsons_x = simpson_points(start_point_a, step_h, step_intervals)
    list_of_function_simpsons_x = function_of_x(list_of_simpsons_x)
    result_of_integral = integral_simpson(start_point_a, end_point_b, step_intervals, list_of_function_simpsons_x, step_h)
    print(f"Приближённое значение интеграла: ~ {result_of_integral:.2f}.")


if __name__ == "__main__":
    main()
