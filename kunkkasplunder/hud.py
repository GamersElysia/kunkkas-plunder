import pygame

from . import colors
from .config import *
from . import tiles


def calc_play_area_base_rectangle(rect):
    return pygame.Rect(0, 0, GRID_COLUMNS * TILE_SIZE, GRID_ROWS * TILE_SIZE)


def calc_sidebar_base_rectangle(rect):
    play_area = calc_play_area_base_rectangle(rect)
    return pygame.Rect(play_area.width, 0, rect.width - play_area.width, rect.height)


def calc_inventory_base_rectangle(rect):
    play_area = calc_play_area_base_rectangle(rect)
    return pygame.Rect(0, play_area.height, rect.width, rect.height - play_area.height)


def draw_base_sidebar(screen):
    rect = calc_sidebar_base_rectangle(screen.get_rect())
    pygame.draw.rect(screen, colors.HUD_GREY, rect)


def draw_inventory_treasures(screen):
    space = screen.get_width() - (NUMBER_OF_TREASURES * TILE_SIZE)
    padding = space / (2 * NUMBER_OF_TREASURES)
    for i in range(0, NUMBER_OF_TREASURES):
        screen.blit(
            tiles.treasure_empty,
            ((2 * i + 1) * padding + i * TILE_SIZE, screen.get_height() * 0.95))


def draw_base_inventory(screen):
    rect = calc_inventory_base_rectangle(screen.get_rect())
    pygame.draw.rect(screen, colors.HUD_GREY, rect)
    draw_inventory_treasures(screen)


def draw_base_hud(screen):
    draw_base_sidebar(screen)
    draw_base_inventory(screen)
