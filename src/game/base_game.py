import pygame, sys
from pygame.locals import *

from utils import Vector

COLLISION_THRESHOLD = 0.01

class BaseGame(object):
    def init(self, App):
        self.app = App

    def draw(self, screen):
        pass

    def update(self, t):
        pass

    def collisions(self, group1, group2):
        colldic = pygame.sprite.groupcollide(group1, group2,False,False,
                                       collided = pygame.sprite.collide_mask)

        for A in colldic:
            for B in colldic[A]:
                if A != B:
                    dif = B.pos - A.pos
                    dif *= COLLISION_THRESHOLD
                    while pygame.sprite.collide_mask(A,B) != None:
                        A.pos -= dif
                        A.update_rect()
                        B.pos += dif
                        B.update_rect()

                    # TODO: MAAASAAAA

                    A.speed, B.speed = B.speed, A.speed
                    A.angular_speed, B.angular_speed = -B.angular_speed, -A.angular_speed

                if group1 == group2:
                    colldic[B].remove(A)

    def exit(self):
        pass
