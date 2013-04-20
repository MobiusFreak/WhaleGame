import pygame, math

from pygame.locals import *

from entity import *

ANG_ACC = 10

class Whale(Entity):
    def __init__(self, size = [80,80],
                 pos = Vector(0,0), acc = 1, player = 1):

        if player == 1:
            mobius = pygame.image.load("../media/mobius.png").convert_alpha()
        else:
            mobius = pygame.image.load("../media/mobius2.png").convert_alpha()

        mobius_img = pygame.transform.smoothscale(mobius,size)

        Entity.__init__(self, mobius_img, pos)

        self.whale_acceleration = acc

        self.player = player
        if player == 1:
            self.key_acc = K_w
            self.key_left = K_a
            self.key_right = K_d
        else:
            self.key_acc = K_UP
            self.key_left = K_LEFT
            self.key_right = K_RIGHT


    def update(self, t):
        Entity.update(self, t)


    def update_acceleration(self, t):
        pressed = pygame.key.get_pressed()

        if self.pos.y < 0:          # in air
            Entity.update_acceleration(self, t)
        elif pressed[self.key_acc]: # in water
            self.acceleration = self.friction_vector() + self.direction * self.whale_acceleration
        else:
            self.acceleration = self.friction_vector()


    def update_angular_acceleration(self, t):
        pressed = pygame.key.get_pressed()

        Entity.update_angular_acceleration(self, t)
        if pressed[self.key_right]:
            self.angular_acceleration += ANG_ACC
        elif pressed[self.key_left]:
            self.angular_acceleration -= ANG_ACC

    def damage(self, diff, source = None):
        if source == "collision":
            diff *= 0.1
        Entity.damage(self, diff, source)

    def die(self):
        game = app.get_current_game()
        game.game_over = True


