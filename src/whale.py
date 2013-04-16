import pygame, math
from pygame.locals import *

from entity import *

ANG_VEL = 2

class Whale(Entity):
    def __init__(self, size = [90,90], pos = Vector(0,0), acc = 2):
        mobius = pygame.image.load("../media/mobius.png").convert_alpha()
        self.mobius_img = pygame.transform.smoothscale(mobius,(80, 80))

        self.direction = Vector(1,0)
        image = pygame.transform.rotozoom(self.mobius_img,
                                          self.direction.angle, 1)

        Entity.__init__(self, image, pos)

        self.acc = acc
        self.mobius_img_center = [60, 45]

        self.rect = pygame.Rect (0,0,size[0],size[1])
        self.rect.center = pos

    def update(self, t):
        self.update_direction(t)
        Entity.update(self, t)

    def update_direction(self, t):
        pressed = pygame.key.get_pressed()

        if pressed[K_a]:
            self.direction.angle += ANG_VEL * t * 0.1
        elif pressed[K_d]:
            self.direction.angle -= ANG_VEL * t * 0.1
        else:
            return


        pos = self.rect.center
        self.image = pygame.transform.rotozoom(self.mobius_img,
                                               self.direction.angle, 1)


        self.rect = self.image.get_rect()
        self.rect.center = pos


    def get_acceleration(self):
        pressed = pygame.key.get_pressed()

        v_acc = Vector(0,0)
        if self.pos[1] < 300:  # in air
            v_acc = V_GRAVITY
        elif pressed[K_w]: # in water
            direction = Vector(self.direction.x, -self.direction.y)
            v_acc = direction * self.acc

        return v_acc + self.get_friction()
