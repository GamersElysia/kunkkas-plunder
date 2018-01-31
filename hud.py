import pygame

import colors
from config import *
import tiles


def calc_play_area_base_rectangle(rect):
    return (0, 0, rect.width * 0.8, rect.height * 0.8)


def calc_sidebar_base_rectangle(rect):
    return (rect.width * 0.8, 0, rect.width * 0.2, rect.height)


def calc_inventory_base_rectangle(rect):
    return (0, rect.height * 0.83, rect.width, rect.height * 0.2)


def draw_base_play_area(screen):
    rect = calc_play_area_base_rectangle(screen.get_rect())
    pygame.draw.rect(screen, colors.OCEAN_BLUE, rect)


def draw_base_sidebar(screen):
    rect = calc_sidebar_base_rectangle(screen.get_rect())
    pygame.draw.rect(screen, colors.HUD_GREY, rect)


def draw_inventory_treasures(screen):
    space = screen.get_width() - (NUMBER_OF_TREASURES * TILE_SIZE)
    padding = space / (2 * NUMBER_OF_TREASURES)
    for i in range(0, NUMBER_OF_TREASURES):
        screen.blit(
            tiles.treasure_empty,
            ((2 * i + 1) * padding + i * TILE_SIZE,
            screen.get_height() * 0.95))


def draw_base_inventory(screen):
    rect = calc_inventory_base_rectangle(screen.get_rect())
    pygame.draw.rect(screen, colors.HUD_GREY, rect)
    draw_inventory_treasures(screen)


def draw_base_hud(screen):
    draw_base_play_area(screen)
    draw_base_sidebar(screen)
    draw_base_inventory(screen)
