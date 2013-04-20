from entity import Entity, Whale, Ship, Ball, ModifierEntity
from game import WhaleGame

class TestGame(WhaleGame):
    def init(self, App):
        WhaleGame.init(self, App)
        self.test_entities()

    def test_entities(self):
        ent = Ball(color = (255,255,0), pos = (725,-500))
        self.entities.add(ent)

        ent = Ball(color = (0,255,0), pos = (500,500))
        self.entities.add(ent)

        ent = Ball(color = (255,0,0), pos = (450,50))
        self.entities.add(ent)

        ent = Ship(pos = (-100,0), whales = self.whales.sprites())
        self.entities.add(ent)
        self.enemies.add(ent)

        ent = ModifierEntity(pos = (600,0))
        self.modifiers.add(ent)
