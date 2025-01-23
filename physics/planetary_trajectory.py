import numpy as np
import matplotlib.pyplot as plt

# Константы и параметры системы
G = 6.67430e-11  # гравитационная постоянная, м^3/(кг·с^2)
M = 1.989e30  # масса Солнца, кг
m = 5.972e24  # масса планеты, кг
dt = 1000  # шаг времени, сек
t_max = 3.154e7  # моделируем 1 год (сек)
x0, y0 = 1.496e11, 0.0  # начальные координаты (1 астрономическая единица), м
vx0, vy0 = 0.0, 29783  # начальные скорости, м/с (орбитальная скорость Земли)

# Инициализация массивов
t = np.arange(0, t_max, dt)
x = np.zeros_like(t)
y = np.zeros_like(t)
vx = np.zeros_like(t)
vy = np.zeros_like(t)

# Начальные условия
x[0], y[0] = x0, y0
vx[0], vy[0] = vx0, vy0

# Численное решение уравнений движения методом Эйлера
for i in range(1, len(t)):
    r = np.sqrt(x[i-1]**2 + y[i-1]**2)  # расстояние до центра
    ax = -G * M * x[i-1] / r**3  # ускорение по x
    ay = -G * M * y[i-1] / r**3  # ускорение по y
    vx[i] = vx[i-1] + ax * dt  # скорость по x
    vy[i] = vy[i-1] + ay * dt  # скорость по y
    x[i] = x[i-1] + vx[i-1] * dt  # координата x
    y[i] = y[i-1] + vy[i-1] * dt  # координата y

# Построение траектории
plt.figure(figsize=(8, 8))
plt.plot(x, y, label="Траектория планеты")
plt.scatter(0, 0, color="yellow", label="Солнце", s=200)  # центр
plt.title("Траектория движения планеты в поле центральной силы")
plt.xlabel("x (м)")
plt.ylabel("y (м)")
plt.axis("equal")
plt.grid()
plt.legend()
plt.show()
