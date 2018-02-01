import random
import sys

import pygame

from ecs import World, Entity
from components import Drawable, Position, Grid
from processors import FogOfWar, KeyboardMovement
import colors
from config import *


def draw_board(screen, world):
    board = world.get(name='Board')[0]
    grid = board.get(Grid)

    player = world.get(name='Player')[0]
    player_position = player.get(Position)
    fog = player.get(Grid)

    for y in range(grid.height):
        for x in range(grid.width):
            screen.blit(tiles.ocean, (x * TILE_SIZE, y * TILE_SIZE))

    for thing in world.get(has=[Drawable, Position]):
        pos = thing.get(Position)
        surface = thing.get(Drawable).surface
        screen.blit(surface, (pos.x * TILE_SIZE, pos.y * TILE_SIZE))

    for y in range(grid.height):
        for x in range(grid.width):
            if fog[x, y] == 0:
                screen.blit(tiles.fog, (x * TILE_SIZE, y * TILE_SIZE))


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

    add_things(world)
    add_treasures(world)
    player = world.create_entity(name='Player')
    player.add(Position(GRID_COLUMNS // 2, GRID_ROWS // 2))
    player.add(Grid(GRID_COLUMNS, GRID_ROWS, 0)) # Represents vision/fog.
    player.add(Drawable(tiles.player_alive))
    world.add_processor(KeyboardMovement(player))
    world.add_processor(FogOfWar(player, radius=1))

    return world


def add_entity_to_world(world, tile):
    entity = world.create_entity()
    x = random.randrange(0, GRID_COLUMNS)
    y = random.randrange(0, GRID_ROWS)
    entity.add(Position(x, y))
    entity.add(Drawable(tile))


def add_treasures(world):
    treasure_tiles = [
        tiles.treasure_emerald,
        tiles.treasure_gold_sword,
        tiles.treasure_gold_sceptre,
        tiles.treasure_pearl,
        tiles.treasure_crown,
        tiles.treasure_ruby_ring,
        tiles.treasure_silver_chalice,
        tiles.treasure_chest,
        tiles.treasure_necklace,
        tiles.treasure_map
    ]
    for i in range(NUMBER_OF_TREASURES):
        add_entity_to_world(world, treasure_tiles[i])


def add_things(world):
    thing_tiles = [
        tiles.island_visited,
        tiles.island_unvisited,

        tiles.sextant,
        tiles.spyglass,
        tiles.tar,
        tiles.iceberg,
        tiles.whirlpool,

        tiles.enemy_pirate_ship,
        tiles.enemy_ghost_ship,
        tiles.enemy_kraken,
        tiles.enemy_phoenix,
        tiles.enemy_siren,
    ]
    for i in range(0, 7):
        for j in range(0, len(thing_tiles)):
            add_entity_to_world(world, thing_tiles[j])


def main():
    world = create_world()
    while True:
        update(world)
        draw(screen, world)
        pygame.time.wait(50)


if __name__ == '__main__':
    size = WINDOW_WIDTH, WINDOW_HEIGHT
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Kunkka's Plunder")
    # These need to be imported after the game window is created.
    import tiles
    import hud

    main()
