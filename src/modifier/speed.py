import pygame, math
from pygame.locals import *

from modifier import Modifier

class SpeedModifier(Modifier):
    def __init__(self, speed = 1):
        self.speed = speed

    def update(self, t, entity):
        entity.pos += entity.speed * self.speed

