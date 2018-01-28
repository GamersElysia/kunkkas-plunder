import pygame
import sys
import colors
import config as cfg
import hud

size = cfg.WINDOW_WIDTH, cfg.WINDOW_HEIGHT
screen = pygame.display.set_mode(size)
import tiles

pygame.display.set_caption("Kunkka's Plunder")


NUMBER_OF_TREASURES = 10


def draw_base_play_area():
    pygame.draw.rect(screen, colors.OCEAN_BLUE, hud.PLAY_AREA_BASE_RECTANGLE)


def draw_base_sidebar():
    pygame.draw.rect(screen, colors.HUD_GREY, hud.SIDEBAR_BASE_RECTANGLE)


def draw_inventory_treasures():
    space = cfg.WINDOW_WIDTH - (NUMBER_OF_TREASURES*cfg.TILE_SIZE)
    print(space)
    padding = space / (2 * NUMBER_OF_TREASURES)
    print(padding)
    for i in range(0, NUMBER_OF_TREASURES):
        screen.blit(tiles.treasure_empty, ((2*i+1)*padding + i*cfg.TILE_SIZE, cfg.WINDOW_HEIGHT * 0.95))


def draw_base_inventory():
    pygame.draw.rect(screen, colors.HUD_GREY, hud.INVENTORY_BASE_RECTANGLE)
    draw_inventory_treasures()


def draw_base_hud():
    draw_base_play_area()
    draw_base_sidebar()
    draw_base_inventory()


def draw_game():
    draw_base_hud()
    pygame.display.flip()


def main():
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
        draw_game()


if __name__ == '__main__':
    main()
