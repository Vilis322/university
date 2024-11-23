
def celsius_to_fahrenheit():
    celsius = input("Enter temperature in Celsius: ")
    celsius = float(celsius)
    fahrenheit = celsius * 1.8 + 32

    return str(f"Temperature in fahrenheit is {fahrenheit}")


print(celsius_to_fahrenheit())
    