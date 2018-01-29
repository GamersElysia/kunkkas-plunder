import pygame

from components import Grid, Position
from config import *
from ecs import Processor


class FogOfWar(Processor):

    def __init__(self, entity, radius=0):
        super().__init__()
        self.entity = entity
        self.radius = radius

    def update(self):
        pos = self.entity.get(Position)
        fog = self.entity.get(Grid)
        radius = self.radius

        for x in range(pos.x - radius, pos.x + radius + 1):
            if 0 <= x < fog.width:
                for y in range(pos.y - radius, pos.y + radius + 1):
                    if 0 <= y < fog.height:
                        fog[x, y] = 1
