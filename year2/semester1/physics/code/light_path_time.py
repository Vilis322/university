from scipy.constants import c
from scipy.optimize import minimize_scalar
import math


def light_speed_in_the_environment(index_of_refraction, light_speed_in_the_vacuum):
    return light_speed_in_the_vacuum / index_of_refraction


def time_function(x, a, b, l, v1, v2):
    return math.sqrt((a ** 2 + x ** 2) / v1) + math.sqrt((b ** 2 + (l - x) ** 2) / v2)


def find_optimal_x(a, b, l, v1, v2):
    return minimize_scalar(time_function, args=(a, b, l, v1, v2), bounds=(0, l), method='bounded')


def main():
    a_distance_in_meters = 50000
    b_distance_in_meters = 100000000
    l_distance_in_meters = 70000

    index_of_refraction_for_air = 1.0
    index_of_refraction_for_water = 1.3

    light_speed_in_the_air = light_speed_in_the_environment(index_of_refraction_for_air, c)
    light_speed_in_the_water = light_speed_in_the_environment(index_of_refraction_for_water, c)

    optimal_x = find_optimal_x(a_distance_in_meters, b_distance_in_meters, l_distance_in_meters, light_speed_in_the_air, light_speed_in_the_water).x
    light_path_time = time_function(optimal_x, a_distance_in_meters, b_distance_in_meters, l_distance_in_meters, light_speed_in_the_air, light_speed_in_the_water)

    print(f"Оптимальное время прохождения данного пути: {light_path_time/1000:.2} в секундах.")


if __name__ == '__main__':
    main()
