import math


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def describe(self):
        print(f"Shape: {self.name}  area: {self.area()}")


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"


shapes = [
    Rectangle(4, 5),
    Circle(3),
    Square(6)
]

for shape in shapes:
    shape.describe()

sq = Square(6)

print(isinstance(sq, Shape))
print(issubclass(Square, Shape))    