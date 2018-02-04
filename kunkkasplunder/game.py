import random
import sys

import pygame

from .components import Drawable, Position, Grid
from . import worldgen
from . import tiles
from . import hud
from . import colors
from .config import *


class DirtyTileTracker:

    def __init__(self):
        self.reset()

    def all_dirty(self):
        self.all = True

    def add(self, tile_position):
        self.dirty.append(tile_position)

    def reset(self):
        self.dirty = []
        self.all = False

    def get_dirty_tiles(self):
        if self.all:
            return True
        return self.dirty


def draw_board(screen, world, dirty_tiles):
    board = world.get_name('Board')
    grid = board.get(Grid)

    player = world.get_name('Player')
    player_position = player.get(Position)
    fog_grid = player.get(Grid)

    tile_grid = map(lambda: [tiles.fog] * grid.width, range(grid.height))

    entity_position_map = {}
    entity_position_map[player_position] = player
    for entity in world.get(has=[Drawable, Position]):
        entity_position_map[entity.get(Position)] = entity

    for y in range(grid.height):
        for x in range(grid.width):
            if dirty_tiles is not True and (x, y) not in dirty_tiles:
                continue
            if fog_grid[x, y] == 0:
                screen.blit(tiles.fog, (x * TILE_SIZE, y * TILE_SIZE))
            elif Position(x, y) in entity_position_map:
                entity = entity_position_map[Position(x, y)]
                surface = entity.get(Drawable).surface
                screen.blit(surface, (x * TILE_SIZE, y * TILE_SIZE))
            else:
                screen.blit(tiles.ocean, (x * TILE_SIZE, y * TILE_SIZE))


def update(world, **extra_data):
    extra_data['events'] = pygame.event.get()
    for event in extra_data['events']:
        if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and
                                          event.key == pygame.K_q)):
            sys.exit()
    world.update(**extra_data)


# TODO: Remove global variable.
font = None
def draw(clock, world, screen, dirty_tiles):
    hud.draw_base_hud(screen)
    draw_board(screen, world, dirty_tiles)

    # render text
    global font
    if font is None:
        font = pygame.font.Font(None, 24)
    else:
        label = font.render('FPS: %d' % round(clock.get_fps()), 1, (0, 255, 0))
        label_topleft = (screen.get_width() - max(label.get_width(), 80) - 10, 10)
        label_rect = pygame.Rect(label_topleft, label.get_size())
        pygame.draw.rect(screen, colors.HUD_GREY, label_rect)
        screen.blit(label, label_topleft)

    pygame.display.update()


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

    dtt = DirtyTileTracker()
    dtt.all_dirty()
    for processor in world.processors:
        if hasattr(processor, 'dirty_tile_tracker'):
            processor.dirty_tile_tracker = dtt

    clock = pygame.time.Clock()
    while True:
        # Handle resize events where we access the screen variable.
        for resize_event in pygame.event.get(pygame.VIDEORESIZE):
            new_width = resize_event.w
            new_height = resize_event.h
            if resize_event.w < WINDOW_WIDTH:
                new_width = WINDOW_WIDTH
            if resize_event.h < WINDOW_HEIGHT:
                new_height = WINDOW_HEIGHT
            screen = pygame.display.set_mode(
                (new_width, new_height), pygame.RESIZABLE)
            dtt.all_dirty()
        update(world)
        draw(clock, world, screen, dtt.get_dirty_tiles())
        dtt.reset()
        clock.tick()
