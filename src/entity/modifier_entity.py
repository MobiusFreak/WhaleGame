import pygame
from pygame.locals import *

from modifier import SpeedModifier, HealModifier
from entity import Entity

class ModifierEntity(Entity):
    def __init__(self, Surface, pos = (0,0), modifier = SpeedModifier()):
        ent = Entity.__init__(self, Surface, pos)

        self.modifier = modifier


class SpeedModifierEntity(ModifierEntity):
    img = None

    def __init__(self, pos = (0,0)):
        if not self.__class__.img:
            self.__class__.img = pygame.image.load("../media/modifier_speed.png").convert_alpha()

        ModifierEntity.__init__(self, self.__class__.img, pos, modifier = SpeedModifier())



class HealModifierEntity(ModifierEntity):
    img = None

    def __init__(self, pos = (0,0)):
        if not self.__class__.img:
            self.__class__.img = pygame.image.load("../media/modifier_health.png").convert_alpha()

        ModifierEntity.__init__(self, self.__class__.img, pos, modifier = HealModifier())
