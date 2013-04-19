import pygame, math
from pygame.locals import *

from entity import *

class Ship(Entity):
    def __init__(self, size = [90,90], pos = Vector(0,0), acc = 2):
        ship = pygame.image.load("../media/shitp.png").convert_alpha()
        self.ship_img = pygame.transform.smoothscale(ship,size)

        Entity.__init__(self, self.ship_img, pos)
        self.rect.inflate_ip(-10,-20)
