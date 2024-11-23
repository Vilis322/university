import matplotlib.pyplot as plt
import math as m


def calculate_lissajous(A1, A2, n, t_max=100, num_points=300):

    t = [i * t_max / num_points for i in range(num_points)]

    x = [A1 * m.cos(i) for i in t]

    y = [A2 * m.sin(n * i) for i in t]

    plt.figure(figsize=(6, 6))
    plt.plot(x, y)
    plt.title(f"Фигура Лиссажу: А1 = {A1}, A2 = {A2}, n = {n}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis("equal")
    plt.show()


calculate_lissajous(A1=10, A2=10, n=10/25)
