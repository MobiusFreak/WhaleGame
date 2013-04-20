import pygame, math
from pygame.locals import *

from ship import Ship
from projectile import *


class Destructor(Ship):
    img = None

    def __init__(self, *args, **kargs):
        if not Destructor.img:
            Destructor.img = pygame.image.load("../media/destructor.png").convert_alpha()


        Ship.__init__(self, Destructor.img, *args, score = 200,
                      projectile = Missile, health = 300,
                      density = 0.85, **kargs)

