import pygame

from components import Position
from config import *
from ecs import Processor


class KeyboardMovement(Processor):

    def __init__(self, entity):
        super().__init__()
        self.entity = entity

    def move_entity(self, event):
        pos = self.entity.get(Position)
        x, y = pos.x, pos.y
        if event.key in KEYS_UP:
            y -= 1
        if event.key in KEYS_DOWN:
            y += 1
        if event.key in KEYS_LEFT:
            x -= 1
        if event.key in KEYS_RIGHT:
            x += 1
        within_bounds = 0 <= x < GRID_COLUMNS and 0 <= y < GRID_ROWS
        if within_bounds:
            pos.x = x
            pos.y = y

    def update(self):
        for event in self.get_data('events'):
            if event.type == pygame.KEYDOWN:
                self.move_entity(event)
                # Don't process more than one movement command per update,
                # otherwise the player may skip tiles by pressing two+ keys
                # simultaneously.
                break
