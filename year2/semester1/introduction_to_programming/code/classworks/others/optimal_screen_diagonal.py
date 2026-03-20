def screen_diagonal(distance):
    diagonal = float(distance) * 100 * 0.39 / 2.5
    return round(diagonal)


user_distance = input("Write the distance from the screen to the eyes:\n")

try:
    result = screen_diagonal(user_distance)
    print(f"Screen diagonal is {result}.")
except ValueError:
    print("You wrote a wrong things!")
