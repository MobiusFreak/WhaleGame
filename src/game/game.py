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
            if len(colldic[A])>0:
                for B in colldic[A]:
                    if A != B:
                        dif = B.pos - A.pos                    
                        while pygame.sprite.collide_mask(A,B) != None:
                            A.pos -= dif*0.01
                            A.update_rect()
                            B.pos += dif*0.01
                            B.update_rect()

                    A.speed, B.speed = B.speed, A.speed
                        
                    if group1 == group2:
                        colldic[B].remove(A)
