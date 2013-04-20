import pygame, math
from pygame.locals import *

from modifier_entity import *
from ship import Ship
from projectile import *
from random import randrange
import app

class WoodShip(Ship):
    img = None

    def __init__(self, *args, **kargs):
        if not WoodShip.img:
            WoodShip.img = pygame.image.load("../media/shitp.png").convert_alpha()


        Ship.__init__(self, WoodShip.img, projectile = Harpoon, health = 40, *args, **kargs)

    def die(self):
        game = app.get_current_game()
        num = randrange(0,1)
        if num > 0.3:
            ent = HealModifierEntity(pos = self.pos)
            game.modifiers.add(ent)

        Ship.die(self)
