from entity import Entity, Whale, Ship, Ball, ModifierEntity

from pygame.locals import *
import pygame

from game import BaseGame
from utils import Vector
from utils.collisions import *


class WhaleGame(BaseGame):
    def __init__(self, players = 2):
        BaseGame.__init__(self)
        self.players = players

    def init(self, App):
        BaseGame.init(self, App)

        self.whales = pygame.sprite.Group()
        self.entities = pygame.sprite.Group()
        self.modifiers = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()

        self.ocean = pygame.Surface(App.screen.get_size())
        self.ocean.fill((0,0,200))

        self.create_whales()


    def create_whales(self):
        for i in range(1, self.players+1):
            self.whales.add(Whale(pos = (100*i,-200), player = i))


    # TODO: center view above whales?
    def draw(self, screen):
        width, height = screen.get_size()

        pos = Vector(0,0)
        for whale in self.whales.sprites():
            pos += whale.pos
        pos = pos * (1. / len(self.whales.sprites()))

        pos -= Vector(width/2, height/2)

        # Draw the ocean
        self.draw_ocean(screen, pos)

        # Draw entities
        self.draw_group(screen, pos, self.entities)
        self.draw_group(screen, pos, self.modifiers)
        self.draw_group(screen, pos, self.projectiles)

        # Draw HUD
        self.draw_indicators(screen, pos)
        self.draw_health(screen, pos)
        # TODO: draw modifiers

    def draw_ocean(self, screen, pos):
        if pos.y > 0: # bajo el maaaar
            color = 200 - pos.y * 0.2
            if color < 20: color = 20
            screen.fill((0,0,color))
        else:
            screen.fill((50,170,225))
            dest = self.ocean.get_rect().copy()
            dest.top -= pos.y
            screen.blit(self.ocean, dest, screen.get_rect())

    def draw_health(self, screen, pos):
        width, height = screen.get_size()

        colors = [(200,0,0,200), (0,200,0,200), (0,200,200,200)]
        # TODO: player attribute?
        for whale in self.whales:
            i = whale.player -1
            color = colors[i % len(colors)]

            bar = pygame.surface.Surface((100, 20), SRCALPHA)

            health_rect = bar.get_rect()
            health_rect.left = 2
            health_rect.right = whale.health - 2
            pygame.draw.rect(bar, color, health_rect)
            pygame.draw.rect(bar, (200,200,200), bar.get_rect(), 3)

            rect = bar.get_rect()
            if i % 2 == 1: # right
                rect.right = width - 10
                rect.bottom = height - (10 + 20 * (i / 2))
            else: # left
                rect.left = 10
                rect.bottom = height - (10 + 20 * (i / 2))


            screen.blit(bar, rect)


    def draw_indicators(self, screen, pos):
        width, height = screen.get_size()
        for whale in self.whales:
            dest = whale.rect.copy()
            dest.left -= pos.x
            dest.top -= pos.y

            screen.blit(whale.image, dest)

            if dest.right < 0 or dest.left > width or \
               dest.top > height or dest.bottom < 0:
                self.draw_whale_indicator(screen, pos, whale)

    def draw_group(self, screen, pos, group):
        for sprite in group:
            dest = sprite.rect.copy()
            dest.left -= pos.x
            dest.top -= pos.y
            screen.blit(sprite.image, dest)


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
        collisions(self.whales, self.modifiers, kill2 = True, function = set_modifier)
#        collisions(self.entities, self.modifiers, kill2 = True, function = set_modifier)
        collisions(self.entities, self.projectiles, function = self.projectile_hit)
        collisions(self.whales, self.projectiles, function = self.projectile_hit)

        collisions(self.whales, self.entities)
        collisions(self.whales, self.whales)
        collisions(self.entities, self.entities)
        collisions(self.entities, self.modifiers)


        self.whales.update(t)
        self.entities.update(t)
        self.modifiers.update(t)
        self.projectiles.update(t)

        return True

    def exit(self):
        pass


    def projectile_hit(self, entity, projectile):
        if entity != projectile.shooter:
            entity.health -= projectile.damage
            self.projectiles.remove(projectile)


def set_modifier(entity, modifier_entity):
    mod = modifier_entity.modifier
    entity.modifiers.append(mod)
    mod.init(entity)
