import math


class Vector(object):
    def __init__(self, arg1=0, arg2=0):
        if isinstance(arg1, tuple):
            self.x, self.y = arg1
        elif isinstance(arg1, Vector):
            self.x = arg1.x
            self.y = arg1.y
        else:
            self.x = arg1
            self.y = arg2

        x = self.x
        y = self.y
        self.__module = math.sqrt(x**2 + y**2)
        self.__angle = math.atan2(y,x)

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

    def __neg__(self):
        return -1 * self

    def get_module(self):
        return self.__module

    def set_module(self, mod):
        self.__module = mod
        self.x = mod * math.cos(self.__angle)
        self.y = mod * math.sin(self.__angle)

    def get_angle(self):
        return math.degrees((math.atan2(self.y, self.x)%\
                             (2*math.pi)))

    def set_angle(self, angle):
        angle = math.radians(angle)
        self.__angle = angle
        self.x = self.__module * math.cos(angle)
        self.y = self.__module * math.sin(angle)

    def __getattr__(self, name):
        if name == "angle":
            return self.get_angle()
        elif name == "module":
            return self.get_module()
        else:
            raise AttributeError

    def __setattr__(self, name, value):
        if name == "angle":
            return self.set_angle(value)
        elif name == "module":
            return self.set_module(value)
        else:
            object.__setattr__(self, name, value)


    def __getitem__(self, i):
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
        else:
            raise IndexError


