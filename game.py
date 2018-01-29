import sys

import pygame

from ecs import World, Entity
from components import Position, Grid
from processors import FogOfWar, KeyboardMovement
import colors
from config import *


def draw_board(screen, world):
    board = world.get(name='Board')
    grid = board.get(Grid)

    player = world.get(name='Player')
    player_position = player.get(Position)
    fog = player.get(Grid)

    for y in range(grid.height):
        for x in range(grid.width):
            if fog[x, y] == 0:
                tile = tiles.fog
            else:
                tile = tiles.ocean
            if x == player_position.x and y == player_position.y:
                tile = tiles.player_alive
            screen.blit(tile, (x * TILE_SIZE, y * TILE_SIZE))


def update(world):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Dispatch events to interested processors
        for processor in world.processors:
            if hasattr(processor, '_event_handlers'):
                if event.type in processor._event_handlers:
                    for fn_name in processor._event_handlers[event.type]:
                        getattr(processor, fn_name)(event)

    for processor in world.processors:
        processor.update()


def draw(screen, world):
    hud.draw_base_hud(screen)
    draw_board(screen, world)
    pygame.display.flip()


def create_world():
    world = World()

    board = world.create_entity(name='Board')
    board.add(Grid(GRID_COLUMNS, GRID_ROWS))

    player = world.create_entity(name='Player')
    player.add(Position(GRID_COLUMNS // 2, GRID_ROWS // 2))
    player.add(Grid(GRID_COLUMNS, GRID_ROWS, 0)) # Represents vision/fog.
    world.add_processor(KeyboardMovement(player))
    world.add_processor(FogOfWar(player))

    return world


def main():
    world = create_world()
    while True:
        update(world)
        draw(screen, world)


if __name__ == '__main__':
    size = WINDOW_WIDTH, WINDOW_HEIGHT
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Kunkka's Plunder")
    # These need to be imported after the game window is created.
    import tiles
    import hud

    main()
