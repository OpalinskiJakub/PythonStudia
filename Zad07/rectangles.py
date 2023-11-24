from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self): pass         # "[(x1, y1), (x2, y2)]"

    def __repr__(self): pass        # "Rectangle(x1, y1, x2, y2)"

    def __eq__(self, other): pass   # obsługa rect1 == rect2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self): pass          # zwraca środek prostokąta

    def area(self): pass            # pole powierzchni

    def move(self, x, y): pass      # przesunięcie o (x, y)

    def intersection(self, other): pass # część wspólna prostokątów

    def cover(self, other): pass    # prostąkąt nakrywający oba

    def make4(self): pass           # zwraca krotkę czterech mniejszych
# A-------B   po podziale  A---+---B
# |       |                |   |   |
# |       |                +---+---+
# |       |                |   |   |
# D-------C                D---+---C

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase): pass