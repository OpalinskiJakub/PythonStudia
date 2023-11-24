

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self): 
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"        

    def __eq__(self, other): 
        return self.x==other.x and self.y==other.y

    def __ne__(self, other):   
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other): 
        return Point(self.x+other.x,self.y+other.y)

    def __sub__(self, other):
        return Point(self.x-other.x,self.y-other.y)

    def __mul__(self, other): 
        return self.x * other.x + self.y * other.y

    def cross(self, other):        
        return self.x * other.y - self.y * other.x

    def length(self): 
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.point1 = Point(2, 3)
        self.point2 = Point(2, 3)
        self.point3 = Point(4, 5)



    def test_addition(self):
        self.assertEqual(self.point1 + self.point3, Point(6, 8))
        self.assertEqual(self.point1 + self.point2, Point(4, 6))
        self.assertEqual(self.point3 + self.point2, Point(6, 8))

    def test_subtraction(self):
        self.assertEqual(self.point3 - self.point1, Point(2, 2))
        self.assertEqual(self.point3 - self.point2, Point(2, 2))
        self.assertEqual(self.point1 - self.point2, Point(0, 0))

    def test_multiplication(self):
        self.assertEqual(self.point1 * self.point3, 23)
        self.assertEqual(self.point1 * self.point2, 13)
       

    def test_cross_product(self):
        self.assertEqual(self.point1.cross(self.point3), -2)
        self.assertEqual(self.point1.cross(self.point2), 0)
        self.assertEqual(self.point3.cross(self.point2), 2)

    def test_length(self):
        self.assertAlmostEqual(self.point1.length(), 3.60555127546, places=10)
        self.assertAlmostEqual(self.point3.length(), 6.40312423743, places=10)
        self.assertAlmostEqual(Point(0, 0).length(), 0, places=10)

    def test_hash(self):
        self.assertEqual(hash(self.point1), hash(self.point2))
        self.assertNotEqual(hash(self.point1), hash(self.point3))
        self.assertEqual(hash(self.point2), hash(Point(2, 3)))
        
if __name__ == '__main__':
    unittest.main()