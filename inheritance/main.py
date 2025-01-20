import math
from abc import abstractmethod


class Share:
    @abstractmethod
    def area(self):
        pass

class Rectangle(Share):
    def area (self, heigh, width):
        return heigh * width

class Circle(Share):
    def area(self, radius):
        return math.pi * math.pow(radius, 2)


share_rectangle = Rectangle()
share_circle = Circle()
print(f"Площадь прямоугольника {share_rectangle.area(34, 65)}")
print(f"Площадь круга {share_circle.area(34)}")


