import pytest

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


def test_adding_too_many_entities_to_world():
    world = World()
    board = world.create_entity(name='Board')
    board.add(Grid(GRID_COLUMNS, GRID_ROWS))

    too_many = GRID_COLUMNS * GRID_ROWS + 1
    with pytest.raises(worldgen.Error) as err_info:
        for _ in range(too_many):
            pos = worldgen.place_drawable_entity_randomly(world, None)
    assert 'Unable to place entity' in str(err_info.value)
    assert len(world.get(has=[Position])) == too_many - 1


def test_correct_number_of_entities():
    world = worldgen.create_world()

    total_should_be = (
        1 +  # Player
        NUMBER_OF_TREASURES +
        NUMBER_OF_ENEMIES +
        NUMBER_OF_HAZARDS +
        NUMBER_OF_ISLANDS +
        NUMBER_OF_TOOLS)

    total = len(world.get(has=[Drawable, Position]))

    assert total_should_be == total
