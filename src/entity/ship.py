import pygame, math
from pygame.locals import *

from entity import *

ANG_ACC = 2
SHIP_ACC = 5

class Ship(Entity):
    def __init__(self, size = [90,90], pos = Vector(0,0), acc = 2,
                 whales = []):

        ship = pygame.image.load("../media/shitp.png").convert_alpha()
        self.ship_img = pygame.transform.smoothscale(ship,size)

        Entity.__init__(self, self.ship_img, pos)
        self.rect.inflate_ip(-10,-20)

        self.whales = whales


    def update_angular_acceleration(self, t):
        pressed = pygame.key.get_pressed()

        Entity.update_angular_acceleration(self, t)

        if self.pos.y + self.rect.height / 2 > 0:
            angle = self.direction.angle
            if angle > 250:
                self.angular_acceleration += ANG_ACC
            elif angle < 110:
                self.angular_acceleration -= ANG_ACC


    def update_acceleration(self, t):
        pressed = pygame.key.get_pressed()

        Entity.update_acceleration(self, t)
        angle = self.direction.angle
        if angle > 250 or angle < 110:
            if self.pos.y + self.rect.height / 2 > 0:
                direction = (self.whales[0].pos - self.pos).x * 1e-3
                self.speed += Vector(SHIP_ACC, 0) * direction * (t * 1e-3)
