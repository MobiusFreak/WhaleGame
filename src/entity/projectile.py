import pygame
from pygame.locals import *

from entity import Entity
import app

# TODO: ajustar el vector direccion al vector velocidad
class Projectile(Entity):
    def __init__(self, Surface, pos = (0,0), direction = (0,0),
                 speed = (0,0), density = 1, friction = 0.2, damage = 10,
                 shooter = None):

        self.damage = damage
        self.shooter = shooter
        Entity.__init__(self, Surface, pos = pos, direction = direction,
                        speed = speed, density = density, friction = 0.2)


class Harpoon(Projectile):
    def __init__(self, *args, **kargs):
        img = pygame.image.load("../media/harpoon.png").convert_alpha()
        Projectile.__init__(self, img, *args, **kargs)



def shoot(shooter, Projectile, pos, direction, speed = 1):
    direction.module = 1
    pos += direction

    ent = Projectile(pos = pos, direction = direction,
                     speed = direction * speed, shooter = shooter)
    game = app.get_current_game()
    game.projectiles.add(ent)

