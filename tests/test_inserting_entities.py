from kunkkasplunder.game import *
from kunkkasplunder.config import *
from kunkkasplunder.ecs import World


# def test_inserting_entities_at_identical_positions():
#     #arrange
#     world = World()
#     board = world.create_entity(name='Board')
#     board.add(Grid(GRID_COLUMNS, GRID_ROWS))
#     x = 0
#     y = 0
#     treasure1 = world.create_entity()
#     treasure2 = world.create_entity()
#     #act
#     treasure1.add(Position(x, y))
#     treasure2.add(Position(x, y))

#     assert treasure1.get(Position) != treasure2.get(Position)


def test_inserting_entities_at_different_positions():
    #arrange
    print(len(positions_in_use))
    world = World()
    board = world.create_entity(name='Board')
    board.add(Grid(GRID_COLUMNS, GRID_ROWS))

    treasure1 = world.create_entity()
    treasure2 = world.create_entity()
    #act
    treasure1.add(Position(0, 0))
    treasure2.add(Position(1, 1))

    assert treasure1.get(Position) == Position(0, 0)
    assert treasure2.get(Position) == Position(1, 1)
