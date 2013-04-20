from entity import Entity, Whale, Ship, ModifierEntity
from game import WhaleGame
from random import randint

from utils import Vector

MIN_COOLDOWN = 5000
MAX_COOLDOWN = 10000

class Survival(WhaleGame):
    def __init__(self, players):
        WhaleGame.__init__(self, players)
        self.difficulty = 0
        self.cooldown = MIN_COOLDOWN


    def update(self, t):
        self.difficulty = self.score/10
        if len(self.enemies) < 5:
            if self.cooldown <= 0:
                self.create_ship(int(self.difficulty))
                self.cooldown = randint(MIN_COOLDOWN, MAX_COOLDOWN)
            else:
                self.cooldown -= t
        return WhaleGame.update(self, t)

    def create_ship(self, level = 1):
        width, heigth = self.app.screen.get_size()

        screen_x = self.screen_pos(self.app.screen).x

        desp = randint(0, width)
        if desp <= width/2:
            desp -= width
        else:
            desp += width

        desp += screen_x
        ship = Ship(pos = Vector(desp,0), acc = 2,
                    whales = self.whales.sprites())

        self.enemies.add(ship)
        self.entities.add(ship)
