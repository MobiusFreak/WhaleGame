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


class Entity(pygame.sprite.DirtySprite):
    def __init__(self, Surface, pos = (0,0), gravity = 1):
        pygame.sprite.DirtySprite.__init__(self)

        self.gravity = gravity
        self.pos = pos

        self.image = Surface
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self, t):
        pass
        # x, y = self.rect.center
        # newx = x
        # newy = self.gravity * t * (300 - y) * 1e-2

        # self.pos = (newx, newy)
        # self.rect.center = self.pos


class App:
    def __init__(self, size = (800, 600)):
        self.size = size
        width, height = size
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()

        self.mobius = pygame.sprite.Group()
        self.entities = pygame.sprite.Group()

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


        image = pygame.Surface((50, 50))
        image.fill((200,0,0))
        ent = Entity(image, pos = (400,500))
        self.entities.add(ent)


    def create_whale(self):
        width, height = self.size
        self.mobius.add(Whale(pos = (width/2, height/2)))

    def loop(self):
        screen = self.screen
        size = self.size

        t = self.clock.tick(FPS_LIMIT)

        self.process_events(t)

        screen.fill((50,170,225))
        screen.blit(self.ocean, self.ocean_rect)

        self.mobius.update(t)
        self.entities.update(t)

        self.mobius.draw(screen)
        self.entities.draw(screen)


        pygame.display.flip()

        return True
