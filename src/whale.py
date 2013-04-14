import pygame, math
from pygame.locals import *

from entity import Entity

ANG_VEL = 2

class Whale(Entity):
    def __init__(self, size = [90,90], pos = (0,0), acc = 1):
        mobius = pygame.image.load("../media/mobius.png")
        self.mobius_img = pygame.transform.smoothscale(mobius,(80, 80))

        Entity.__init__(self, self.mobius_img, pos)

        self.acc = acc
        self.angle = 180

        # self.rect = self.image.get_rect()
        self.rect = pygame.Rect (0,0,size[0],size[1])
        self.rect.center = pos


    def update(self, t):
        self.update_angle(t)
        Entity.update(self, t)

    def update_angle(self, t):
        pressed = pygame.key.get_pressed()

        if pressed[K_a]:
            self.angle += ANG_VEL * t * 0.1
            pos = self.rect.center
            self.image = pygame.transform.rotozoom(self.mobius_img,
                                                   self.angle, 1)
            self.rect.center = pos

        if pressed[K_d]:
            self.angle -= ANG_VEL * t * 0.1
            pos = self.rect.center
            self.image = pygame.transform.rotozoom(self.mobius_img,
                                                   self.angle, 1)
            self.rect.center = pos


    def update_speed(self, t):
        pressed = pygame.key.get_pressed()
        if pressed[K_w]:
            speed_x, speed_y = self.speed
            acc_x = self.acc * math.cos(math.radians(self.angle)) * t * 1e-3
            acc_y = self.acc * math.sin(math.radians(self.angle)) * t * 1e-3
            self.speed = (speed_x + acc_x, speed_y + acc_y)
