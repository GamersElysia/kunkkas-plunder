# This file is needed so modules can be imported from the top-level in test
# modules.

import os

import pygame


os.environ["SDL_VIDEODRIVER"] = "dummy"


# Need to get rid of this.
# Currently it's required to post messages to the pygame event queue.
pygame.init()
