import numpy as np
import matplotlib.pyplot as plt

N_values = range(10, 501, 10)
num_trials = 5000

S2_values = []

for N in N_values:
    displacements = []
    for _ in range(num_trials):
        steps = np.random.choice([-1, 1], size=N)
        x_N = np.sum(steps)
        displacements.append(x_N ** 2)
    S2_values.append(np.mean(displacements))

plt.figure(figsize=(10, 6))
plt.plot(N_values, S2_values, label=r'$S^2$', marker='o')
plt.title('Средний квадрат смещения частицы vs. число шагов')
plt.xlabel('Число шагов N')
plt.ylabel(r'$S^2 = \langle (x_N)^2 \rangle$')
plt.grid(True)
plt.legend()
plt.show()
