import pygame
from pygame.locals import *

class App:
    def __init__(self, size = (320, 240)):
        self.size = size
        self.screen = pygame.display.set_mode(size)

    def start(self):
        while self.loop():
            pass

    def loop(self):
        screen = self.screen
        size = self.size

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        screen.fill((0,0,0))

        pygame.display.flip()

        return True
