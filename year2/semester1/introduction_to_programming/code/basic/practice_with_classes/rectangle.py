class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        rectangle_area = self.width * self.height
        return rectangle_area

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height

    def display_info(self):
        return f"Rectangle area equals {self.calculate_area()}, width equals {self.width}, height equals {self.height}."

    def __str__(self):
        return self.display_info()


if __name__ == "__main__":
    rectangle = Rectangle(4, 5)

    print(rectangle)

    rectangle.resize(3, 5)

    print(rectangle)
