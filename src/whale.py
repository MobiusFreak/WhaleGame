import pygame, sys
from pygame.locals import *

class Whale(pygame.sprite.DirtySprite):
    def __init__(self, size = [90,90], pos = (0,0)):
        pygame.sprite.DirtySprite.__init__(self)

        mobius = pygame.image.load("../media/mobius.png")
        self.ang_vel = 1
        self.acc = 0
        self.angle = 0

        self.image = mobius

        self.image = pygame.transform.smoothscale(mobius,(80, 80))

        # self.rect = self.image.get_rect()
        self.rect = pygame.Rect (0,0,size[0],size[1])

        self.rect.center = pos

    def update(self, t):
        pressed = pygame.key.get_pressed()
        if pressed[K_w]:
            self.acc += 1
        if pressed[K_s]:
            pass #TODO
        if pressed[K_a]:
            self.angle += self.ang_vel * t
            self.image = pygame.transform.rotate(self.image, self.ang_vel*t*1e-3)
            pos = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = pos
        if pressed[K_d]:
            self.angle -= self.ang_vel
            self.image = pygame.transform.rotate(self.image, -self.ang_vel)
            # self.rect = self.image.get_rect()

