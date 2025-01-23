import numpy as np
import matplotlib.pyplot as plt

# Заданные параметры системы
m = 1.0  # масса
k = 10.0  # жесткость пружины
r = 1.0  # коэффициент сопротивления
x0 = 1.0  # начальное смещение
v0 = 0.0  # начальная скорость
dt = 0.01  # шаг времени
t_max = 10.0  # максимальное время моделирования

# Инициализация времени и массивов для x и v
t = np.arange(0, t_max, dt)
x = np.zeros_like(t)
v = np.zeros_like(t)

# Начальные условия
x[0] = x0
v[0] = v0

# Численное решение уравнений движения (метод Эйлера)
for i in range(1, len(t)):
    a = -(k * x[i-1] + r * v[i-1]) / m  # ускорение
    v[i] = v[i-1] + a * dt  # скорость
    x[i] = x[i-1] + v[i-1] * dt  # положение

# Построение графика затухающих колебаний
plt.figure(figsize=(8, 6))
plt.plot(t, x, label="Затухающие колебания")
plt.title("Затухающие колебания")
plt.xlabel("Время (t)")
plt.ylabel("Смещение (x)")
plt.grid()
plt.legend()
plt.show()
