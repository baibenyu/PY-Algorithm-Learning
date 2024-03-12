import math


class Point:
    coordinates = []

    def set_coordinates(self, x, y):
        self.coordinates = [x, y]

        return self.coordinates


class Line():

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_len(self):
        self.length = math.sqrt((self.start[0] - self.end[0]) ** 2 + (self.start[1] - self.end[1]) ** 2)
        return self.length


p1 = Point()
p2 = Point()
line = Line(p1.set_coordinates(2, 5), p2.set_coordinates(4, 9))
print(line.get_len())
