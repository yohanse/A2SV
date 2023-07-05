import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

    def midpoint(self, other):
        mx = (self.x + other.x) / 2
        my = (self.y + other.y) / 2
        return Point(mx, my)

    def __str__(self):
        return "Point({}, {})".format(self.x, self.y)


# Usage:
p1 = Point(3, 4)
p2 = Point(6, 8)

print("Distance:", p1.distance(p2))
print("Midpoint:", p2.midpoint(p1))
