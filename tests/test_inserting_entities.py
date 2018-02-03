import os
from kunkkasplunder.game import *
from kunkkasplunder.config import *


os.environ["SDL_VIDEODRIVER"] = "dummy"


# Need to get rid of this.
# Currently it's required to post messages to the pygame event queue.
pygame.init()



def test_inserting_entities_at_identical_positions():
    #arrange
    world = create_world()
    board = world.create_entity(name='Board')
    board.add(Grid(GRID_COLUMNS, GRID_ROWS))
    x = 0
    y = 0
    treasure1 = world.create_entity()
    treasure2 = world.create_entity()
    #act
    add_position_to_entity(treasure1, Position(x, y))
    add_position_to_entity(treasure2, Position(x, y))

    assert treasure1.get(Position) != treasure2.get(Position)

def test_inserting_entities_at_different_positions():
    #arrange
    print(len(positions_in_use))
    world = create_world()
    board = world.create_entity(name='Board')
    board.add(Grid(GRID_COLUMNS, GRID_ROWS))

    treasure1 = world.create_entity()
    treasure2 = world.create_entity()
    #act
    add_position_to_entity(treasure1, Position(0, 0))
    add_position_to_entity(treasure2, Position(1, 1))

    assert treasure1.get(Position) == Position(0, 0)
    assert treasure2.get(Position) == Position(1, 1)
