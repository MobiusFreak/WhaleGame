from entity import Entity, Whale, Ship, Ball, ModifierEntity

from pygame.locals import *

import pygame

from game import BaseGame
from utils import Vector

class TestGame(BaseGame):
    def init(self, App):
        BaseGame.init(self, App)

        self.whales = pygame.sprite.Group()
        self.entities = pygame.sprite.Group()
        self.modifiers = pygame.sprite.Group()

        self.ocean = pygame.Surface(App.screen.get_size())
        self.ocean.fill((0,0,200))

        self.create_whales()
        self.test_entities()


    def test_entities(self):
        ent = Ball(color = (255,255,0), pos = (725,-500))
        self.entities.add(ent)

        ent = Ball(color = (0,255,0), pos = (500,500))
        self.entities.add(ent)

        ent = Ball(color = (255,0,0), pos = (450,50))
        self.entities.add(ent)

        ent = Ship(pos = (125,-250), whales = self.whales.sprites())
        self.entities.add(ent)

        ent = ModifierEntity(pos = (600,0))
        self.modifiers.add(ent)


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

        for modifier in self.modifiers:
            dest = modifier.rect.copy()
            dest.left -= pos.x
            dest.top -= pos.y
            screen.blit(modifier.image, dest)


        for whale in self.whales.sprites():
            dest = whale.rect.copy()
            dest.left -= pos.x
            dest.top -= pos.y

            if dest.right < 0 or dest.left > width or dest.top > height or dest.bottom < 0:
                self.draw_whale_indicator(screen, pos, whale)


    def draw_whale_indicator(self, screen, pos, whale):
            width, height = screen.get_size()
            orig_rect = whale.original_image.get_rect()
            diagonal = Vector(orig_rect.topleft) - Vector(orig_rect.bottomright)
            side = int(diagonal.module)
            radius = side / 2

            indicator_rect = pygame.Rect(0,0,side,side)
            indicator = pygame.surface.Surface((side,side), SRCALPHA)
            pygame.draw.circle(indicator, (255,0,0),
                               (side/2,side/2),
                               radius, 3)

            dest = whale.rect.copy()
            dest.center = indicator_rect.center
            indicator.blit(whale.image, dest)


            # TODO: size depends on the distance
            # screen_center = pos + Vector(width/2, height/2)
            # distance = (whale.pos - screen_center).module

            # scaled_size = int(60 / (distance / height))

            # indicator = pygame.transform.smoothscale(indicator,
            #                                      [scaled_size,scaled_size])
            # indicator_rect = indicator.get_rect()

            dest = whale.rect.copy()
            dest.left -= pos.x
            dest.top -= pos.y

            indicator_rect.center = dest.center

            if dest.right < 0:
                indicator_rect.left = 0
            elif dest.left > width:
                indicator_rect.right = width
            if dest.top > height:
                indicator_rect.bottom = height
            elif dest.bottom < 0:
                indicator_rect.top = 0

            screen.blit(indicator, indicator_rect)


    def update(self, t):
        self.collisions(self.whales,self.entities)
        self.collisions(self.whales,self.whales)
        self.collisions(self.entities,self.entities)
        self.collisions(self.entities,self.modifiers)


        # Modifiers
        colldic = pygame.sprite.groupcollide(self.whales, self.modifiers, False, True)

        for Entity in colldic:
            for ModifierEntity in colldic[Entity]:
                mod = ModifierEntity.modifier
                Entity.modifiers.append(mod)
                mod.init(Entity)

        self.whales.update(t)
        self.entities.update(t)
        self.modifiers.update(t)

        return True

    def exit(self):
        pass
