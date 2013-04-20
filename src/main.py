#!/usr/bin/python


import pygame, sys
from pygame.locals import *

from app import App


if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    app = App()
    app.start()
    sys.exit()
