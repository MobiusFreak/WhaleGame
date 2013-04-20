import pygame, math
from pygame.locals import *

from entity import *

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
        self.cooldown = 0

    def update(self, t, ship):
        if self.cooldown > 0:
            self.cooldown -= t
        else:
            objective = ship.objective

            direction = objective.pos - ship.pos
            direction.module = 1

            # TODO: este cambio de coordenadas es una mierda
            img_direction = Vector(direction.x, -direction.y)

            ent = Harpoon(pos = ship.pos, direction = img_direction,
                          speed = direction * 5)

            game = app.get_current_game()
            game.projectiles.add(ent)

            self.cooldown = 2000
