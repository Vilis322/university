import numpy as np
import matplotlib.pyplot as plt

# Параметры системы
m = 1.0  # масса
k = 10.0  # жесткость пружины
r = 0.5  # коэффициент сопротивления
Fm = 5.0  # амплитуда вынуждающей силы
x0 = 0.0  # начальное смещение
v0 = 0.0  # начальная скорость
dt = 0.01  # шаг времени
t_max = 50.0  # максимальное время моделирования

# Частоты для анализа
omega_values = np.linspace(0.1, 5.0, 100)
amplitudes = []

# Основной цикл по частотам
for omega in omega_values:
    # Временная сетка и массивы
    t = np.arange(0, t_max, dt)
    x = np.zeros_like(t)
    v = np.zeros_like(t)

    # Начальные условия
    x[0] = x0
    v[0] = v0

    # Численное решение уравнения движения (метод Эйлера)
    for i in range(1, len(t)):
        F = Fm * np.sin(omega * t[i-1])  # вынуждающая сила
        a = (F - k * x[i-1] - r * v[i-1]) / m  # ускорение
        v[i] = v[i-1] + a * dt  # скорость
        x[i] = x[i-1] + v[i-1] * dt  # положение

    # Вычисление амплитуды как максимального значения |x|
    amplitudes.append(np.max(np.abs(x)))

# Построение графика зависимости A(ω)
plt.figure(figsize=(8, 6))
plt.plot(omega_values, amplitudes, label="Амплитуда A(ω)")
plt.title("Резонансная кривая")
plt.xlabel("Частота ω (рад/с)")
plt.ylabel("Амплитуда A")
plt.grid()
plt.legend()
plt.show()
