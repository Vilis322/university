class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height

    def __str__(self):
        return f"Rectangle area equals {self.area}, width equals {self.width}, height equals {self.height}."


if __name__ == "__main__":

    rectangle_one = Rectangle(4, 5)
    print(rectangle_one)

    rectangle_two = Rectangle(3, 4)
    print(rectangle_two)

    rectangle_three = Rectangle(3.5, 4.5)
    print(rectangle_three)

    the_big_one_rectangle = Rectangle(1000, 100000)
    print(the_big_one_rectangle)
