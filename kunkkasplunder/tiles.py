from collections import namedtuple
import os
import sys

from . import spritesheet
from .config import TILE_SIZE, TILE_COLUMNS, TILE_ROWS


TileCoord = namedtuple('TileCoord', ['x', 'y'])


def load():
    module = sys.modules[__name__]
    members = dir(module)
    image_path = os.path.join(os.path.dirname(__file__), 'assets', 'tiles.png')
    tile_spritesheet = spritesheet.load(image_path).load_grid(
        (TILE_SIZE, TILE_SIZE), TILE_COLUMNS, TILE_ROWS)
    for identifier in members:
        value = getattr(module, identifier)
        if type(value) is TileCoord:
            setattr(module, identifier, tile_spritesheet[value.y][value.x])


ocean = TileCoord(0, 0)
fog = TileCoord(1, 0)

island_visited = TileCoord(2, 0)
island_unvisited = TileCoord(3, 0)

weapon_sword_up = TileCoord(0, 1)
weapon_sword_down = TileCoord(1, 1)
weapon_cannon_up = TileCoord(2, 1)
weapon_cannon_down = TileCoord(3, 1)
weapon_axe_up = TileCoord(0, 2)
weapon_axe_down = TileCoord(1, 2)
weapon_arrows_up = TileCoord(2, 2)
weapon_arrows_down = TileCoord(3, 2)
weapon_harpoon_up = TileCoord(0, 3)
weapon_harpoon_down = TileCoord(1, 3)
weapon_daggers_up = TileCoord(2, 3)
weapon_daggers_down = TileCoord(3, 3)

treasure_emerald = TileCoord(0, 4)
treasure_gold_sword = TileCoord(1, 4)
treasure_gold_sceptre = TileCoord(2, 4)
treasure_pearl = TileCoord(3, 4)
treasure_crown = TileCoord(0, 5)
treasure_ruby_ring = TileCoord(1, 5)
treasure_silver_chalice = TileCoord(2, 5)
treasure_chest = TileCoord(3, 5)
treasure_necklace = TileCoord(0, 6)
treasure_map = TileCoord(1, 6)

sextant = TileCoord(2, 6)
spyglass = TileCoord(3, 6)
tar = TileCoord(0, 7)
iceberg = TileCoord(1, 7)
whirlpool = TileCoord(2, 7)

enemy_pirate_ship = TileCoord(3, 7)
enemy_ghost_ship = TileCoord(0, 8)
enemy_kraken = TileCoord(1, 8)
enemy_phoenix = TileCoord(2, 8)
enemy_siren = TileCoord(3, 8)

player_alive = TileCoord(0, 9)
player_dead = TileCoord(1, 9)

treasure_onyx_cross = TileCoord(2, 9)
treasure_empty = TileCoord(3, 9)

shown_enemy = TileCoord(0, 10)
shown_treasure = TileCoord(1, 10)


def treasures():
    return [
        treasure_emerald,
        treasure_gold_sword,
        treasure_gold_sceptre,
        treasure_pearl,
        treasure_crown,
        treasure_ruby_ring,
        treasure_silver_chalice,
        treasure_chest,
        treasure_necklace,
        treasure_map,
    ]


def enemies():
    return [
        enemy_pirate_ship,
        enemy_ghost_ship,
        enemy_kraken,
        enemy_phoenix,
        enemy_siren,
    ]


def tools():
    return [
        sextant,
        spyglass,
        tar,
    ]


def hazards():
    return [
        iceberg,
        whirlpool,
    ]
