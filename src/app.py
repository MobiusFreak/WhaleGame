import pygame, sys
from pygame.locals import *

from whale import Whale

FPS_LIMIT = 60


class ExitListener:
    def __init__(self, App):
        App.register_event(QUIT, self.salir)
        App.register_event(KEYDOWN, self.salir, key = K_ESCAPE)

    def salir(self, t):
        sys.exit()


class App:
    def __init__(self, size = (800, 600)):
        self.size = size
        width, height = size
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()

        self.create_ocean()
        self.create_whale()

        self.callbacks = {KEYDOWN : {}, KEYUP : {}, QUIT : []}

        ExitListener(self)

    def start(self):
        while self.loop():
            pass

    def register_event(self, evt, call, key = None):
        if evt == KEYDOWN or evt == KEYUP:
            if self.callbacks[evt].has_key(key):
                self.callbacks[evt][key].append(call)
            else:
                self.callbacks[evt][key]=[call]
        else:
            self.callbacks[evt].append(call)

    def process_events(self, t):
        for event in pygame.event.get():
            if self.callbacks.has_key(event.type):
                if (event.type == KEYDOWN or event.type == KEYUP):
                    if self.callbacks[event.type].has_key(event.key):
                        for call in self.callbacks[event.type][event.key]:
                            call(t)
                else:
                    for call in self.callbacks[event.type]:
                        call(t)


    def create_ocean(self):
        width, height = self.size

        self.ocean = pygame.Surface((width, height / 2))
        self.ocean.fill((0,0,200))
        self.ocean_rect = pygame.Rect(0,height/2,width,height/2)

    def create_whale(self):
        width, height = self.size
        self.mobius = pygame.sprite.Group(Whale(pos = (width/2, height/2)))

    def loop(self):
        screen = self.screen
        size = self.size

        t = self.clock.tick(FPS_LIMIT)

        self.process_events(t)

        screen.fill((50,170,225))
        screen.blit(self.ocean, self.ocean_rect)
        self.mobius.draw(screen)

        pygame.display.flip()

        return True
