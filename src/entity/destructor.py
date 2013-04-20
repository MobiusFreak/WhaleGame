import pygame, math
from pygame.locals import *

from ship import Ship
from projectile import *
from random import randrange
from modifier_entity import *
import app


class Destructor(Ship):
    img = None

    def __init__(self, *args, **kargs):
        if not Destructor.img:
            Destructor.img = pygame.image.load("../media/destructor.png").convert_alpha()


        Ship.__init__(self, Destructor.img, *args, score = 200,
                      projectile = Missile, health = 200,
                      density = 0.85, **kargs)


    def die(self):
        game = app.get_current_game()
        num = randrange(0,1)
        if num > 0.9:
            ent = SpeedModifierEntity(pos = self.pos)
            game.modifiers.add(ent)

        Ship.die(self)
