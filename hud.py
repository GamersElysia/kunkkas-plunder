import pygame

import colors
from config import *
import tiles


PLAY_AREA_BASE_RECTANGLE = (0, 0, WINDOW_WIDTH * 0.8, WINDOW_HEIGHT * 0.8)
SIDEBAR_BASE_RECTANGLE = (WINDOW_WIDTH * 0.8, 0, WINDOW_WIDTH * 0.2, WINDOW_HEIGHT)
INVENTORY_BASE_RECTANGLE = (0, WINDOW_HEIGHT * 0.83, WINDOW_WIDTH, WINDOW_HEIGHT * 0.2)


def draw_base_play_area(screen):
    pygame.draw.rect(screen, colors.OCEAN_BLUE, PLAY_AREA_BASE_RECTANGLE)


def draw_base_sidebar(screen):
    pygame.draw.rect(screen, colors.HUD_GREY, SIDEBAR_BASE_RECTANGLE)


def draw_inventory_treasures(screen):
    space = WINDOW_WIDTH - (NUMBER_OF_TREASURES * TILE_SIZE)
    padding = space / (2 * NUMBER_OF_TREASURES)
    for i in range(0, NUMBER_OF_TREASURES):
        screen.blit(tiles.treasure_empty, ((2 * i + 1) *
                                           padding + i * TILE_SIZE, WINDOW_HEIGHT * 0.95))


def draw_base_inventory(screen):
    pygame.draw.rect(screen, colors.HUD_GREY, INVENTORY_BASE_RECTANGLE)
    draw_inventory_treasures(screen)


def draw_base_hud(screen):
    draw_base_play_area(screen)
    draw_base_sidebar(screen)
    draw_base_inventory(screen)
