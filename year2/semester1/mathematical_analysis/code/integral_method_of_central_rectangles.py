def function_of_x(list_of_x):
    return [i**2 for i in list_of_x]


def calculation_of_step(a, b, n):
    return (b-a) / n


def central_rectangles_method(a, h, n):
    return [a + i * h + h / 2 for i in range(n)]


def integral_method_of_central_rectangles(list_of_x, h):
    return sum(list_of_x) * h


def main():
    start_point_a = 0
    end_point_b = 5
    step_intervals = 100
    step_h = calculation_of_step(start_point_a, end_point_b, step_intervals)
    list_of_middle_x = central_rectangles_method(start_point_a, step_h, step_intervals)
    list_of_function_of_middle_x = function_of_x(list_of_middle_x)
    result_of_integral = integral_method_of_central_rectangles(list_of_function_of_middle_x, step_h)
    print(f"Приближённое значение интеграла: ~ {result_of_integral:.2f}.")


if __name__ == "__main__":
    main()
