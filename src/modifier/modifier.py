import pygame, math
from pygame.locals import *

from entity import *
from utils.collisions import *

from entity import Harpoon, shoot

import app

class Modifier(object):
    def __init__(self):
        pass

    def init(self, entity):
        pass

    def update(self, t, entity):
        pass

    def clear(self, entity):
        pass


# TODO: bla bla bla
class SpeedModifier(Modifier):
    def __init__(self, speed = 1):
        self.speed = speed

    def update(self, t, entity):
        entity.pos += entity.speed * self.speed

class HealModifier(Modifier):
    def __init__(self, hp = 40):
        self.hp = hp

    def init(self, entity):
        entity.heal(self.hp)
