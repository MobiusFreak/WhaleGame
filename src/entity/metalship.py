import pygame, math
from pygame.locals import *

from ship import Ship


class MetalShip(Ship):
    img = None

    def __init__(self, pos = (0,0)):
        if not self.__class__.img:
            self.__class__.img = pygame.image.load("../media/shitp_metal.png").convert_alpha()

        Ship.__init__(self, self.__class__.img, projectile = Harpoon, health = 40, *args, **kargs)

