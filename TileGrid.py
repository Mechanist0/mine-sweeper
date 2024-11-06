from Tile import Tile
import random
import pygame

class TileGrid:
    grid = []
    width = 0
    height = 0
    difficulty = 0

    def __init__(self, width: int, height: int, size: int, difficulty: float, test_grid: [[]] = None):
        self.width = width
        self.height = height
        self.size = size
        self.difficulty = difficulty
        self.test_grid = test_grid

    def build_grid(self):
        # Test grid will look like [[1, 1, 1, 0],[0, 0, 0, 0],[1, 1, 1, 1],[0, 0, 0, 0]]
        if self.test_grid is not None:
            print("!Test Grid Not None, Entering Testing Mode!")
            for y in range(len(self.test_grid)):
                row = []
                for x in range(len(self.test_grid[y])):
                    size = 10
                    row.append(Tile(x*size, y*size, size, True if self.test_grid[y][x] == 1 else False))
                self.grid.append(row)
        else:
            for y in range(self.height):
                row = []
                for x in range(self.width):
                    row.append(Tile(x*self.size, y*self.size, self.size, True if random.random() < self.difficulty else False))
                self.grid.append(row)


    def calculate_nearby(self):
        # For every tile, count the number of mines directly around our tile
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                mine_count = 0
                # Handle Corner Cases
                if x==0 and y==0: # Top Left
                    print("top left")
                    if self.grid[y][x+1].armed:
                        mine_count += 1
                    if self.grid[y+1][x].armed:
                        mine_count += 1
                    if self.grid[y+1][x+1].armed:
                        mine_count += 1
                elif x == 0 and y == len(self.grid) - 1: # Bottom Left
                    print("Bottom left")
                    if self.grid[y-1][x].armed:
                        mine_count += 1
                    if self.grid[y-1][x+1].armed:
                        mine_count += 1
                    if self.grid[y][x + 1].armed:
                        mine_count += 1
                elif x == len(self.grid[y])-1 and y == 0: # Top Right
                    print("Top Right")
                    if self.grid[y + 1][x - 1].armed:
                        mine_count += 1
                    if self.grid[y + 1][x].armed:
                        mine_count += 1
                    if self.grid[y][x - 1].armed:
                        mine_count += 1
                elif x == len(self.grid[y])-1 and y == len(self.grid) - 1: # Bottom Right
                    print("Bottom Right")
                    if self.grid[y - 1][x-1].armed:
                        mine_count += 1
                    if self.grid[y - 1][x].armed:
                        mine_count += 1
                    if self.grid[y][x-1].armed:
                        mine_count += 1

                # Handle Edge Cases
                elif x == 0 and y != 0 and y!= len(self.grid) - 1: # Left Edge
                    if self.grid[y+1][x].armed:
                        mine_count += 1
                    if self.grid[y+1][x+1].armed:
                        mine_count += 1
                    if self.grid[y][x+1].armed:
                        mine_count += 1
                    if self.grid[y-1][x+1].armed:
                        mine_count += 1
                    if self.grid[y-1][x].armed:
                        mine_count += 1

                elif x == len(self.grid[y])-1 and y != 0 and y!= len(self.grid) - 1: # Right Edge
                    if self.grid[y + 1][x].armed:
                        mine_count += 1
                    if self.grid[y + 1][x - 1].armed:
                        mine_count += 1
                    if self.grid[y][x - 1].armed:
                        mine_count += 1
                    if self.grid[y - 1][x - 1].armed:
                        mine_count += 1
                    if self.grid[y - 1][x].armed:
                        mine_count += 1
                elif y == 0 and x != 0 and x!= len(self.grid[y])-1: # Top Edge
                    if self.grid[y][x-1].armed:
                        mine_count += 1
                    if self.grid[y][x+1].armed:
                        mine_count += 1
                    if self.grid[y+1][x-1].armed:
                        mine_count += 1
                    if self.grid[y+1][x].armed:
                        mine_count += 1
                    if self.grid[y+1][x+1].armed:
                        mine_count += 1
                elif y == len(self.grid) - 1 and x != 0 and x!= len(self.grid[y])-1: # Bottom Edge
                    if self.grid[y][x - 1].armed:
                        mine_count += 1
                    if self.grid[y][x + 1].armed:
                        mine_count += 1
                    if self.grid[y - 1][x - 1].armed:
                        mine_count += 1
                    if self.grid[y - 1][x].armed:
                        mine_count += 1
                    if self.grid[y - 1][x + 1].armed:
                        mine_count += 1

                # Everything else
                else:
                    if self.grid[y - 1][x - 1].armed:
                        mine_count += 1
                    if self.grid[y - 1][x].armed:
                        mine_count += 1
                    if self.grid[y - 1][x + 1].armed:
                        mine_count += 1
                    if self.grid[y][x-1].armed:
                        mine_count += 1
                    if self.grid[y][x+1].armed:
                        mine_count += 1
                    if self.grid[y + 1][x - 1].armed:
                        mine_count += 1
                    if self.grid[y + 1][x].armed:
                        mine_count += 1
                    if self.grid[y + 1][x + 1].armed:
                        mine_count += 1

                self.grid[y][x].danger = mine_count

    def uncover_tile(self, x, y, flag):
        tile: Tile = self.grid[y][x]
        if tile.armed:
            return -1
        elif tile.state == 0 and flag:
            tile.state = 1
        elif tile.state == 0 and not flag:
            tile.state = 2
        elif tile.state == 1:
            tile.state = 0

        if tile.danger == 0:
            return 1

    def draw_grid(self, screen):
        for y in self.grid:
            for x in y:
                x.draw(screen)

    def peak_danger_grid(self):
        for y in range(len(self.grid)):
            print('[')
            for x in range(len(self.grid[y])):
                print('[' + str(self.grid[y][x].danger) + ']')
            print(']\n')
