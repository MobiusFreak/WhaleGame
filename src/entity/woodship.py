import pygame, math
from pygame.locals import *

from ship import Ship
from projectile import *


class WoodShip(Ship):
    img = None

    def __init__(self, *args, **kargs):
        if not WoodShip.img:
            WoodShip.img = pygame.image.load("../media/shitp.png").convert_alpha()


        Ship.__init__(self, WoodShip.img, projectile = Harpoon, health = 40, *args, **kargs)
