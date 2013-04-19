import pygame
from pygame.locals import *


from entity import Entity


class Ball(Entity):
    def __init__(self, color = (255,0,0), pos = (0,0)):
        img = pygame.surface.Surface((40,40), SRCALPHA)
        pygame.draw.circle(img, color, (20,20), 20)
        pygame.draw.circle(img, (0,0,0), (20,20), 20, 2)
        ent = Entity.__init__(self, img, pos)
