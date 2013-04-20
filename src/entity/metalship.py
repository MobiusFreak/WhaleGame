import pygame, math
from pygame.locals import *

from projectile import Harpoon
from ship import Ship


class MetalShip(Ship):
    img = None

    def __init__(self, *args, **kargs):
        if not MetalShip.img:
            MetalShip.img = pygame.image.load("../media/shitp_metal.png").convert_alpha()

        Ship.__init__(self, MetalShip.img, score = 50, projectile = Harpoon, health = 100, *args, **kargs)

