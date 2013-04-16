# -*- coding:utf-8 -*-

import pygame, sys
from pygame.locals import *

from whale import Whale, Whale2
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

        # Icon and window title
        pygame.display.set_caption("Mobius")

        icon = pygame.image.load("../media/mobius.png").convert_alpha()
        icon = pygame.transform.smoothscale(icon,(32,32))

        pygame.display.set_icon(icon)


        self.clock = pygame.time.Clock()

        self.whales = pygame.sprite.Group()
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

    def test_entities(self):
        ent = Ship(pos = (725,-500))
        self.entities.add(ent)

        ent = Ship(pos = (450,50))
        self.entities.add(ent)

        ent = Ship(pos = (125,-250))
        self.entities.add(ent)

        ent = Ship(pos = (50,-50))
        self.entities.add(ent)


    def create_whale(self):
        width, height = self.size
        self.whales.add(Whale(pos = (400,-200)))
        self.whales.add(Whale2(pos = (400,100)))

    def draw(self):
        width, height = self.size

        pos = self.whales.sprites()[0].pos # mobius position
        pos += self.whales.sprites()[1].pos # mobius position
        pos = pos * 0.5
        pos -= Vector(width/2, height/2)

        if pos.y > 0: # bajo del maaaar
            self.screen.fill((0,0,200))
        else:
            self.screen.fill((50,170,225))
            dest = self.ocean.get_rect().copy()
            dest.top -= pos.y
            self.screen.blit(self.ocean, dest, self.screen.get_rect())

        for entity in self.entities:
            dest = entity.rect.copy()
            dest.left -= pos.x
            dest.top -= pos.y
            self.screen.blit(entity.image, dest)

        for whale in self.whales:
            dest = whale.rect.copy()
            dest.left -= pos.x
            dest.top -= pos.y
            self.screen.blit(whale.image, dest)

        pygame.display.flip()

    def update(self):
        t = self.clock.tick(FPS_LIMIT)

        self.fps_t += t

        if self.fps_t > 5000:
            print self.clock.get_fps(), "FPS"
            self.fps_t = 0

        self.process_events(t)

        self.collisions(self.whales,self.entities)
        self.collisions(self.whales,self.whales)
        self.collisions(self.entities,self.entities)

        self.whales.update(t)
        self.entities.update(t)


        return True

    def collisions(self, group1, group2):
        colldic = pygame.sprite.groupcollide(group1, group2,False,False, collided = pygame.sprite.collide_mask)
        #print colldic.keys()
        for A in colldic:
            for B in colldic[A]:
                A.speed, B.speed = B.speed, A.speed
                if group1 == group2:
                    colldic[B].remove(A)

                # # Fix vertical overlap
                # if A.rect.top > B.rect.bottom:
                #     A.rect.top = B.rect.bottom
                # else:
                #     A.rect.bottom = B.rect.top

                # # Fix horizontal overlap
                # if A.rect.left > B.rect.right:
                #     A.rect.left = B.rect.right
                # else:
                #     A.rect.right = B.rect.left



    def loop(self):
        if self.update():
            self.draw()
            return True
        else:
            return False


    def start(self):
        while self.loop():
            pass


