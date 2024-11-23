import numpy as np
import matplotlib.pyplot as plt
import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning)

# Константы
planck_constant = 6.626e-34
speed_of_light = 3e8
boltzmann_constant = 1.38e-23


def planck_spectral_radiance(frequency, temperature):
    with np.errstate(over='ignore'):
        return (2 * planck_constant * frequency ** 3) / (speed_of_light ** 2 * (np.exp((planck_constant * frequency) / (boltzmann_constant * temperature)) - 1))


frequency_min = 100
frequency_max = 2e15
frequency_values = np.linspace(frequency_min, frequency_max, 100)

temperature_values = [500, 1000, 1500, 2000, 2500]

max_emission_frequencies = []
integrated_areas = []

plt.figure(figsize=(10, 6))
for temp in temperature_values:
    radiance_values = planck_spectral_radiance(frequency_values, temp)
    plt.plot(frequency_values, radiance_values, label=f'T = {temp} K')

    max_index = np.argmax(radiance_values)
    max_emission_frequencies.append(frequency_values[max_index])

    area_under_curve = np.trapz(radiance_values, frequency_values)
    integrated_areas.append(area_under_curve)

plt.xlabel('Частота (Гц)')
plt.ylabel('Спектральная светимость (Вт/м²/Гц)')
plt.title('Спектральная светимость при разных температурах')
plt.legend()
plt.grid(True)
plt.show(block=False)

print("\nПроверка закона смещения Вина:")
wein_ratios = []

for temp, max_freq in zip(temperature_values, max_emission_frequencies):
    wein_ratio = temp / max_freq
    wein_ratios.append(wein_ratio)
    print(f'T = {temp} K, f_max = {max_freq:.2e} Гц, T/f_max = {wein_ratio:.2e}')

average_wein_ratio = np.mean(wein_ratios)

tolerance = 4e-12
all_within_tolerance = True

for ratio in wein_ratios:
    deviation = ratio - average_wein_ratio
    within_tolerance = abs(deviation) <= tolerance
    if not within_tolerance:
        all_within_tolerance = False
        break

if all_within_tolerance:
    print("Все значения T/f_max находятся в пределах допустимого отклонения.")
else:
    print("Некоторые значения T/f_max находятся вне допустимого отклонения.")

print("\nПроверка закона Стефана-Больцмана:")
for temp, area in zip(temperature_values, integrated_areas):
    print(f'T = {temp} K, Площадь под графиком = {area:.2e}, T^4 = {temp ** 4:.2e}')

temperature_power_4 = [temp ** 4 for temp in temperature_values]
plt.figure(figsize=(10, 6))
plt.plot(temperature_power_4, integrated_areas, 'o-', color='r')
plt.xlabel('Температура^4 (K^4)')
plt.ylabel('Суммарная энергия излучения (Площадь под графиком)')
plt.title('Зависимость суммарной энергии излучения от T^4')
plt.grid(True)
plt.show()
