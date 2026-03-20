import math
import time


def taylor_sine(x, epsilon=1e-8):
    term = x
    sine = term
    n = 1
    while abs(term) > epsilon:
        term *= -x**2 / ((2 * n) * (2 * n + 1))
        sine += term
        n += 1
    return sine


epsilon = 1e-8
step = math.pi / 100
values = []

start_taylor = time.time()
for i in range(101):
    x = i * step
    taylor_result = taylor_sine(x, epsilon)
    builtin_result = math.sin(x)
    difference = abs(taylor_result - builtin_result)
    values.append((x, taylor_result, builtin_result, difference))
end_taylor = time.time()

start_builtin = time.time()
for i in range(101):
    x = i * step
    math.sin(x)
end_builtin = time.time()

print(f"{'x':^12}{'Синус (Тейлор)':^20}{'Синус (встроенный)':^20}{'Разница':^15}")
print("-" * 67)
for x, taylor, builtin, diff in values:
    print(f"{x:^12.6f}{taylor:^20.8f}{builtin:^20.8f}{diff:^15.2e}")

print("\nСравнение времени выполнения:")
print(f"Моя функция: {end_taylor - start_taylor} секунд")
print(f"Встроенная функция: {end_builtin - start_builtin} секунд")