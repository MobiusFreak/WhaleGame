# -*- coding:utf-8 -*-

import pygame, sys
from pygame.locals import *

from utils.callbacks import *
from game import TestGame
from game import Menu

FPS_LIMIT = 60

current_game = None

def get_current_game():
    global current_game
    return current_game


class App:
    def __init__(self, size = (1024, 600), game = Menu()):
        self.init_display(size)

        self.clock = pygame.time.Clock()

        register_event(QUIT, self.salir)
        register_event(KEYDOWN, self.escape, key = K_ESCAPE)

        self.fps_t = 0
        self.font = pygame.font.Font("../media/font/VeraMono.ttf", 20)
        self.fps_surface = self.font.render("? FPS", True, (0,0,0))

        global current_game
        current_game = game

        self.game = game
        self.game.init(self)

    def init_display(self, size):
        self.size = size
        width, height = size

        self.screen = pygame.display.set_mode(size)

        # Icon and window title
        pygame.display.set_caption("Mobius")

        icon = pygame.image.load("../media/mobius.png").convert_alpha()
        icon = pygame.transform.smoothscale(icon,(32,32))

        pygame.display.set_icon(icon)

    def change_game(self,game):
        global current_game
        current_game = game
        self.game.exit()
        self.game = game
        self.game.init(self)


    # TODO: should be in utils.callbacks?
    def process_events(self, t):
        for event in pygame.event.get():
            if callbacks.has_key(event.type):
                if (event.type == KEYDOWN or event.type == KEYUP):
                    if callbacks[event.type].has_key(event.key):
                        for call in callbacks[event.type][event.key]:
                            call()
                else:
                    for call in callbacks[event.type]:
                        call()

    def draw(self):
        width, height = self.size

        self.game.draw(self.screen)
        self.screen.blit(self.fps_surface, self.fps_surface.get_rect())

        pygame.display.flip()

    def update(self):
        t = self.clock.tick(FPS_LIMIT)

        self.fps_t += t

        if self.fps_t > 1000:
            self.fps_surface = self.font.render(str(int(self.clock.get_fps())) + " FPS", True, (0,0,0))
            self.fps_t = 0


        self.process_events(t)
        if not self.game.update(t):
            self.change_game(Menu())

        return True

    def loop(self):
        if self.update():
            self.draw()
            return True
        else:
            return False


    def start(self):
        while self.loop():
            pass

    def salir(self):
        sys.exit()

    def escape(self):
        if isinstance(self.game, Menu):
            self.salir()
        else:
            self.change_game(Menu())
