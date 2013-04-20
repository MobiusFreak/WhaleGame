import pygame, math
from pygame.locals import *

from random import randint

from entity import *
from modifier import ShootingModifier

import app
import sound

ANG_ACC = 2
SHIP_ACC = 5
DAMAGE_UNDER_WATER = 5 # per second

class Ship(Entity):
    def __init__(self, Surface, projectile = None, *args, **kargs):
        Entity.__init__(self, Surface, *args, **kargs)

        game = app.get_current_game()
        self.whales = game.whales.sprites()

        self.objective = self.whales[0]

        if projectile:
            mod = ShootingModifier(projectile)
            mod.init(self)
            self.modifiers.append(mod)


    def update(self, t):
        closest_whale = self.whales[0]
        closest_distance = (self.pos - closest_whale.pos).module
        for whale in self.whales:
            distance = (self.pos - whale.pos).module
            if distance < closest_distance:
                closest_whale = whale
                closest_distance = distance

        self.objective = closest_whale

        Entity.update(self, t)
        if self.pos.y + self.rect.height / 2 > 0:
            angle = self.direction.angle
            if not (angle > 250 or angle < 110):
                self.damage(DAMAGE_UNDER_WATER * t * 1e-3)

    def update_modifiers(self, t):
        if self.pos.y + self.rect.height / 2 > 0:
            angle = self.direction.angle
            if (angle > 250 or angle < 110):
                Entity.update_modifiers(self, t)

    def update_angular_acceleration(self, t):
        pressed = pygame.key.get_pressed()

        Entity.update_angular_acceleration(self, t)

        if self.pos.y + self.rect.height / 2 > 0:
            angle = self.direction.angle
            if angle > 250:
                self.angular_acceleration += ANG_ACC
            elif angle < 110:
                self.angular_acceleration -= ANG_ACC


    def update_acceleration(self, t):
        pressed = pygame.key.get_pressed()

        Entity.update_acceleration(self, t)
        angle = self.direction.angle
        if angle > 250 or angle < 110:
            if self.pos.y + self.rect.height / 2 > 0:
                direction = (self.objective.pos - self.pos).x * 1e-3
                self.speed += Vector(SHIP_ACC, 0) * direction * (t * 1e-3)

    def floatability_vector(self):
        # TODO: it should depend on the amount of pixels in the water
        if self.rect.bottom / 2 > 0: # in water
            return (1 - self.density) * Vector(0,-5)
        else:
            return Vector(0,0)

    def die(self):
        sound.play("crack")
        Entity.die(self)
