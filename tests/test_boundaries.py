from kunkkasplunder.game import *
from kunkkasplunder.config import *
from kunkkasplunder import worldgen


def move_player_many_times(key):
    world = worldgen.create_world()
    repeat = max(GRID_COLUMNS, GRID_ROWS) * 2
    for _ in range(repeat):
        event = pygame.event.Event(KEYDOWN, key=key)
        pygame.event.post(event)
        update(world)
    return world.get(name="Player")[0].get(Position)


def test_top_boundary():
    pos = move_player_many_times(K_UP)
    assert pos.y == 0


def test_bottom_boundary():
    pos = move_player_many_times(K_DOWN)
    assert pos.y == GRID_ROWS - 1


def test_left_boundary():
    pos = move_player_many_times(K_LEFT)
    assert pos.x == 0


def test_right_boundary():
    pos = move_player_many_times(K_RIGHT)
    assert pos.x == GRID_COLUMNS - 1
