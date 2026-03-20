class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"Name of product is {self.name}\nPrice for this product is {self.price}\n"

    def __str__(self):
        return self.get_info()


class Product(Item):
    def __init__(self, name, price, brand, category):
        super().__init__(name, price)
        self.brand = brand
        self.category = category

    def get_brand_and_category(self):
        return f"Brand of this product is {self.brand}\nCategory of this product is {self.category}\n"

    def __str__(self):
        return self.get_brand_and_category()


class Food(Product):
    def __init__(self, name, price, brand, category, expiry_date, weight):
        super().__init__(name, price, brand, category)
        self.expiry_date = expiry_date
        self.weight = weight

    def get_expiry_date_and_weight(self):
        return f"Expiry date of this product is {self.expiry_date}\nWeight of this product is {self.weight}"

    def __str__(self):
        return self.get_expiry_date_and_weight()


class Beverage(Product):
    def __init__(self, name, price, brand, category, volume, carbonated):
        super().__init__(name, price, brand, category)
        self.volume = volume
        self.carbonated = carbonated

    def is_carbonated(self):
        return "Beverage is carbonated" if self.carbonated is True else "Beverage is not carbonated"

    def __str__(self):
        return f"{self.is_carbonated()}\nVolume of beverage is {self.volume}\n"


if __name__ == "__main__":

    food1 = Food("Banana", 1.99, "Chiquita", "Fruit", "2023-01-31", 150)
    food2 = Food("Cheese", 4.99, "Kraft", "Dairy", "2022-12-15", 250)

    beverage1 = Beverage("Coca Cola", 2.49, "Coca Cola Company", "Soft Drink", 500, True)
    beverage2 = Beverage("Water", 0.99, "Aquafina", "Bottled Water", 1000, False)

    print(food1.get_info())
    print(food1.get_brand_and_category())
    print(food1)

    print(beverage2.get_info())
    print(beverage2.get_brand_and_category())
    print(beverage2)
