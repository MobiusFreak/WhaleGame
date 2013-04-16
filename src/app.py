import pygame, sys
from pygame.locals import *

from whale import Whale
from entity import Entity
from vector import Vector
from ship import Ship

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

        self.ocean = pygame.Surface((width, height))
        self.ocean.fill((0,0,200))
        self.ocean_rect = pygame.Rect(0,height/2,width,height/2)


    def test_entities(self):
        ent = Ship(pos = (725,500))
        self.entities.add(ent)

        ent = Ship(pos = (450,50))
        self.entities.add(ent)

        ent = Ship(pos = (125,250))
        self.entities.add(ent)

        ent = Ship(pos = (50,50))
        self.entities.add(ent)


    def create_whale(self):
        width, height = self.size
        self.mobius.add(Whale(pos = (width/2, height/2)))

    def draw(self):
        width, height = self.size

        pos = self.mobius.sprites()[0].pos # mobius position
        pos -= Vector(width/2, height/2)

        if pos[1] > height/2: # bajo del maaaar
            self.screen.fill((0,0,200))
        else:
            self.screen.fill((50,170,225))
            dest = self.ocean_rect.copy()
            dest.top -= pos[1]
            self.screen.blit(self.ocean, dest, self.screen.get_rect())

        for entity in self.entities:
            dest = entity.rect.copy()
            dest.left -= pos[0]
            dest.top -= pos[1]
            self.screen.blit(entity.image, dest)

        for whale in self.mobius:
            dest = whale.rect.copy()
            dest.left -= pos[0]
            dest.top -= pos[1]
            self.screen.blit(whale.image, dest)

#        self.entities.draw(self.screen)
#        self.mobius.draw(self.screen)

        pygame.display.flip()

    def update(self):
        t = self.clock.tick(FPS_LIMIT)

        self.fps_t += t

        if self.fps_t > 1000:
            print self.clock.get_fps(), "FPS"
            self.fps_t = 0

        self.process_events(t)

        self.collisions(self.mobius,self.entities)
        self.collisions(self.entities,self.entities)
        
        self.mobius.update(t)
        self.entities.update(t)


        return True
    
    def collisions(self, group1, group2):
        colldic = pygame.sprite.groupcollide(group1, group2,False,False)
        #print colldic.keys()
        for item in colldic:
            for entity in colldic[item]:
                temp = item.speed
                item.speed = entity.speed
                entity.speed = temp
                if group1 == group2:
                    colldic[entity].remove(item)

    def loop(self):
        if self.update():
            self.draw()
            return True
        else:
            return False


    def start(self):
        while self.loop():
            pass

    
