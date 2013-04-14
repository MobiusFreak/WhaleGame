import pygame, sys
from pygame.locals import *

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
        self.ocean = pygame.Surface((width, height / 2))
        self.ocean.fill((0,0,200))
        self.ocean_rect = pygame.Rect(0,height/2,width,height/2)

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
                if event.type == KEYDOWN or event.type == KEYUP:
                    for call in self.callbacks[event.type][event.key]:
                        call(t)
                else:
                    for call in self.callbacks[event.type]:
                        call(t)


    def loop(self):
        screen = self.screen
        size = self.size

        t = self.clock.tick(FPS_LIMIT)

        self.process_events(t)

        screen.fill((50,170,225))
        screen.blit(self.ocean, self.ocean_rect)

        pygame.display.flip()

        return True
