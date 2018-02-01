import random
import sys

import pygame

from .components import Drawable, Position, Grid
from . import worldgen
from . import tiles
from . import hud
from .config import *

def draw_board(screen, world):
    board = world.get(name='Board')[0]
    grid = board.get(Grid)

    player = world.get(name='Player')[0]
    player_position = player.get(Position)
    fog = player.get(Grid)

    for y in range(grid.height):
        for x in range(grid.width):
            screen.blit(tiles.ocean, (x * TILE_SIZE, y * TILE_SIZE))

    for thing in world.get(has=[Drawable, Position]):
        pos = thing.get(Position)
        surface = thing.get(Drawable).surface
        screen.blit(surface, (pos.x * TILE_SIZE, pos.y * TILE_SIZE))

    for y in range(grid.height):
        for x in range(grid.width):
            if fog[x, y] == 0:
                screen.blit(tiles.fog, (x * TILE_SIZE, y * TILE_SIZE))


def update(world, **extra_data):
    if pygame.event.peek(pygame.QUIT):
        sys.exit()
    extra_data['events'] = pygame.event.get()
    world.update(**extra_data)

# TODO: Remove global variable.
font = None
def draw(clock, world, screen):
    hud.draw_base_hud(screen)
    draw_board(screen, world)

    # render text
    global font
    if font is None:
        font = pygame.font.Font(None, 24)
    else:
        label = font.render('FPS: %d' % round(clock.get_fps()), 1, (0, 255, 0))
        screen.blit(label, (screen.get_width() - label.get_width() - 10, 10))

    pygame.display.flip()


def init():
    pygame.init()
    pygame.display.set_caption("Kunkka's Plunder")
    screen = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
    tiles.load()
    return screen


def run():
    screen = init()
    world = worldgen.create_world()
    clock = pygame.time.Clock()
    while True:
        # Handle resize events where we access the screen variable.
        for resize_event in pygame.event.get(pygame.VIDEORESIZE):
            screen = pygame.display.set_mode(
                (resize_event.w, resize_event.h), pygame.RESIZABLE)
        update(world)
        draw(clock, world, screen)
        clock.tick(20)
