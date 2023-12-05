from rectangles import Rectangle
from points import Point
import pytest 

def test_from_points():
    point1 = (0, 0)
    point2 = (3, 4)
    rectangle = Rectangle.from_points((point1, point2))
    assert rectangle == Rectangle(0, 0, 3, 4)

def test_properties():
    rectangle = Rectangle(1, 2, 5, 7)
    assert rectangle.top == 7
    assert rectangle.left == 1
    assert rectangle.bottom == 2
    assert rectangle.right == 5
    assert rectangle.width == 4
    assert rectangle.height == 5
    assert rectangle.topleft == Point(1, 7)
    assert rectangle.bottomleft == Point(1, 2)
    assert rectangle.topright == Point(5, 7)
    assert rectangle.bottomright == Point(5, 2)


