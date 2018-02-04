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
    inventory_area = calc_inventory_base_rectangle(screen.get_rect())
    whitespace = inventory_area.width - NUMBER_OF_TREASURES * TILE_SIZE
    padding = whitespace / (NUMBER_OF_TREASURES + 1)
    y = inventory_area.y + inventory_area.height / 2 - TILE_SIZE / 2
    for i in range(0, NUMBER_OF_TREASURES):
        x = inventory_area.x + padding * (i + 1) + TILE_SIZE * i
        screen.blit(tiles.treasure_empty, (x, y))


def draw_base_inventory(screen):
    rect = calc_inventory_base_rectangle(screen.get_rect())
    pygame.draw.rect(screen, colors.HUD_GREY, rect)
    draw_inventory_treasures(screen)


def draw_base_hud(screen):
    draw_base_sidebar(screen)
    draw_base_inventory(screen)
