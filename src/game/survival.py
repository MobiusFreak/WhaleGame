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
        if self.cooldown <= 0:
            self.create_ship()
            self.cooldown = randint(MIN_COOLDOWN, MAX_COOLDOWN)
        else:
            self.cooldown -= t
        return WhaleGame.update(self, t)

    def create_ship(self,level = 1):
        width, heigth = self.app.screen.get_size()
        desp = randint(0,width)
        if desp <= width/2:
            desp -= width
        else:
            desp += width
        ship = Ship(pos = Vector(desp,0), acc = 2,
                    whales = self.whales.sprites())
        self.entities.add(ship)
