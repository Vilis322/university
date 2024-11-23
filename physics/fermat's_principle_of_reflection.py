import math


def calculate_path_between_points(point_from, point_to):
    x_point_from, y_point_from = point_from
    x_point_to, y_point_to = point_to
    return math.sqrt((x_point_to - x_point_from)**2 + (y_point_to - y_point_from)**2)


def calculate_path_distance(distance_before_reflection, distance_after_reflection):
    return distance_before_reflection + distance_after_reflection


def search_reflected_point(point_b, point_c):
    x_point_b, y_point_b = point_b
    x_point_c, y_point_c = point_c

    return x_point_b, 2 * y_point_c - y_point_b


def get_fermat_principle(distance_between_default_points, distance_between_default_and_reflected_points):
    return distance_between_default_points <= distance_between_default_and_reflected_points


def user_input(input_message):
    return float(input(input_message))


def main():
    x_coordinate_for_point_a = user_input("Введите координату х для точки А: ")
    y_coordinate_for_point_a = user_input("Введите координату у для точки А: ")
    x_coordinate_for_point_b = user_input("Введите координату х для точки В: ")
    y_coordinate_for_point_b = user_input("Введите координату у для точки В: ")
    x_coordinate_for_point_c = user_input("Введите координату х для точки С: ")
    y_coordinate_for_point_c = user_input("Введите координату у для точки С: ")

    point_a = (x_coordinate_for_point_a, y_coordinate_for_point_a)
    point_b = (x_coordinate_for_point_b, y_coordinate_for_point_b)
    point_c = (x_coordinate_for_point_c, y_coordinate_for_point_c)
    reflected_b = search_reflected_point(point_b, point_c)

    path_from_a_to_c = calculate_path_between_points(point_a, point_c)
    path_from_c_to_b = calculate_path_between_points(point_c, point_b)
    path_from_a_to_reflected_b = calculate_path_between_points(point_a, reflected_b)

    path_from_a_to_b_through_c = calculate_path_distance(path_from_a_to_c, path_from_c_to_b)
    path_from_a_to_c_through_reflected_b = calculate_path_distance(path_from_a_to_c, path_from_a_to_reflected_b)

    if get_fermat_principle(path_from_a_to_b_through_c, path_from_a_to_c_through_reflected_b):
        print("Принцип Ферма работает.")
    else:
        print("Принцип Ферма не работает.")


if __name__ == "__main__":
    main()
