import copy
import random

from .components import Drawable, Position, Grid
from .ecs import World
from .processors import FogOfWar, KeyboardMovement
from . import tiles
from .config import *


def create_world():
    world = World()

    board = world.create_entity(name='Board')
    grid = Grid(GRID_COLUMNS, GRID_ROWS)
    board.add(grid)

    player = world.create_entity(name='Player')
    player_pos = Position(GRID_COLUMNS // 2, GRID_ROWS // 2)
    player.add(player_pos)
    player.add(Grid(GRID_COLUMNS, GRID_ROWS, 0))  # Represents vision/fog.
    player.add(Drawable(tiles.player_alive))
    grid[player_pos] = player

    add_things(world)

    world.add_processor(KeyboardMovement(player))
    world.add_processor(FogOfWar(player, radius=0))

    return world


def add_things(world):
    # One of each treasure.
    entity_tiles_to_add = copy.copy(tiles.treasures())

    for _ in range(NUMBER_OF_ISLANDS):
        entity_tiles_to_add.append(tiles.island_unvisited)

    for _ in range(NUMBER_OF_TOOLS):
        entity_tiles_to_add.append(random.choice(tiles.tools()))

    for _ in range(NUMBER_OF_HAZARDS):
        entity_tiles_to_add.append(random.choice(tiles.hazards()))

    for _ in range(NUMBER_OF_ENEMIES):
        entity_tiles_to_add.append(random.choice(tiles.enemies()))

    for tile in entity_tiles_to_add:
        pos = place_drawable_entity_randomly(world, tile)


def place_drawable_entity_randomly(world, surface):
    grid = world.get_name('Board').get(Grid)


    if not any(grid[i] is None for i in grid):
        raise Error('Unable to place entity in world - Grid is full')

    while True:
        pos = Position(
            random.randrange(0, grid.width),
            random.randrange(0, grid.height))
        if grid[pos] is None:
            break

    entity = world.create_entity()
    entity.add(pos)
    entity.add(Drawable(surface))
    grid[pos] = entity

    return pos


class Error(Exception):
    pass
