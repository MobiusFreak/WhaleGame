import pygame
from pygame.locals import *

from modifier import SpeedModifier
from entity import Entity

class ModifierEntity(Entity):
    img = None

    def __init__(self, pos = (0,0), modifier = SpeedModifier()):
        if not ModifierEntity.img:
            ModifierEntity.img = pygame.image.load("../media/modifier_speed.png").convert_alpha()

        ent = Entity.__init__(self, ModifierEntity.img, pos)

        self.modifier = modifier
