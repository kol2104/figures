from math import pi, isclose, sqrt
from figures import Circle, Triangle, TriangleCannotBeCreatedError
import pytest


def test_circle_area():
    radius = 10.2
    area = pi * radius ** 2
    circle = Circle(radius=radius)

    assert isclose(circle.calculate_area(), area)
    assert isclose(circle.radius, radius)


def test_triangle_area():
    sides = (3.0, 4.0, 6.0)
    half_perimeter = sum(sides) / 2
    area = sqrt(half_perimeter * (half_perimeter - sides[0]) *
                (half_perimeter - sides[1]) * (half_perimeter - sides[2]))
    triangle = Triangle(sides=sides)

    assert isclose(triangle.calculate_area(), area)
    for i in sides:
        assert i in triangle.sides


def test_triangle_error():
    with pytest.raises(TriangleCannotBeCreatedError) as exception:
        Triangle(sides=(3, 4, 10))  # sum of 2 sides must be greater than third side
    assert 'Invalid side lengths' in str(exception.value)


def test_triangle_is_rectangular():
    sides = (3.0, 4.0, 5.0)
    sum_of_2_sides = (sides[0] ** 2) + (sides[1] ** 2)
    is_rectangular = isclose(sum_of_2_sides, sides[2] ** 2)
    triangle = Triangle(sides=sides)

    assert is_rectangular == triangle.is_rectangular()
    for i in sides:
        assert i in triangle.sides


def test_triangle_not_ordered_sides():
    sides = (8.2, 4.4, 5.9)
    sum_of_2_sides = (sides[1] ** 2) + (sides[2] ** 2)
    is_rectangular = isclose(sum_of_2_sides, sides[0] ** 2)

    half_perimeter = sum(sides) / 2
    area = sqrt(half_perimeter * (half_perimeter - sides[0]) *
                (half_perimeter - sides[1]) * (half_perimeter - sides[2]))
    triangle = Triangle(sides=sides)

    assert is_rectangular == triangle.is_rectangular()
    assert isclose(triangle.calculate_area(), area)
    for i in sides:
        assert i in triangle.sides
