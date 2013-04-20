from entity import Entity, Whale, Ship, ModifierEntity, WoodShip, MetalShip, Destructor
from game import WhaleGame
from random import randint, randrange

from utils import Vector

MIN_COOLDOWN = 5000
MAX_COOLDOWN = 10000

class Survival(WhaleGame):
    def __init__(self, players):
        WhaleGame.__init__(self, players)
        self.difficulty = 0
        self.cooldown = MIN_COOLDOWN


    def update(self, t):
        if len(self.enemies) < 5:
            if self.cooldown <= 0:
                self.create_ship(int(self.difficulty))
                self.cooldown = randint(MIN_COOLDOWN, MAX_COOLDOWN)
            else:
                self.cooldown -= t
        return WhaleGame.update(self, t)

    def create_ship(self, level = 1):

        if self.difficulty < 10:
            self.difficulty = int(self.score/50)
        width, heigth = self.app.screen.get_size()

        screen_x = self.screen_pos(self.app.screen).x

        desp = randint(0, width)
        if desp <= width/2:
            desp -= width
        else:
            desp += width

        desp += screen_x

        num = randrange(self.difficulty-3, self.difficulty+3);
        if num < 0:
            num = 0
        if num > 10:
            num = 10
        
        if num < 3:
            ship = WoodShip(pos = Vector(desp,0))
        elif num < 8:
            ship = MetalShip(pos = Vector(desp,0))
        else:
            ship = Destructor(pos = Vector(desp,0))

        self.enemies.add(ship)
        self.entities.add(ship)
