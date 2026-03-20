from carsclass import Cars


car_one = Cars()
car_one.make = "BMW"
car_one.model = "X5"
car_one.year = 2019
car_one.features = []
car_one.features.extend(["Engine Type: Gas", "Transmission: 8-speed shiftable automatic", "Drive Type: all wheel drive",
                        "Cylinders	Inline: 6tk", "Total Seating: 5tk", "Basic Warranty: 4 yr./ 50,000 mi."])


car_two = Cars()
car_two.make = "Mercedes"
car_two.model = "AMG"
car_two.year = 2015
car_two.features = []
car_two.features.extend(["Twin power domes on the hood", "AMG-inspired cockpit with aluminum shift paddles",
                         "Rear diffuser", "Enlarged vents on the AMG Front Apron", "A wide stance and tires"])


car_three = Cars()
car_three.make = "Audi"
car_three.model = "A4"
car_three.year = 2022
car_three.features = []
car_three.features.extend(["A sunroof", "Three-zone climate control", "Heated front seats", "Leather upholstery",
                           "A 10.1-inch touchscreen", "Wireless Apple CarPlay", "Android Audio"])


cars = [car_one, car_two, car_three]

car_four = Cars()
car_four.make = "BMW"
car_four.model = "X6"
car_four.year = 2022
car_four.features = []

cars.append(car_four)

for car in cars:
    print(f"Make: {car.make}\nModel: {car.model}\nYear: {car.year}\nFeatures: ")
    for feature in car.features:
        print(f"- {feature}\n")
