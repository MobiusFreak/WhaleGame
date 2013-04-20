import pygame, sys
from pygame.locals import *
from utils import Vector

AIR_FRICTION = 0.05
WATER_FRICTION = 0.15

V_GRAVITY = Vector(0, 0.5)
DEFAULT_DENSITY = 0.8

class Entity(pygame.sprite.Sprite):
    def __init__(self, Surface, pos = (0,0),
                 mass = None, speed = (0,0),
                 direction = (1,0), angular_speed = 0,
                 acceleration = (0,0), angular_acceleration = 0,
                 health = 100, density = DEFAULT_DENSITY, friction = 1):

        pygame.sprite.Sprite.__init__(self)

        self.health = health

        self.pos = Vector(pos)
        self.speed = Vector(speed)

        self.direction = Vector(direction)
        self.angular_speed = angular_speed

        self.original_image = Surface
        self.image = Surface
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.update_rect()
        self.update_image_direction()

        volume = self.mask.count()

        if mass:
            self.mass = mass
            self.density = float(self.mass) / volume
        else:
            self.mass = density * volume
            self.density = density

        self.friction = friction

        # Default value is 0
        self.acceleration = Vector(acceleration)
        self.angular_acceleration = angular_acceleration

        # Modifiers
        self.modifiers = []


    def update_rect(self):
        if (self.pos - Vector(self.rect.center)).module > 1:
            self.rect.center = tuple(self.pos)

    def update_image_direction(self):
        angle = -self.direction.angle

        image = self.original_image.copy()

        # FLIP
        #if angle < 270 and angle > 90: # in water
        #    image = pygame.transform.flip(image, False, True)


        pos = self.rect.center
        self.image = pygame.transform.rotozoom(image,
                                               angle, 1)

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = pos


    def update(self, t):
        self.update_acceleration(t)
        self.update_speed(t)
        self.update_position(t)

        self.update_angular_acceleration(t)
        self.update_angular_speed(t)
        self.update_angle(t)

        for modifier in self.modifiers:
            modifier.update(t, self)


    def update_acceleration(self, t):
        self.acceleration = V_GRAVITY + self.friction_vector() + self.floatability_vector()

    def update_speed(self, t):
        self.speed += self.acceleration * (t * 1e-2)

    def update_position(self, t):
        self.pos += self.speed * (t * 1e-1)
        self.update_rect()


    def update_angular_acceleration(self, t):
        self.angular_acceleration = self.angular_friction()

    def update_angular_speed(self, t):
        self.angular_speed += self.angular_acceleration * (t * 1e-2)

    def update_angle(self, t):
        self.direction.angle += self.angular_speed * (t * 1e-2)
        self.update_image_direction()


    def friction_vector(self):
        # TODO: it should depend on the amount of pixels in the water
        if self.pos.y > 0: # in water
            friction = WATER_FRICTION * self.friction
        else:              # in air
            friction = AIR_FRICTION * self.friction

        return -self.speed * friction

    def angular_friction(self):
        # TODO: it should depend on the amount of pixels in the water
        if self.pos.y > 0: # in water
            friction = WATER_FRICTION
        else:              # in air
            friction = AIR_FRICTION

        return -self.angular_speed * friction * 4

    def floatability_vector(self):
        # TODO: it should depend on the amount of pixels in the water
        if self.pos.y > 0: # in water
            return (1 - self.density) * Vector(0,-5)
        else:
            return Vector(0,0)
