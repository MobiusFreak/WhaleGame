import pygame
from pygame.locals import *
from os import listdir
from os.path import isfile, join

from random import randint

sounds = {}

def play(base):
    if not sounds.has_key(base):
        print "error: sound %s not found" % base
    elif pygame.mixer.get_init():
        l = len(sounds[base])
        s = sounds[base][randint(0, l-1)]
        s.play()

def init():
    sound_path = join("..", "media", "sound")
    sound_files = [ f for f in listdir(sound_path) if isfile(join(sound_path,f)) ]
    for sound_file in sound_files:
        name, extension = sound_file.split(".")
        if extension == "ogg":
            base, num = name.split("-")

            if not sounds.has_key(base):
                sounds[base] = []

            s = pygame.mixer.Sound(join(sound_path,sound_file))
            sounds[base].append(s)
