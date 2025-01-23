import random


def function_of_x(x):
    return x**2


start_point_a = 0
end_point_b = 5
step_intervals = 100

x_random = [random.uniform(start_point_a, end_point_b) for _ in range(step_intervals)]
f_values = [function_of_x(x) for x in x_random]
result_of_integral = (end_point_b - start_point_a) * sum(f_values) / step_intervals

print(f"Приближённое значение интеграла: ~ {result_of_integral:.2f}.")
