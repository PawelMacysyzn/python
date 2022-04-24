from abc import ABC, abstractmethod
import math


class Figure(ABC):
    def print_figure(self):
        arg_1 = self.__class__.__name__
        arg_2 = ": {:.2f} m^2" .format(self.surface_area())
        arg_3 = ", {:.2f} m" .format(self.perimeter())
        arg_4 = " [surf., perimeter]"
        print(arg_1, arg_2, arg_3, arg_4)

    @abstractmethod
    def surface_area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Figure):
    def __init__(self, radius) -> None:
        self.radius = radius

    def surface_area(self):
        return math.pi * (self.radius**2)

    def perimeter(self):
        return 2 * self.radius * math.pi


class Squares(Figure):
    def __init__(self, side_a) -> None:
        self.side_a = side_a

    def surface_area(self):
        return self.side_a * self.side_a

    def perimeter(self):
        return 4 * self.side_a


class Rectangle(Squares):
    def __init__(self, side_a, side_b) -> None:
        super().__init__(side_a)
        self.side_b = side_b

    def surface_area(self):
        return self.side_a * self.side_b

    def perimeter(self):
        return 2 * self.side_a + 2 * self.side_b


class RightTriangle(Squares):
    def __init__(self, side_a, side_h) -> None:
        super().__init__(side_a)
        self.side_h = side_h

    def surface_area(self):
        return self.side_a * self.side_h / 2

    def perimeter(self):
        if self.side_a == self.side_h:
            return self.side_a + \
                self.side_a + (self.side_a * math.sqrt(2))
        else:
            self.side_c = math.sqrt(
                self.side_a*self.side_a + self.side_h*self.side_h)
            return self.side_c + self.side_a + self.side_h


def sum_surface_areas(list_of_figures):
    sum = 0
    for figure in list_of_figures:
        sum += figure.surface_area()
    print("Sum of all surface areas: {:.2f} m^2" .format(sum))


def sum_perimeters(list_of_figures):
    sum = 0
    for figure in list_of_figures:
        sum += figure.perimeter()
    print("Sum of all perimeters: {:.2f} m" .format(sum))


x1 = Circle(10)
x1.print_figure()

x2 = Squares(10)
x2.print_figure()

x3 = Rectangle(10, 5)
x3.print_figure()

x4 = RightTriangle(10, 5)
x4.print_figure()

list_of_figures = [x1, x2, x3, x4]

sum_surface_areas(list_of_figures)
sum_perimeters(list_of_figures)
