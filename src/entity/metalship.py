import pygame, math
from pygame.locals import *

from projectile import Harpoon
from ship import Ship
from modifier_entity import *
from random import random
import app

class MetalShip(Ship):
    img = None

    def __init__(self, *args, **kargs):
        if not MetalShip.img:
            MetalShip.img = pygame.image.load("../media/shitp_metal.png").convert_alpha()

        Ship.__init__(self, MetalShip.img, score = 35, projectile = Harpoon, health = 100, *args, **kargs)


    def die(self):
        game = app.get_current_game()
        num = random()
        if num > 0.8:
            ent = SpeedModifierEntity(pos = self.pos)
            game.modifiers.add(ent)

        Ship.die(self)
