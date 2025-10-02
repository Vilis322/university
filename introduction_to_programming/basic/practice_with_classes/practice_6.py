class Engine:
    def __init__(self, max_power, type_of_fuel):
        self.max_power = max_power
        self.type_of_fuel = type_of_fuel


class CarBody:
    def __init__(self, type_of_body, count_doors):
        self.type_of_body = type_of_body
        self.count_doors = count_doors


class Wheel:
    def __init__(self, diameter, type_of_rubber):
        self.diameter = diameter
        self.type_of_rubber = type_of_rubber


class Car:
    def __init__(self, engine, car_body, wheel, brand):
        self.engine = engine
        self.car_body = car_body
        self.wheel = wheel
        self.brand = brand

    def display_engine_info(self):
        return f"Max power engine`s: {self.engine.max_power} HP.\nType of fuel: {self.engine.type_of_fuel}.\n"

    def display_car_body_info(self):
        return f"Type of body: {self.car_body.type_of_body}\nAmount doors: {self.car_body.count_doors}\n"

    def display_wheel_info(self):
        return f"Diameter: {self.wheel.diameter}\nType of rubber: {self.wheel.type_of_rubber}\n"

    def __str__(self):
        return f"Car: {self.brand}\n{self.display_engine_info()}{self.display_car_body_info()}{self.display_wheel_info()}"


if __name__ == "__main__":
    bmw_engine = Engine(400, "diesel")
    bmw_car_body = CarBody("sedan", 4)
    bmw_wheel = Wheel(25, "summer rubber")
    bmw = Car(bmw_engine, bmw_car_body, bmw_wheel, "BMW")
    print(bmw)

    subaru_engine = Engine(340, "gasoline")
    subaru_car_body = CarBody("sedan", 4)
    subaru_wheel = Wheel(24, "summer rubber")
    subaru = Car(subaru_engine, subaru_car_body, subaru_wheel, "Subaru")
    print(subaru)
