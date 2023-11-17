
from points import Point

class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self): 
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y}), ({self.pt3.x}, {self.pt3.y})]"

    def __repr__(self): 
        return f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})"

    def __eq__(self, other): 
         return {self.pt1, self.pt2, self.pt3} == {other.pt1, other.pt2, other.pt3}

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self): 
        return Point((self.pt1.x + self.pt2.x + self.pt3.x) / 3, (self.pt1.y + self.pt2.y + self.pt3.y) / 3)

    def area(self): 
         return 0.5 * abs((self.pt2.x - self.pt1.x) * (self.pt3.y - self.pt1.y) - (self.pt3.x - self.pt1.x) * (self.pt2.y - self.pt1.y))

    def move(self, x, y):
        self.pt1.x += x
        self.pt2.x += x
        self.pt3.x += x
        self.pt1.y += y
        self.pt2.y += y
        self.pt3.y += y


# Kod testujący moduł.

import unittest

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.triangle1 = Triangle(0, 0, 3, 0, 0, 4)
        self.triangle2 = Triangle(0, 4, 3, 0, 0, 0)
        self.triangle3 = Triangle(1, 1, 4, 1, 1, 5)

    def test_str_representation(self):
        self.assertEqual(str(self.triangle1), "[(0, 0), (3, 0), (0, 4)]")
        self.assertEqual(str(self.triangle3), "[(1, 1), (4, 1), (1, 5)]")

    def test_repr_representation(self):
        self.assertEqual(repr(self.triangle1), "Triangle(0, 0, 3, 0, 0, 4)")
        self.assertEqual(repr(self.triangle3), "Triangle(1, 1, 4, 1, 1, 5)")

    def test_equality(self):
        self.assertEqual(self.triangle1, self.triangle2)
        self.assertNotEqual(self.triangle1, self.triangle3)
        self.assertEqual(self.triangle2, Triangle(0, 0, 3, 0, 0, 4))

    def test_center(self):
        self.assertEqual(self.triangle1.center(), Point(1, 1.3333333333333333))
        self.assertEqual(self.triangle3.center(), Point(2, 2.3333333333333335))

    def test_area(self):
        self.assertAlmostEqual(self.triangle1.area(), 6, places=10)
        self.assertAlmostEqual(self.triangle3.area(), 6, places=10)
        self.assertAlmostEqual(self.triangle2.area(), 6, places=10)

    def test_move(self):
        self.triangle1.move(1, 1)
        self.assertEqual(self.triangle1, Triangle(1, 1, 4, 1, 1, 5))
        self.triangle3.move(-1, -1)
        self.assertEqual(self.triangle3, Triangle(0, 0, 3, 0, 0, 4))

if __name__ == '__main__':
    unittest.main()

