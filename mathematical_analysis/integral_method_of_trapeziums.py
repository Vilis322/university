def function_of_x(list_of_x):
    return [i**2 for i in list_of_x]


def calculation_of_step(a, b, n):
    return (b-a) / n


def trapeziums_method(a, h, n):
    return [a + h * i for i in range(n+1)]


def integral_method_of_trapeziums(list_of_x, h):
    return (sum(list_of_x[1:-1]) + ((list_of_x[0] + list_of_x[-1]) / 2)) * h


def main():
    start_point_a = 0
    end_point_b = 5
    step_intervals = 100
    step_h = calculation_of_step(start_point_a, end_point_b, step_intervals)
    list_of_x_trapeziums = trapeziums_method(start_point_a, step_h, step_intervals)
    list_of_function_of_x_trapeziums = function_of_x(list_of_x_trapeziums)
    result_of_integral = integral_method_of_trapeziums(list_of_function_of_x_trapeziums, step_h)
    print(f"Приближённое значение интеграла: ~ {result_of_integral:.2f}.")


if __name__ == "__main__":
    main()
