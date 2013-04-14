import pygame, math
from pygame.locals import *

from entity import *

ANG_VEL = 2

class Whale(Entity):
    def __init__(self, size = [90,90], pos = (0,0), acc = 1):
        mobius = pygame.image.load("../media/mobius.png")
        self.mobius_img = pygame.transform.smoothscale(mobius,(80, 80))
        Entity.__init__(self, self.mobius_img, pos)

        self.angle = 0
        self.image = pygame.transform.rotozoom(self.mobius_img,
                                               self.angle, 1)

        self.acc = acc
        self.mobius_img_center = [60, 45]

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
        elif pressed[K_d]:
            self.angle -= ANG_VEL * t * 0.1
        else:
            return

        self.angle %= 360

        pos = self.rect.center
        self.image = pygame.transform.rotozoom(self.mobius_img,
                                               self.angle, 1)
        self.rect = self.image.get_rect()
        self.rect.center = pos


    def update_speed(self, t):
        speed_x, speed_y = self.speed
        acc_x, acc_y = 0, 0

        pressed = pygame.key.get_pressed()

        if speed_y > 0:
            friction_y = -1
        else:
            friction_y = 1

        if speed_x > 0:
            friction_x = -1
        else:
            friction_x = 1

        if self.pos[1] < 300:  # in air
            acc_y += GRAVITY

            acc_x += friction_x * AIR_FRICTION * speed_x
            acc_y += friction_y * AIR_FRICTION * speed_y
        elif pressed[K_w]: # in water
            acc_x = self.acc * math.cos(math.radians(self.angle)) *1e-10
            acc_y = -self.acc * math.sin(math.radians(self.angle)) *1e-10

            acc_x += friction_x * WATER_FRICTION * speed_x
            acc_y += friction_y * WATER_FRICTION * speed_y

        self.speed = (speed_x + acc_x * t, speed_y + acc_y * t)


