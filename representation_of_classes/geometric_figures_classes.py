# to do
# make classes for  triangles

from cmath import pi


class Circle():
    def __init__(self, radius) -> None:
        self.radius = radius
        self.count_surface_area()

    def count_surface_area(self):
        self.surface_area = pi * (self.radius**2)
        pass

    def print_surface_area(self):
        print(self.__class__.__name__, ":", self.surface_area, "m^2")
        pass


class Squares(Circle):
    def __init__(self, side_a) -> None:
        self.side_a = side_a
        self.count_surface_area()
        pass

    def count_surface_area(self):
        self.surface_area = self.side_a * self.side_a
        pass


class Rectangle(Squares):
    def __init__(self, side_a, side_b) -> None:
        self.side_a = side_a
        self.side_b = side_b
        self.count_surface_area()
        pass

    def count_surface_area(self):
        self.surface_area = self.side_a * self.side_b
        pass


class Triangle(Circle):
    def __init__(self, side_a, side_h) -> None:
        self.side_a = side_a
        self.side_h = side_h
        self.count_surface_area()
        pass

    def count_surface_area(self):
        self.surface_area = self.side_a * self.side_h / 2
        pass


x1 = Circle(2)
x1.print_surface_area()

x2 = Squares(2)
x2.print_surface_area()

x3 = Rectangle(2, 3)
x3.print_surface_area()

x4 = Triangle(2, 3)
x4.print_surface_area()
