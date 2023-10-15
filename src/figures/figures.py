from math import pi, sqrt, isclose
from abc import ABC, abstractmethod


class Figure(ABC):
    """
    Abstract class represents one geometric figure.
    Class provides method that must implement each child
    class to work with specific geometric figure.
    """

    @abstractmethod
    def calculate_area(self) -> float:
        """
        Method to calculate area of geometric figure
        :return: area of geometric figure
        """
        pass


class Circle(Figure):
    """
    Class inherits from abstract class :class:`Figure` and represents one circle.

    Class implements abstract method to calculate area of a circle.
    In init method you can set radius of the circle.
    """

    def __init__(self, radius: float):
        """
        Init method creates circle class with specified radius.
        :param radius: radius of the circle
        """
        self.radius = radius

    def calculate_area(self) -> float:
        """
        Method to calculate area of the circle using it radius.
        :return: area of the circle
        """
        return pi * self.radius ** 2


class Triangle(Figure):
    """
    Class inherits from abstract class :class:`Figure` and represents one triangle.

    Class implements abstract method to calculate area of a triangle.
    Sides of triangle sets in init method.

    Class also provides method to check if the triangle is rectangular.
    """

    def __init__(self, sides: tuple[float, float, float]) -> None:
        """
        Init method takes 3 sides of triangle and creates class with specified sides.
        :param sides: sides of the triangle
        :raises TriangleCannotBeCreatedError: if triangle cannot be created with such sides
        """
        temp_sides = sorted(sides)
        if temp_sides[0] + temp_sides[1] <= temp_sides[2]:
            raise TriangleCannotBeCreatedError('Invalid side lengths')
        self.sides = sides

    def calculate_area(self) -> float:
        """
        Method to calculate area of the triangle using Heron's formula.
        :return: area of the triangle
        """
        half_perimeter = sum(self.sides) / 2
        return sqrt(half_perimeter * (half_perimeter - self.sides[0]) *
                    (half_perimeter - self.sides[1]) * (half_perimeter - self.sides[2]))

    def is_rectangular(self) -> bool:
        """
        Method to check if the triangle is rectangular using Pythagorean theorem.
        :return: True if triangle is rectangular and False otherwise
        """
        sorted_sides = sorted(self.sides)
        sum_of_2_sides = (sorted_sides[0] ** 2) + (sorted_sides[1] ** 2)
        return isclose(sum_of_2_sides, sorted_sides[2] ** 2)


class TriangleCannotBeCreatedError(BaseException):
    """
    The error is an exception that means the triangle cannot be created.
    """
    def __int__(self, message: str = ''):
        """
        Method calls the base exception init method with specified message
        :param message: details of error
        """
        super().__init__('Triangle cannot be created: ' + message)
