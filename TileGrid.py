from Tile import Tile
import random
import pygame
import functools

class TileGrid:
    grid = []
    width = 0
    height = 0
    difficulty = 0

    def __init__(self, width: int, height: int, size: int, difficulty: float, test_grid: [[]] = None, offset_x = 0, offset_y = 0):
        self.width = width
        self.height = height
        self.size = size
        self.difficulty = difficulty
        self.test_grid = test_grid
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.mines = 0

    def build_grid(self):
        # Test grid will look like [[1, 1, 1, 0],[0, 0, 0, 0],[1, 1, 1, 1],[0, 0, 0, 0]]
        if self.test_grid is not None:
            print("!Test Grid Not None, Entering Testing Mode!")
            for y in range(len(self.test_grid)):
                row = []
                for x in range(len(self.test_grid[y])):
                    size = 10
                    armed = True if self.test_grid[y][x] == 1 else False
                    row.append(Tile((x*size) + self.offset_x, (y*size) + self.offset_y, size, armed))
                    if armed:
                        self.mines += 1

                self.grid.append(row)
        else:
            for y in range(self.height):
                row = []
                for x in range(self.width):
                    armed = True if random.random() < self.difficulty else False
                    row.append(Tile((x*self.size) + self.offset_x, (y*self.size) + self.offset_y, self.size, armed))
                    if armed:
                        self.mines += 1
                self.grid.append(row)
        # Calculate Danger
        self.calculate_danger()

    def get_surrounding(self, x, y):
        surrounding = []
        # Handle Corner Cases
        if x == 0 and y == 0:  # Top Left
            surrounding.append(self.grid[y][x+1])
            surrounding.append(self.grid[y+1][x])
            surrounding.append(self.grid[y+1][x+1])
        elif x == 0 and y == len(self.grid) - 1:  # Bottom Left
            surrounding.append(self.grid[y][x+1])
            surrounding.append(self.grid[y-1][x])
            surrounding.append(self.grid[y-1][x+1])
        elif x == len(self.grid[y]) - 1 and y == 0:  # Top Right
            surrounding.append(self.grid[y+1][x-1])
            surrounding.append(self.grid[y+1][x])
            surrounding.append(self.grid[y][x-1])
        elif x == len(self.grid[y]) - 1 and y == len(self.grid) - 1:  # Bottom Right
            surrounding.append(self.grid[y-1][x-1])
            surrounding.append(self.grid[y-1][x])
            surrounding.append(self.grid[y][x-1])
        # Handle Edge Cases
        elif x == 0 and y != 0 and y != len(self.grid) - 1:  # Left Edge
            surrounding.append(self.grid[y+1][x])
            surrounding.append(self.grid[y+1][x+1])
            surrounding.append(self.grid[y][x+1])
            surrounding.append(self.grid[y-1][x+1])
            surrounding.append(self.grid[y-1][x])
        elif x == len(self.grid[y]) - 1 and y != 0 and y != len(self.grid) - 1:  # Right Edge
            surrounding.append(self.grid[y+1][x])
            surrounding.append(self.grid[y+1][x-1])
            surrounding.append(self.grid[y][x-1])
            surrounding.append(self.grid[y-1][x-1])
            surrounding.append(self.grid[y-1][x])
        elif y == 0 and x != 0 and x != len(self.grid[y]) - 1:  # Top Edge
            surrounding.append(self.grid[y][x-1])
            surrounding.append(self.grid[y][x+1])
            surrounding.append(self.grid[y+1][x-1])
            surrounding.append(self.grid[y+1][x])
            surrounding.append(self.grid[y+1][x+1])
        elif y == len(self.grid) - 1 and x != 0 and x != len(self.grid[y]) - 1:  # Bottom Edge
            surrounding.append(self.grid[y][x-1])
            surrounding.append(self.grid[y][x+1])
            surrounding.append(self.grid[y-1][x-1])
            surrounding.append(self.grid[y-1][x])
            surrounding.append(self.grid[y-1][x+1])
        # Everything else
        else:
            surrounding.append(self.grid[y-1][x-1])
            surrounding.append(self.grid[y-1][x])
            surrounding.append(self.grid[y-1][x+1])

            surrounding.append(self.grid[y][x-1])
            surrounding.append(self.grid[y][x+1])

            surrounding.append(self.grid[y+1][x-1])
            surrounding.append(self.grid[y+1][x])
            surrounding.append(self.grid[y+1][x+1])
        return surrounding

    def calculate_danger(self):
        # For every tile, count the number of mines directly around our tile
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                count = 0
                surrounding = self.get_surrounding(x, y)
                for tile in surrounding:
                    if tile.armed:
                        count += 1
                self.grid[y][x].danger = count

    def uncover_tile(self, x, y, flag):
        tiles_to_uncover = []
        tiles_to_search = []
        current_tile = self.grid[y][x]

        if flag and current_tile.state == 0:
            current_tile.state = 1
            if current_tile.armed:
                self.mines -= 1
            return

        if current_tile.state == 1 and flag:
            if current_tile.armed:
                return
            current_tile.state = 0
            return

        if current_tile.state != 0:
            return

        if current_tile.armed and current_tile.state != 1:
            return -1

        if current_tile.danger > 0:
            current_tile.state = 2
            return

        tiles_to_uncover.append(self.grid[y][x])
        tiles_to_search.extend(self.get_surrounding(x, y))

        while len(tiles_to_search) != 0:
            for tile in tiles_to_search:
                if tile.danger > 0:
                    tiles_to_uncover.append(tile)
                    tiles_to_search.remove(tile)
                elif tile.danger == 0:
                    tiles_to_uncover.append(tile)
                    tiles_to_search.remove(tile)
                    new_tiles = self.get_surrounding(int((tile.x-self.offset_x)/tile.size), int((tile.y-self.offset_y)/tile.size))
                    for new_tile in new_tiles:
                        if new_tile not in tiles_to_uncover:
                            tiles_to_search.append(new_tile)

        for tile in tiles_to_uncover:
            tile.state = 2


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

