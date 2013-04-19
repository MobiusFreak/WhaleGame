import pygame, math

from pygame.locals import *

from entity import *

ANG_VEL = 2

class Whale(Entity):
    def __init__(self, size = [80,80], pos = Vector(0,0), acc = 2, player = 1):
        if player == 1:
            mobius = pygame.image.load("../media/mobius.png").convert_alpha()
        else:
            mobius = pygame.image.load("../media/mobius2.png").convert_alpha()

        self.mobius_img = pygame.transform.smoothscale(mobius,size)

        self.direction = Vector(1,0)
        image = pygame.transform.rotozoom(self.mobius_img,
                                          self.direction.angle, 1)

        Entity.__init__(self, image, pos)

        self.acc = acc

        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.rect.inflate_ip(-10,-10)

        if player == 1:
            self.key_acc = K_w
            self.key_left = K_a
            self.key_right = K_d
        else:
            self.key_acc = K_UP
            self.key_left = K_LEFT
            self.key_right = K_RIGHT

    def update(self, t):
        self.update_direction(t)
        Entity.update(self, t)

    def update_direction(self, t):
        pressed = pygame.key.get_pressed()

        if pressed[self.key_left]:
            self.direction.angle += ANG_VEL * t * 0.1
        elif pressed[self.key_right]:
            self.direction.angle -= ANG_VEL * t * 0.1
        else:
            return

        angle = self.direction.angle


        image = self.mobius_img.copy()

        if angle < 270 and angle > 90: # in water
            image = pygame.transform.flip(self.mobius_img, False, True)


        pos = self.rect.center
        self.image = pygame.transform.rotozoom(image,
                                               self.direction.angle, 1)

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = pos


    def get_acceleration(self):
        pressed = pygame.key.get_pressed()

        v_acc = Vector(0,0)
        if self.pos.y < 0:  # in air
            v_acc = V_GRAVITY
        elif pressed[self.key_acc]: # in water
            direction = Vector(self.direction.x, -self.direction.y)
            v_acc = direction * self.acc

        return v_acc + self.get_friction()

