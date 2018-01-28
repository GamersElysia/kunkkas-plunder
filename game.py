import pygame
import sys
import colors
import config
import hud as hud


size = config.WINDOW_WIDTH, config.WINDOW_HEIGHT
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Kunkka's Plunder")


def draw_base_play_area():
    pygame.draw.rect(screen, colors.OCEAN_BLUE, hud.PLAY_AREA_BASE_RECTANGLE)


def draw_base_sidebar():
    pygame.draw.rect(screen, colors.HUD_GREY, hud.SIDEBAR_BASE_RECTANGLE)


def draw_base_inventory():
    pygame.draw.rect(screen, colors.HUD_GREY, hud.INVENTORY_BASE_RECTANGLE)


def draw_base_hud():
    draw_base_play_area()
    draw_base_sidebar()
    draw_base_inventory()
    pygame.display.flip()


def draw_game():
    draw_base_hud()


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    draw_game()
