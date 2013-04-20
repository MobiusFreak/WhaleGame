import pygame
from pygame.locals import *

from entity import Entity


# TODO: ajustar el vector direccion al vector velocidad
class Projectile(Entity):
    def __init__(self, Surface, pos = (0,0), direction = (0,0),
                 speed = (0,0), density = 1, friction = 0.2, damage = 10):

        self.damage = damage
        Entity.__init__(self, Surface, pos = pos, direction = direction,
                        speed = speed, density = density, friction = 0.2)


class Harpoon(Projectile):
    def __init__(self, pos = (0,0), direction = (0,0),
                 speed = (0,0)):

        img = pygame.image.load("../media/harpoon.png").convert_alpha()
        Projectile.__init__(self, img, pos = pos, direction = direction,
                            speed = speed)

