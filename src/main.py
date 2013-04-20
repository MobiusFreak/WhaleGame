#!/usr/bin/python


import pygame, sys
from pygame.locals import *
import sound

from app import App


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    pygame.mixer.init(frequency = 44100)
    sound.init()

    app = App()
    app.start()
    sys.exit()
