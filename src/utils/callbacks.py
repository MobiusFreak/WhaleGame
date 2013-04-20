from pygame.locals import *

callbacks = {KEYDOWN : {}, KEYUP : {}, QUIT : []}

def register_event(evt, call, key = None):
    if evt == KEYDOWN or evt == KEYUP:
        if callbacks[evt].has_key(key):
            callbacks[evt][key].append(call)
        else:
            callbacks[evt][key]=[call]
    else:
        callbacks[evt].append(call)

def unregister_event(evt, call, key = None):
    if evt == KEYDOWN or evt == KEYUP:
        if callbacks[evt].has_key(key):
            if call in callbacks[evt][key]:
                callbacks[evt][key].remove(call)
    else:
        if call in callbacks[evt]:
            callbacks[evt].remove(call)

