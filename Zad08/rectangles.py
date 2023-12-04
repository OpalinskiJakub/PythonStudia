from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Invalid rectangle coordinates: x1 < x2 and y1 < y2 must hold.")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self): 
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"


    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other): 
        if not isinstance(other, Rectangle):
            return False
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self): 
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self): 
        return abs(self.pt1.x - self.pt2.x) * abs(self.pt1.y - self.pt2.y)

    def move(self, x, y): 
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)

    def intersection(self, other): 
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)
        if x1 >= x2 or y1 >= y2:
            return None  # Brak części wspólnej
        return Rectangle(x1, y1, x2, y2)
        # część wspólna prostokątów

    def cover(self, other): 
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)
        # prostąkąt nakrywający oba

    def make4(self): 
        center = self.center()
        return (
            Rectangle(self.pt1.x, self.pt1.y, center.x, center.y),
            Rectangle(center.x, self.pt1.y, self.pt2.x, center.y),
            Rectangle(self.pt1.x, center.y, center.x, self.pt2.y),
            Rectangle(center.x, center.y, self.pt2.x, self.pt2.y)
        )

        # zwraca krotkę czterech mniejszych
# A-------B   po podziale  A---+---B
# |       |                |   |   |
# |       |                +---+---+
# |       |                |   |   |
# D-------C                D---+---C

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect1 = Rectangle(1, 1, 3, 3)
        self.rect2 = Rectangle(2, 2, 4, 4)
        self.rect3 = Rectangle(5, 5, 7, 7)
        self.rect4 = Rectangle(2, 2, 6, 6)
        self.rect5 = Rectangle(1, 1, 3, 3)

    def test_init_valid_rectangle(self):
        self.assertIsInstance(self.rect1, Rectangle)

    def test_init_invalid_rectangle(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(3, 3, 1, 1)

    def test_string_representation(self):
        self.assertEqual(str(self.rect1), "[(1, 1), (3, 3)]")

    def test_representation(self):
        self.assertEqual(repr(self.rect1), "Rectangle(1, 1, 3, 3)")

    def test_equality(self):
        self.assertNotEqual(self.rect1, self.rect2)
        self.assertNotEqual(self.rect1, self.rect3)
        self.assertEqual(self.rect1, self.rect5)

    def test_center(self):
        self.assertEqual(self.rect1.center(), Point(2.0, 2.0))

    def test_area(self):
        self.assertEqual(self.rect1.area(), 4)

    def test_move(self):
        moved_rect = self.rect1.move(1, 1)
        self.assertEqual(moved_rect, self.rect2)

    def test_intersection(self):
        self.assertIsNone(self.rect1.intersection(self.rect3))
        intersect_rect = self.rect2.intersection(self.rect4)
        self.assertEqual(intersect_rect, Rectangle(2, 2, 4, 4))

    def test_cover(self):
        cover_rect = self.rect1.cover(self.rect2)
        self.assertEqual(cover_rect, Rectangle(1, 1, 4, 4))

    def test_make4(self):
        rects = self.rect2.make4()
        self.assertEqual(rects, (
            Rectangle(2, 2, 3.0, 3.0),
            Rectangle(3.0, 2, 4, 3.0),
            Rectangle(2, 3.0, 3.0, 4),
            Rectangle(3.0, 3.0, 4, 4)
        ))

if __name__ == '__main__':
    unittest.main()