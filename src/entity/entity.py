import pygame, sys
from pygame.locals import *
from utils import Vector

AIR_FRICTION = 0.1
WATER_FRICTION = 0.2

V_GRAVITY = Vector(0, 1)
V_DEFAULT_FLOATABILITY = Vector(0, -2)


class Entity(pygame.sprite.Sprite):
    def __init__(self, Surface, pos = (0,0)):
        pygame.sprite.Sprite.__init__(self)

        self.floatability = V_DEFAULT_FLOATABILITY
        self.pos = Vector(pos)
        self.speed = Vector(0,0)

        self.image = Surface
        self.rect = self.image.get_rect()
        self.rect.center = tuple(pos)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, t):
        self.update_speed(t)
        self.update_pos(t)

    def update_speed(self, t):
        self.speed += self.get_acceleration() * t * 1e-2

    def update_pos(self, t):
        self.pos += self.speed * t * 0.05
        self.update_rect()

    def update_rect(self):
        if (self.pos - Vector(self.rect.center)).module > 1:
            self.rect.center = tuple(self.pos)

    def get_friction(self):
        if self.pos.y > 0: # in water
            return -1 * self.speed * WATER_FRICTION
        else: # in air
            return -1 * self.speed * AIR_FRICTION

    def get_floatability(self):
        if self.pos.y > 0: # in water
            return self.floatability
        else:
            return Vector(0,0)

    def get_acceleration(self):
        return V_GRAVITY + self.get_friction() + self.get_floatability()
