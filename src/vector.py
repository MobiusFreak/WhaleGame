import math


class Vector(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.module = math.sqrt(x**2 + y**2)
        self.angle = math.atan2(y,x)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector):
            return NotImplemented
        else:
            return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __repr__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"

    def get_module(self):
        return math.sqrt(self.x**2 + self.y**2)

    def set_module(self, mod):
        self.module = mod
        self.x = mod * math.cos(self.angle)
        self.y = mod * math.sin(self.angle)

    def get_angle(self):
        return math.degrees((math.atan2(self.y, self.x)%\
                                 (2*math.pi)))

    def set_angle(self, angle):
        angle = math.radians(angle)
        self.angle = angle
        self.x = self.module * math.cos(angle)
        self.y = self.module * math.sin(angle)

    def __getitem__(self, i):
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
        else:
            raise IndexError


