import pygame, sys
from pygame.locals import *

from whale import Whale

FPS_LIMIT = 60

GRAVITY = 1
AIR_FRICTION = 0.1
WATER_FRICTION = 0.2
DEFAULT_FLOTABILITY = 2

class ExitListener:
    def __init__(self, App):
        App.register_event(QUIT, self.salir)
        App.register_event(KEYDOWN, self.salir, key = K_ESCAPE)

    def salir(self, t):
        sys.exit()


class Entity(pygame.sprite.DirtySprite):
    def __init__(self, Surface, pos = (0,0)):
        pygame.sprite.DirtySprite.__init__(self)

        self.flotability = DEFAULT_FLOTABILITY
        self.pos = pos
        self.speed = (0,0)

        self.image = Surface
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self, t):
        speed_x, speed_y = self.speed
        pos_x, pos_y = self.pos

        acc_y = 0

        if speed_y > 0:
            friction = -1
        else:
            friction = 1

        if pos_y > 300: # in water
            acc_y -= self.flotability
            acc_y += friction * WATER_FRICTION * speed_y
        else: # in air
            acc_y += friction * AIR_FRICTION * speed_y

        acc_y += GRAVITY

        new_speed_y = speed_y + (acc_y * t * 0.5e-2)

        self.speed = (speed_x, new_speed_y)

        self.pos = (pos_x + speed_x, pos_y + new_speed_y )
        self.rect.center = self.pos


class App:
    def __init__(self, size = (800, 600)):
        self.size = size
        width, height = size
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()

        self.mobius = pygame.sprite.Group()
        self.entities = pygame.sprite.Group()

        self.create_ocean()
        #self.create_whale()

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
