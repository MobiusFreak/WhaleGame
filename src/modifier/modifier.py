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



# Ship modifiers
class HarpoonModifier(Modifier):
    def init(self, entity):
        self.cooldown = 3000

    def update(self, t, ship):
        if self.cooldown > 0:
            self.cooldown -= t
        else:
            objective = ship.objective
            direction = objective.pos - ship.pos

            shoot(ship, Harpoon, ship.pos, direction)

            self.cooldown = 2000
