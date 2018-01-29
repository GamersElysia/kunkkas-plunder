import unittest

import pygame

import game


class TestBoundaryConditions(unittest.TestCase):
    def test_given_input_that_would_move_out_of_x_bounds_when_player_is_moved_then_player_stays_in_x_bounds(self):
        game.game_state['player']['position'] = (0, 0)
        event = pygame.event.Event(pygame.KEYDOWN, {'unicode': '', 'key': 276, 'mod': 0, 'scancode': 75})
        game.move_player(event)
        self.assertEqual(game.game_state['player']['position'], (0, 0))

    def test_given_input_that_would_move_out_of_y_bounds_when_player_is_moved_then_player_stays_in_y_bounds(self):
        game.game_state['player']['position'] = (0, 0)
        event = pygame.event.Event(pygame.KEYDOWN, {'unicode': '', 'key': 273, 'mod': 0, 'scancode': 72})
        game.move_player(event)
        self.assertEqual(game.game_state['player']['position'], (0, 0))

    def test_given_valid_input_when_player_is_moved_then_players_location_changes(self):
        game.game_state['player']['position'] = (0, 0)
        event = pygame.event.Event(pygame.KEYDOWN, {'unicode': '3', 'key': 259, 'mod': 0, 'scancode': 81})
        game.move_player(event)
        self.assertEqual(game.game_state['player']['position'], (1, 1))


if __name__ == '__main__':
    unittest.main()
