#     Name of the program: Mobius - Description: a game about a whale that has to wreck every ship
#     Copyright (C) 2013
#     
#     Authors:
#     Daniel 'akathorn' Espino <akathorn@gmail.com>
#     Carlos 'Qvent' Garcia <supermegaluigi@gmail.com>
#     Isaac 'mio85' Sánchez <isr_92@hotmail.com>
#     Marcos 'sneaky' Sebastián <gatojazz92@gmail.com>
#     

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.

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

    pygame.mixer.music.load("../media/music.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)


    app = App()
    app.start()
    sys.exit()
