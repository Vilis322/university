from pathlib import Path


def get_fahrenheit_list(file):
    fahrenheit_list = []
    text = Path(file).read_text()

    for value in text.splitlines():
        if value.isnumeric():
            fahrenheit = float(value) * 1.8 + 32
            fahrenheit_list.append(fahrenheit)

    return fahrenheit_list


def main():
    fahrenheit_list = get_fahrenheit_list("temps.txt")

    if fahrenheit_list:
        average_value = sum(fahrenheit_list) / len(fahrenheit_list)
        min_value = min(fahrenheit_list)
        max_value = max(fahrenheit_list)
        print(f"The average is {average_value}.\nThe minimum is {min_value}.\nThe maximum is {max_value}")
        return


if __name__ == "__main__":
    main()
