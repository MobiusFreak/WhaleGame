import pygame
from pygame.locals import *

from entity import Entity
import app
import sound

REORIENTATION_ACCELERATION = 1

# TODO: ajustar el vector direccion al vector velocidad
class Projectile(Entity):
    def __init__(self, Surface, pos = (0,0), direction = (0,0),
                 speed = (0,0), density = 1, friction = 0.2, damage = 10,
                 shooter = None):

        self.damage = damage
        self.shooter = shooter
        Entity.__init__(self, Surface, pos = pos, direction = direction,
                        speed = speed, density = density, friction = 0.2)


    def update_angular_acceleration(self, t):
        Entity.update_angular_acceleration(self, t)

        acceleration = 0

        angle = self.speed.angle - self.direction.angle
        acceleration = angle * REORIENTATION_ACCELERATION * 1e-1

        if angle > 180:
            acceleration *= -1

        self.angular_acceleration += acceleration


class Harpoon(Projectile):
    def __init__(self, *args, **kargs):
        img = pygame.image.load("../media/harpoon.png").convert_alpha()
        Projectile.__init__(self, img, *args, **kargs)



def shoot(shooter, Projectile, pos, direction, speed = 5):
    sound.play("harpoon")
    direction.module = 1
    pos += direction

    ent = Projectile(pos = pos, direction = direction,
                     speed = direction * speed, shooter = shooter)

    game = app.get_current_game()
    game.projectiles.add(ent)

