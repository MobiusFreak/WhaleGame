from entity import Entity, Whale, Ship, Ball

from pygame.locals import *

import pygame

from game import BaseGame
from utils import Vector

class TestGame(BaseGame):
    def init(self, App):
        BaseGame.init(self, App)

        self.whales = pygame.sprite.Group()
        self.entities = pygame.sprite.Group()

        self.ocean = pygame.Surface(App.screen.get_size())
        self.ocean.fill((0,0,200))

        self.test_entities()
        self.create_whales()


    def test_entities(self):
        ent = Ball(color = (255,255,0), pos = (725,-500))
        self.entities.add(ent)

        ent = Ball(color = (0,255,0), pos = (500,500))
        self.entities.add(ent)

        ent = Ball(color = (255,0,0), pos = (450,50))
        self.entities.add(ent)

        ent = Ship(pos = (125,-250))
        self.entities.add(ent)


    def create_whales(self):
        width, height = self.app.size
        self.whales.add(Whale(pos = (300,-200)))
        self.whales.add(Whale(pos = (400,100), player = 2))


    def draw(self, screen):
        width, height = screen.get_size()

        pos = Vector(0,0)

        for whale in self.whales.sprites():
            pos += whale.pos
        pos = pos * (1. / len(self.whales.sprites()))

        pos -= Vector(width/2, height/2)

        if pos.y > 0: # bajo el maaaar
            color = 200 - pos.y * 0.2
            if color < 20: color = 20
            screen.fill((0,0,color))
        else:
            screen.fill((50,170,225))
            dest = self.ocean.get_rect().copy()
            dest.top -= pos.y
            screen.blit(self.ocean, dest, screen.get_rect())

        for entity in self.entities:
            dest = entity.rect.copy()
            dest.left -= pos.x
            dest.top -= pos.y
            screen.blit(entity.image, dest)

        for whale in self.whales:
            dest = whale.rect.copy()
            dest.left -= pos.x
            dest.top -= pos.y
            screen.blit(whale.image, dest)


    def update(self, t):
        self.collisions(self.whales,self.entities)
        self.collisions(self.whales,self.whales)
        self.collisions(self.entities,self.entities)

        self.whales.update(t)
        self.entities.update(t)

        return True

    def exit(self):
        pass
