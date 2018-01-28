import pygame
import sys
import colors
from config import *
import hud


size = WINDOW_WIDTH, WINDOW_HEIGHT
screen = pygame.display.set_mode(size)
import tiles

pygame.display.set_caption("Kunkka's Plunder")


NUMBER_OF_TREASURES = 10


def draw_base_play_area():
    pygame.draw.rect(screen, colors.OCEAN_BLUE, hud.PLAY_AREA_BASE_RECTANGLE)


def draw_base_sidebar():
    pygame.draw.rect(screen, colors.HUD_GREY, hud.SIDEBAR_BASE_RECTANGLE)


def draw_inventory_treasures():
    space = WINDOW_WIDTH - (NUMBER_OF_TREASURES*TILE_SIZE)
    print(space)
    padding = space / (2 * NUMBER_OF_TREASURES)
    print(padding)
    for i in range(0, NUMBER_OF_TREASURES):
        screen.blit(tiles.treasure_empty, ((2*i+1)*padding + i*TILE_SIZE, WINDOW_HEIGHT * 0.95))


def draw_base_inventory():
    pygame.draw.rect(screen, colors.HUD_GREY, hud.INVENTORY_BASE_RECTANGLE)
    draw_inventory_treasures()


def draw_base_hud():
    draw_base_play_area()
    draw_base_sidebar()
    draw_base_inventory()


def test_spritesheet():
    t = tiles.tiles
    for i in range(len(t)):
        row = t[i]
        for j in range(len(row)):
            tile = row[j]
            screen.blit(tile, (40 * j + 20, 40 * i + 20))


def draw_board():
    w, h = game_state['board']['size']
    for y in range(h):
        for x in range(w):
            if game_state['board']['fog'][y][x] > 0:
                tile = tiles.fog
            else:
                tile = tiles.ocean
            if (x, y) == game_state['player']['position']:
                tile = tiles.player_alive
            screen.blit(tile, (x * TILE_SIZE, y * TILE_SIZE))


def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x, y = game_state['player']['position']
            if event.key == pygame.K_UP:
                y -= 1
            if event.key == pygame.K_DOWN:
                y += 1
            if event.key == pygame.K_LEFT:
                x -= 1
            if event.key == pygame.K_RIGHT:
                x += 1
            game_state['player']['position'] = x, y

    # Remove fog at player position
    x, y = game_state['player']['position']
    game_state['board']['fog'][y][x] = 0


def draw_game():
    draw_base_hud()
    draw_board()
    # test_spritesheet()
    pygame.display.flip()


game_state = {
    'board': {
        'size': (GRID_COLUMNS, GRID_ROWS),
        'fog': [[1] * GRID_COLUMNS for i in range(GRID_ROWS)]
    },
    'player': {
        'position': (7, 9)
    }
}


def main():
    while True:
        update()
        draw_game()


if __name__ == '__main__':
    main()
