import numpy as np
import matplotlib.pyplot as plt

num_steps = 100

x, y = 0, 0

x_coords = [x]
y_coords = [y]

for i in range(num_steps):
    angle = 2 * np.pi * np.random.rand()
    length = np.random.rand()

    x += length * np.cos(angle)
    y += length * np.sin(angle)

    x_coords.append(x)
    y_coords.append(y)

plt.plot(x_coords, y_coords, marker='o')
plt.xlabel('X координата')
plt.ylabel('Y координата')
plt.title('Траектория броуновской частицы')
plt.grid(True)
plt.show()
