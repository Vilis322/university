import logging
import math

logging.basicConfig(
    filename='errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def coordinates():
    points = 0
    num_of_points: int = 0
    list_of_points = []

    while num_of_points == 0:
        try:
            num_of_points = int(input("PLease enter how many points you have (the program expects an integer): "))
        except ValueError as e:
            print("An invalid input for count of points. Please try again.")
            logging.error(f"Invalid input: {e}")

    while points != num_of_points:
        x_coordinate = input(f"Enter x coordinate for point {points + 1}: ").strip()
        y_coordinate = input(f"Enter y coordinate for point {points + 1}: ").strip()
        try:
            x_coordinate = float(x_coordinate)
            y_coordinate = float(y_coordinate)
            list_of_points.append((x_coordinate, y_coordinate))
            points += 1
        except ValueError as e:
            print("Invalid input. The program expects from you an integer or float number! Please try again.")
            logging.error(f"Invalid input: {e}")

    return list_of_points


def distance(list_of_points):
    minimal_distance = float('inf')
    closest_points = None
    calculate_distance = lambda point1, point2: math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

    for i in range(len(list_of_points)):
        for j in range(i + 1, len(list_of_points)):
            point1, point2 = list_of_points[i], list_of_points[j]
            distance = calculate_distance(point1, point2)
            if distance < minimal_distance:
                minimal_distance = distance
                closest_points = (i+1, j+1)

    return closest_points


def main():
    list_of_points = coordinates()
    closest_points = distance(list_of_points)
    print(f"Points {closest_points[0]} and {closest_points[1]} are the closest to each other.")


if __name__ == "__main__":
    main()
