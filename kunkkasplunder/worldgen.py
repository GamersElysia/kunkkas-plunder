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
    board.add(Grid(GRID_COLUMNS, GRID_ROWS))

    player = world.create_entity(name='Player')
    player_pos = Position(GRID_COLUMNS // 2, GRID_ROWS // 2)
    player.add(player_pos)
    player.add(Grid(GRID_COLUMNS, GRID_ROWS, 0))  # Represents vision/fog.
    player.add(Drawable(tiles.player_alive))

    add_things(world)

    world.add_processor(KeyboardMovement(player))
    world.add_processor(FogOfWar(player, radius=0))

    return world


def add_things(world):
    entity_tiles_to_add = copy.copy(tiles.treasures())

    for _ in range(NUMBER_OF_ISLANDS):
        entity_tiles_to_add.append(tiles.island_unvisited)

    for _ in range(NUMBER_OF_TOOLS):
        entity_tiles_to_add.append(random.choice(tiles.tools()))

    for _ in range(NUMBER_OF_HAZARDS):
        entity_tiles_to_add.append(random.choice(tiles.hazards()))

    for _ in range(NUMBER_OF_ENEMIES):
        entity_tiles_to_add.append(random.choice(tiles.enemies()))

    player = world.get(name='Player')[0]
    inhabited = [player.get(Position)]
    for tile in entity_tiles_to_add:
        pos = place_drawable_entity_randomly(world, tile, inhabited)
        inhabited.append(pos)


def place_drawable_entity_randomly(world, surface, inhabited_positions=None):
    if inhabited_positions is None:
        inhabited_positions = []

    grid = world.get(name='Board')[0].get(Grid)
    if grid.width * grid.height <= len(inhabited_positions):
        raise Error('Unable to place entity in world due to all tiles being inhabited')

    while True:
        pos = Position(
            random.randrange(0, GRID_COLUMNS),
            random.randrange(0, GRID_ROWS))
        if pos not in inhabited_positions:
            break

    entity = world.create_entity()
    entity.add(pos)
    entity.add(Drawable(surface))

    return pos


class Error(Exception):
    pass
