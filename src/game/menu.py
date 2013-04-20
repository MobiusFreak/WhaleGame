from pygame.locals import *
import pygame

from game import BaseGame, TestGame
from utils.callbacks import *

from utils import Vector

class Menu(BaseGame):
    def init(self, App):
        BaseGame.init(self, App)
        self.screen = self.app.screen
        self.font = pygame.font.Font("../media/font/VeraMono.ttf", 20)
        self.players = None

        self.draw_select_player_screen()


    def draw_window(self):
        button = pygame.Surface((500, 500))
        button.fill((0,200,200))
        self.screen.fill((200,100,0))
        self.dest = button.get_rect().copy()
        self.dest.center = self.screen.get_rect().center
        self.screen.blit(button, self.dest, self.screen.get_rect())


    # Player selection
    def draw_select_player_screen(self):
        self.draw_window()

        text = self.font.render("Whales?", True, (0,0,0))
        self.screen.blit(text, self.dest, self.screen.get_rect())
        self.dest.top += self.font.get_linesize()*2

        text = self.font.render("1 - Just me. I'm a whale.", True,
                                (0,0,100))
        self.screen.blit(text, self.dest, self.screen.get_rect())

        self.dest.top += self.font.get_linesize()
        text = self.font.render("2 - We are whales. Two whales.", True,
                                (0,100,0))
        self.screen.blit(text, self.dest, self.screen.get_rect())


        register_event(KEYDOWN, self.select_1_player , K_1)
        register_event(KEYDOWN, self.select_2_players , K_2)

    def select_1_player(self):
        unregister_event(KEYDOWN, self.select_1_player , K_1)
        unregister_event(KEYDOWN, self.select_2_players , K_2)

        self.players = 1

        self.draw_select_mode_screen()

    def select_2_players(self):
        unregister_event(KEYDOWN, self.select_1_player , K_1)
        unregister_event(KEYDOWN, self.select_2_players , K_2)

        self.players = 2

        self.draw_select_mode_screen()

    # Mode selection
    def draw_select_mode_screen(self):
        self.draw_window()

        text = self.font.render("Hum... What do you whale?", True, (0,0,0))
        self.screen.blit(text, self.dest, self.screen.get_rect())
        self.dest.top += self.font.get_linesize()*2

        text = self.font.render("1 - Test Whale.", True,
                                (0,0,100))
        self.screen.blit(text, self.dest, self.screen.get_rect())

        register_event(KEYDOWN, self.select_test_game , K_1)

    def select_test_game(self):
        unregister_event(KEYDOWN, self.select_test_game , K_1)
        game = TestGame(self.players)
        self.app.change_game(game)
