import pygame, sys
from pygame.locals import *

from whale import Whale
from entity import Entity

FPS_LIMIT = 60

class ExitListener:
    def __init__(self, App):
        App.register_event(QUIT, self.salir)
        App.register_event(KEYDOWN, self.salir, key = K_ESCAPE)

    def salir(self, t):
        sys.exit()


class App:
    def __init__(self, size = (1024, 600)):
        self.size = size
        width, height = size

        self.screen = pygame.display.set_mode(size)

        self.clock = pygame.time.Clock()

        self.mobius = pygame.sprite.Group()
        self.entities = pygame.sprite.Group()

        self.test_entities()
        self.create_ocean()
        self.create_whale()

        self.callbacks = {KEYDOWN : {}, KEYUP : {}, QUIT : []}

        ExitListener(self)

        self.fps_t = 0

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


    def test_entities(self):
        image = pygame.Surface((50, 50))
        image.fill((200,0,0))
        ent = Entity(image, pos = (725,500))
        self.entities.add(ent)

        image = pygame.Surface((50, 50))
        image.fill((0,200,0))
        ent = Entity(image, pos = (450,50))
        self.entities.add(ent)

        image = pygame.Surface((50, 50))
        image.fill((0,0,0))
        ent = Entity(image, pos = (125,250))
        self.entities.add(ent)

        image = pygame.Surface((50, 50))
        image.fill((255,0,255))
        ent = Entity(image, pos = (50,350))
        self.entities.add(ent)


    def create_whale(self):
        width, height = self.size
        self.mobius.add(Whale(pos = (width/2, height/2)))

    def draw(self):
        self.screen.fill((50,170,225))
        self.screen.blit(self.ocean, self.ocean_rect, self.screen.get_rect())

        self.entities.draw(self.screen)
        self.mobius.draw(self.screen)

        pygame.display.flip()

    def update(self):
        t = self.clock.tick(FPS_LIMIT)

        self.fps_t += t

        if self.fps_t > 1000:
            print self.clock.get_fps(), "FPS"
            self.fps_t = 0

        self.process_events(t)

        self.mobius.update(t)
        self.entities.update(t)

        return True


    def loop(self):
        if self.update():
            self.draw()
            return True
        else:
            return False


    def start(self):
        while self.loop():
            pass
