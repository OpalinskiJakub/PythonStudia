from points import Point

from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Invalid rectangle coordinates: x1 < x2 and y1 < y2 must hold.")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    @classmethod
    def from_points(cls, points):
        x1, y1 = points[0]
        x2, y2 = points[1]
        return cls(x1, y1, x2, y2)

    @property
    def top(self):
        return self.pt2.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def right(self):
        return self.pt2.x

    @property
    def width(self):
        return abs(self.pt2.x - self.pt1.x)

    @property
    def height(self):
        return abs(self.pt2.y - self.pt1.y)

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

    @property
    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def __str__(self):
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
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
            return None 
        return Rectangle(x1, y1, x2, y2)
        

    def cover(self, other):
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)
        

    def make4(self):
        center = self.center
        return (
            Rectangle(self.pt1.x, self.pt1.y, center.x, center.y),
            Rectangle(center.x, self.pt1.y, self.pt2.x, center.y),
            Rectangle(self.pt1.x, center.y, center.x, self.pt2.y),
            Rectangle(center.x, center.y, self.pt2.x, self.pt2.y)
        )
