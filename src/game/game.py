import pygame, sys
from pygame.locals import *

from utils import Vector


class Game(object):
    def init(self, App):
        self.app = App

    def draw(self, screen):
        pass

    def collisions(self, group1, group2):
        colldic = pygame.sprite.groupcollide(group1, group2,False,False,
                                  collided = pygame.sprite.collide_mask)
        for A in colldic:
            for B in colldic[A]:
                A.speed, B.speed = B.speed, A.speed
                if group1 == group2:
                    colldic[B].remove(A)
