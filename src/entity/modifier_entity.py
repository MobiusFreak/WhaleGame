import pygame
from pygame.locals import *

from modifier import SpeedModifier
from entity import Entity

class ModifierEntity(Entity):
    def __init__(self, pos = (0,0), modifier = SpeedModifier()):
        img = pygame.surface.Surface((40,40), SRCALPHA)
        pygame.draw.circle(img, (255,0,0), (20,20), 20)
        pygame.draw.circle(img, (200,0,0), (20,20), 10)
        pygame.draw.circle(img, (0,0,0), (20,20), 20, 2)
        ent = Entity.__init__(self, img, pos)

        self.modifier = modifier
