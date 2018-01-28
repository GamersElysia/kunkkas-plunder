import pygame
import sys
import colors
import config
import hud
import spritesheet


size = config.WINDOW_WIDTH, config.WINDOW_HEIGHT
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Kunkka's Plunder")


tiles = spritesheet.load('tiles.png').load_grid((32, 32), 4, 11)


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


def test_spritesheet():
    for i in range(len(tiles)):
        row = tiles[i]
        for j in range(len(row)):
            tile = tiles[i][j]
            screen.blit(tile, (40 * j + 20, 40 * i + 20))


def draw_game():
    draw_base_hud()
    test_spritesheet()
    pygame.display.flip()


def main():
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
        draw_game()


if __name__ == '__main__':
    main()
