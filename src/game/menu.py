# -*- coding:utf-8 -*-

from pygame.locals import *
import pygame

from game import BaseGame, TestGame, Survival
from utils.callbacks import *

from utils import Vector

import sound

class Menu(BaseGame):
    def init(self, App):
        BaseGame.init(self, App)
        self.screen = self.app.screen
        self.font = pygame.font.Font("../media/font/VeraMono.ttf", 20)
        self.players = None

        register_event(KEYDOWN, self.open_help, K_h)
        self.draw_select_player_screen()


    def open_help(self):
        self.app.change_game(HelpScreen())

    def draw_window(self):
        button = pygame.Surface((500, 500))
        button.fill((0,200,200))
        self.screen.fill((200,100,0))
        self.dest = button.get_rect().copy()
        self.dest.center = self.screen.get_rect().center
        self.screen.blit(button, self.dest, self.screen.get_rect())

        bigfont = pygame.font.Font("../media/font/VeraMono.ttf", 40)
        text = bigfont.render("Mobius", True, (0,0,0))
        dest = self.dest
        dest.top -= bigfont.get_linesize()
        self.screen.blit(text, dest, self.screen.get_rect())
        self.dest.top += self.font.get_linesize()*2

        self.dest.top += self.font.get_linesize()
        text = self.font.render("Press 'h' for help", True, (0,000,0))
        dest = text.get_rect()
        width, height = self.app.screen.get_size()
        dest.bottom = height
        dest.right = width
        print dest
        self.screen.blit(text, dest, self.screen.get_rect())


        self.dest.top += self.font.get_linesize()
        text = self.font.render("Press 'ESC' to exit the game", True, (0,000,0))
        dest = text.get_rect()
        width, height = self.app.screen.get_size()
        dest.bottom = height
        dest.left = 0
        print dest
        self.screen.blit(text, dest, self.screen.get_rect())


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
        sound.play("oneplayer")
        unregister_event(KEYDOWN, self.select_1_player , K_1)
        unregister_event(KEYDOWN, self.select_2_players , K_2)

        self.players = 1

        self.draw_select_mode_screen()

    def select_2_players(self):
        sound.play("twoplayers")
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

        text = self.font.render("1 - Surwhaleval.", True,
                                (0,0,100))
        self.screen.blit(text, self.dest, self.screen.get_rect())


        register_event(KEYDOWN, self.select_survival , K_1)

    def select_test_game(self):
        unregister_event(KEYDOWN, self.select_test_game , K_1)
        unregister_event(KEYDOWN, self.select_survival , K_2)
        game = TestGame(self.players)
        self.app.change_game(game)

    def select_survival(self):
        unregister_event(KEYDOWN, self.select_test_game , K_1)
        unregister_event(KEYDOWN, self.select_survival , K_2)
        game = Survival(self.players)
        self.app.change_game(game)

    def exit(self):
        unregister_event(KEYDOWN, self.select_test_game , K_1)
        unregister_event(KEYDOWN, self.select_survival , K_2)
        unregister_event(KEYDOWN, self.select_1_player , K_1)
        unregister_event(KEYDOWN, self.select_2_players , K_2)
        unregister_event(KEYDOWN, self.open_help, K_h)

class HelpScreen(BaseGame):
    def init(self, App):
        BaseGame.init(self, App)
        self.screen = self.app.screen
        self.font = pygame.font.Font("../media/font/VeraMono.ttf", 20)

        self.draw_help_screen()


    def draw_window(self):
        button = pygame.Surface((500, 500))
        button.fill((0,100,200))
        self.screen.fill((100,200,0))
        self.dest = button.get_rect().copy()
        self.dest.center = self.screen.get_rect().center
        self.screen.blit(button, self.dest, self.screen.get_rect())


    def draw_help_screen(self):
        self.draw_window()

        text = self.font.render("You need help?", True, (0,0,0))
        self.screen.blit(text, self.dest, self.screen.get_rect())
        self.dest.top += self.font.get_linesize()*2

        text = self.font.render("Try to kill ships by pushing them.",
                                True, (0,0,0))
        self.screen.blit(text, self.dest, self.screen.get_rect())

        self.dest.top += self.font.get_linesize()*2
        text = self.font.render("Player 1 controls:", True, (0,000,0))
        self.screen.blit(text, self.dest, self.screen.get_rect())

        self.dest.top += self.font.get_linesize()
        text = self.font.render("    Accelerate:  W", True, (0,000,0))
        self.screen.blit(text, self.dest, self.screen.get_rect())

        self.dest.top += self.font.get_linesize()
        text = self.font.render("    Rotate left: A", True, (0,000,0))
        self.screen.blit(text, self.dest, self.screen.get_rect())

        self.dest.top += self.font.get_linesize()
        text = self.font.render("    Rotate left: D", True, (0,000,0))
        self.screen.blit(text, self.dest, self.screen.get_rect())


        self.dest.top += self.font.get_linesize()*2
        text = self.font.render("Player 2 controls:", True, (0,000,0))
        self.screen.blit(text, self.dest, self.screen.get_rect())

        self.dest.top += self.font.get_linesize()
        text = self.font.render("    Accelerate:  ARROW UP", True, (0,000,0))
        self.screen.blit(text, self.dest, self.screen.get_rect())

        self.dest.top += self.font.get_linesize()
        text = self.font.render("    Rotate left: ARROW LEFT", True, (0,000,0))
        self.screen.blit(text, self.dest, self.screen.get_rect())

        self.dest.top += self.font.get_linesize()
        text = self.font.render("    Rotate left: ARROW RIGHT", True, (0,000,0))
        self.screen.blit(text, self.dest, self.screen.get_rect())

        self.dest.top += self.font.get_linesize()
        text = self.font.render("Press 'ESC' to return to menu", True, (0,000,0))
        dest = text.get_rect()
        width, height = self.app.screen.get_size()
        dest.bottom = height
        dest.left = 0
        print dest
        self.screen.blit(text, dest, self.screen.get_rect())
