import spritesheet
import config as cfg


tiles = spritesheet.load('tiles.png').load_grid((cfg.TILE_SIZE, cfg.TILE_SIZE), cfg.TILE_COLUMNS, cfg.TILE_ROWS)

ocean = tiles[0][0]
fog = tiles[0][1]

island_visited = tiles[0][2]
island_unvisited = tiles[0][3]

weapon_sword_up = tiles[1][0]
weapon_sword_down = tiles[1][1]
weapon_cannon_up = tiles[1][2]
weapon_cannon_down = tiles[1][3]
weapon_axe_up = tiles[2][0]
weapon_axe_down = tiles[2][1]
weapon_arrows_up = tiles[2][2]
weapon_arrows_down = tiles[2][3]
weapon_harpoon_up = tiles[3][0]
weapon_harpoon_down = tiles[3][1]
weapon_daggers_up = tiles[3][2]
weapon_daggers_down = tiles[3][3]

treasure_emerald = tiles[4][0]
treasure_gold_sword = tiles[4][1]
treasure_gold_sceptre = tiles[4][2]
treasure_pearl = tiles[4][3]
treasure_crown = tiles[5][0]
treasure_ruby_ring = tiles[5][1]
treasure_silver_chalice = tiles[5][2]
treasure_chest = tiles[5][3]
treasure_necklace = tiles[6][0]
treasure_map = tiles[6][1]

sextant = tiles[6][2]
spyglass = tiles[6][3]
tar = tiles[7][0]
iceberg = tiles[7][1]
whirlpool = tiles[7][2]

enemy_pirate_ship = tiles[7][3]
enemy_ghost_ship = tiles[8][0]
enemy_kraken = tiles[8][1]
enemy_phoenix = tiles[8][2]
enemy_siren = tiles[8][3]

player_alive = tiles[9][0]
player_dead = tiles[9][1]

treasure_onyx_cross = tiles[9][2]
treasure_empty = tiles[9][3]

shown_enemy = tiles[10][0]
shown_treasure = tiles[10][1]
