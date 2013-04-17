from entity import Entity, Whale, Ship

from game import *
from utils import Vector

class TestGame(Game):
    def init(self, App):
        Game.init(self, App)

        self.whales = pygame.sprite.Group()
        self.entities = pygame.sprite.Group()

        self.ocean = pygame.Surface(App.screen.get_size())
        self.ocean.fill((0,0,200))

        self.test_entities()
        self.create_whales()


    def test_entities(self):
        ent = Ship(pos = (725,-500))
        self.entities.add(ent)

        ent = Ship(pos = (450,50))
        self.entities.add(ent)

        ent = Ship(pos = (125,-250))
        self.entities.add(ent)

        img = pygame.surface.Surface((40,40), SRCALPHA)
        pygame.draw.circle(img, (255,0,0), (20,20), 20)
        pygame.draw.circle(img, (0,0,0), (20,20), 20, 2)
        ent = Entity(img, pos = (0, -300))
        self.entities.add(ent)


    def create_whales(self):
        width, height = self.app.size
        self.whales.add(Whale(pos = (300,-200)))
        self.whales.add(Whale(pos = (400,100), player = 2))


    def draw(self, screen):
        width, height = screen.get_size()

        pos = Vector(0,0)
        for whale in self.whales.sprites():
            pos += whale.pos

        pos = pos * (1. / len(self.whales.sprites()))

        pos -= Vector(width/2, height/2)

        if pos.y > 0: # bajo del maaaar
            color = 200 - pos.y * 0.1
            if color < 0: color = 0
            screen.fill((0,0,color))
        else:
            screen.fill((50,170, 225))
            dest = self.ocean.get_rect().copy()
            dest.top -= pos.y
            screen.blit(self.ocean, dest, screen.get_rect())

        for entity in self.entities:
            dest = entity.rect.copy()
            dest.left -= pos.x
            dest.top -= pos.y
            screen.blit(entity.image, dest)

        for whale in self.whales:
            dest = whale.rect.copy()
            dest.left -= pos.x
            dest.top -= pos.y
            screen.blit(whale.image, dest)


    def update(self, t):
        self.collisions(self.whales,self.entities)
        self.collisions(self.whales,self.whales)
        self.collisions(self.entities,self.entities)

        self.whales.update(t)
        self.entities.update(t)


        return True
