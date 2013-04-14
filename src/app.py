import pygame
from pygame.locals import *

FPS_LIMIT = 60

class App:
    def __init__(self, size = (800, 600)):
        self.size = size
        width, height = size
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.ocean = pygame.Surface((width, height / 2))
        self.ocean.fill((0,0,200))
        self.ocean_rect = pygame.Rect(0,height/2,width,height/2)

    def start(self):
        while self.loop():
            pass

    def loop(self):
        screen = self.screen
        size = self.size

        t = self.clock.tick(FPS_LIMIT)

        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return False

        screen.fill((50,170,225))
        screen.blit(self.ocean, self.ocean_rect)

        pygame.display.flip()

        return True
