import pygame, sys
from pygame.locals import *

GRAVITY = 1
AIR_FRICTION = 0.1
WATER_FRICTION = 0.2
DEFAULT_FLOTABILITY = 2

class Entity(pygame.sprite.DirtySprite):
    def __init__(self, Surface, pos = (0,0)):
        pygame.sprite.DirtySprite.__init__(self)

        self.flotability = DEFAULT_FLOTABILITY
        self.pos = pos
        self.speed = (0,0)

        self.image = Surface
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self, t):
        speed_x, speed_y = self.speed
        pos_x, pos_y = self.pos

        acc_y = 0

        if speed_y > 0:
            friction = -1
        else:
            friction = 1

        if pos_y > 300: # in water
            acc_y -= self.flotability
            acc_y += friction * WATER_FRICTION * speed_y
        else: # in air
            acc_y += friction * AIR_FRICTION * speed_y

        acc_y += GRAVITY

        new_speed_y = speed_y + (acc_y * t * 0.5e-2)

        self.speed = (speed_x, new_speed_y)

        self.pos = (pos_x + speed_x, pos_y + new_speed_y )
        self.rect.center = self.pos
