import pygame, math
from pygame.locals import *


class Modifier(object):
    def __init__(self):
        pass

    def init(self, entity):
        pass

    def update(self, t, entity):
        pass

    def clear(self, entity):
        pass


class SpeedModifier(Modifier):
    def __init__(self, speed = 1):
        self.speed = speed

    def update(self, t, entity):
        entity.pos += entity.speed * self.speed

