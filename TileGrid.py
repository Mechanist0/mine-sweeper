from Tile import Tile
import random
import pygame

class TileGrid:
    grid = []
    width = 0
    height = 0
    difficulty = 0

    def __init__(self, width: int, height: int, size: int, difficulty: float):
        self.width = width
        self.height = height
        self.size = size
        self.difficulty = difficulty

    def build_grid(self):
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(Tile(x*self.size, y*self.size, self.size, True if random.random() > self.difficulty else False))
            self.grid.append(row)

    def draw_grid(self, screen):
        for y in self.grid:
            for x in y:
                x.draw(screen)