from entity import *
from modifier import Modifier

# Ship modifiers
class ShootingModifier(Modifier):
    def __init__(self, projectile):
        self.projectile = projectile
    def init(self, entity):
        self.cooldown = 3000

    def update(self, t, ship):
        if self.cooldown > 0:
            self.cooldown -= t
        else:
            objective = ship.objective
            direction = objective.pos - ship.pos

            shoot(ship, self.projectile, ship.pos, direction)

            self.cooldown = 2000
