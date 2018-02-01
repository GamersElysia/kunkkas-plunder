# Based on https://www.pygame.org/wiki/Spritesheet

import copy

import pygame


def load(filename):
    """Create a Spritesheet from a filesystem path."""
    return Spritesheet(filename)


class Spritesheet:

    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert()

    def image_at(self, rect, colorkey=None):
        """Create a surface from the specified rectangle.

        Rect can be a pygame.Rect object or a tuple (x,y,width,height).

        colorkey is an optional transparent color for the returned image. If set
        to -1 then colorkey will sampled from the top-left pixel of the region.
        """
        if not isinstance(rect, pygame.Rect):
            rect = pygame.Rect(rect)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def images_at(self, rects, colorkey=None):
        """Loads multiple images from the sheet, given a list of rectangles."""
        return [self.image_at(rect, colorkey) for rect in rects]

    def load_grid(self, rect, nx, ny, colorkey=None):
        """Loads a grid of images and returns them as a 2D list."""
        if not isinstance(rect, pygame.Rect):
            if len(rect) == 2:
                # Allow just (width, height) tuple, defaulting (x, y) to 0, 0
                rect = (0, 0) + rect
            rect = pygame.Rect(rect)

        rows = []
        for y in range(ny):
            row_rects = [rect.move(x * rect.width, y * rect.height) for x in range(nx)]
            row = self.images_at(row_rects, colorkey)
            rows.append(row)

        return rows
