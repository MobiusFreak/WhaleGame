# -*- coding:utf-8 -*-

import pygame, sys
from pygame.locals import *

from game import TestGame
from game import Menu

FPS_LIMIT = 60

class App:
    def __init__(self, size = (1024, 600), game = Menu()):
        self.init_display(size)

        self.clock = pygame.time.Clock()

        self.callbacks = {KEYDOWN : {}, KEYUP : {}, QUIT : []}

        self.register_event(QUIT, self.salir)
        self.register_event(KEYDOWN, self.escape, key = K_ESCAPE)

        self.fps_t = 0

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


    def register_event(self, evt, call, key = None):
        if evt == KEYDOWN or evt == KEYUP:
            if self.callbacks[evt].has_key(key):
                self.callbacks[evt][key].append(call)
            else:
                self.callbacks[evt][key]=[call]
        else:
            self.callbacks[evt].append(call)

    def unregister_event(self, evt, call, key = None):
        if evt == KEYDOWN or evt == KEYUP:
            if self.callbacks[evt].has_key(key):
                if call in self.callbacks[evt][key]:
                    self.callbacks[evt][key].remove(call)
        else:
            if call in self.callbacks[evt]:
                self.callbacks[evt].remove(call)

    def change_game(self,game):
        self.game.exit()
        self.game = game
        self.game.init(self)

    def process_events(self, t):
        for event in pygame.event.get():
            if self.callbacks.has_key(event.type):
                if (event.type == KEYDOWN or event.type == KEYUP):
                    if self.callbacks[event.type].has_key(event.key):
                        for call in self.callbacks[event.type][event.key]:
                            call(t)
                else:
                    for call in self.callbacks[event.type]:
                        call(t)

    def draw(self):
        width, height = self.size

        self.game.draw(self.screen)

        pygame.display.flip()

    def update(self):
        t = self.clock.tick(FPS_LIMIT)

        self.fps_t += t

        if self.fps_t > 5000:
            print int(self.clock.get_fps()), "FPS"
            self.fps_t = 0

        self.process_events(t)

        self.game.update(t)

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

    def salir(self, t):
        sys.exit()

    def escape(self, t):
        if isinstance(self.game, Menu):
            self.salir(t)
        else:
            self.change_game(Menu())
