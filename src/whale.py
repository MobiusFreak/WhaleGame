import pygame, sys
from pygame.locals import *

class Whale(pygame.sprite.DirtySprite):
    def __init__(self, size = [84,48], pos = (0,0)):
        pygame.sprite.DirtySprite.__init__(self)

        mobius = pygame.image.load("../media/mobius.png")

        self.image = pygame.transform.smoothscale(mobius,
                                                  (size[0], size[1]))

        self.rect = self.image.get_rect()
        self.rect.center = pos

<<<<<<< HEAD
    def update(self, t):
        pass

=======
    def update():
        pass
>>>>>>> b8e816ec827f6b36061cfd57c2f603f7ba2ce97e
