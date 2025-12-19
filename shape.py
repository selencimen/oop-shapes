# pylint: disable=too-few-public-methods missing-module-docstring
import math


class Shape:
    """
    Base (temel) class.
    Tüm şekillerin ortak özellikleri: name ve color
    """

    def __init__(self, color, name):
        # self.color ve self.name: objenin üzerinde saklanan attribute'lar
        self.color = color
        self.name = name

    def say_name(self):
        return f"My name is {self.name}."



class Rectangle(Shape):
    """
    Shape'ten miras alan dikdörtgen class'ı.
    Ek attribute'ları: width, height
    """

    def __init__(self, color, name, width, height):
        # Shape'in kurulumunu (name, color) super() ile yapıyoruz.
        super().__init__(color, name)
        self.width = width
        self.height = height

    def say_name(self):
        return f"My name is {self.name} and I am a rectangle."


    def area(self):
        # Dikdörtgen alanı = width * height
        return self.width * self.height

    def perimeter(self):
        # Dikdörtgen çevresi = 2 * (width + height)
        return 2 * (self.width + self.height)


class Circle(Shape):
    """
    Shape'ten miras alan daire class'ı.
    Ek attribute'ı: radius
    """

    def __init__(self, color, name, radius):
        super().__init__(color, name)
        self.radius = radius

    def say_name(self):
        return f"My name is {self.name} and I am a circle."


    def area(self):
        # Daire alanı = pi * r^2
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        # Daire çevresi = 2 * pi * r
        return 2 * math.pi * self.radius
