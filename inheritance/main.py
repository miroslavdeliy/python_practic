import math
from abc import ABC, abstractmethod

#Абстрактный класс
class Share(ABC):

    @abstractmethod
    def area(self):
        pass


#Прямоугольник
class Rectangle(Share):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area (self):
        return self.height * self.width


#Круг
class Circle(Share):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


#Основное тело программы
share_rectangle = Rectangle(10, 50)
share_circle = Circle(10)

print(f"Площадь прямоугольника {share_rectangle.area()}")
print(f"Площадь круга {share_circle.area()}")