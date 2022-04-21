import math


class Circle():
    def __init__(self, radius) -> None:
        self.radius = radius
        self.count_surface_area()
        self.count_perimeter()

    def count_surface_area(self):
        self.surface_area = math.pi * (self.radius**2)
        pass

    def count_perimeter(self):
        self.perimeter = 2 * self.radius * math.pi
        pass

    def print_surface_area(self):
        print(self.__class__.__name__, ":", "%3.2f" % self.surface_area, "m^2")
        print("%3.2f" % self.perimeter, "m")
        pass


class Squares(Circle):
    def __init__(self, side_a) -> None:
        self.side_a = side_a
        self.count_surface_area()
        self.count_perimeter()
        pass

    def count_surface_area(self):
        self.surface_area = self.side_a * self.side_a
        pass

    def count_perimeter(self):
        self.perimeter = 4 * self.side_a
        pass


class Rectangle(Squares):
    def __init__(self, side_a, side_b) -> None:
        self.side_a = side_a
        self.side_b = side_b
        self.count_surface_area()
        self.count_perimeter()
        pass

    def count_surface_area(self):
        self.surface_area = self.side_a * self.side_b
        pass

    def count_perimeter(self):
        self.perimeter = 2 * self.side_a * 2 * self.side_b
        pass


class RightTriangle(Circle):
    def __init__(self, side_a, side_h) -> None:
        self.side_a = side_a
        self.side_h = side_h
        self.count_surface_area()
        self.count_perimeter()
        pass

    def count_surface_area(self):
        self.surface_area = self.side_a * self.side_h / 2
        pass

    def count_perimeter(self):
        if self.side_a == self.side_h:
            self.perimeter = self.side_a + \
                self.side_a + (self.side_a * math.sqrt(2))
        else:
            self.side_c = math.sqrt(
                self.side_a*self.side_a + self.side_h*self.side_h)
            self.perimeter = self.side_c + self.side_a + self.side_h
        pass


x1 = Circle(2)
x1.print_surface_area()

x2 = Squares(2)
x2.print_surface_area()

x3 = Rectangle(2, 3)
x3.print_surface_area()

x4 = RightTriangle(2, 3)
x4.print_surface_area()
