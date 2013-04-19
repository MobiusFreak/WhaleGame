from pygame.locals import *
import pygame

from game import BaseGame, TestGame

from utils import Vector

class Menu(BaseGame):
    def init(self, App):
        BaseGame.init(self, App)
        self.button = pygame.Surface((300, 300))
        self.button.fill((0,200,200))
        self.app.screen.fill((200,0,0))
        dest = self.button.get_rect().copy()
        dest.center = (512, 300)
        self.app.screen.blit(self.button, dest, self.app.screen.get_rect())


        self.app.register_event(KEYDOWN, self.change_to_test_game , K_n)

    def update(self, t):
        pass

    def exit(self):
        self.app.unregister_event(KEYDOWN, self.change_to_test_game , K_n)

    def change_to_test_game(self, t):
        game = TestGame()
        self.app.change_game(game)
