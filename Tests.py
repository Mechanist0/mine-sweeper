import pygame
import TileGrid
import unittest

class TestNearby(unittest.TestCase):
    def setUp(self):
        pygame.font.init()

    def tearDown(self):
        TileGrid.TileGrid.grid = []

    def test_corners(self):
        corners_grid = [[0, 1], ## 3 2
                        [1, 1]] ## 2 2
        corners_test_grid = TileGrid.TileGrid(1, 1, 10, 0, corners_grid)
        corners_test_grid.build_grid()
        corners_test_grid.peak_danger_grid()

        self.assertEqual(3, corners_test_grid.grid[0][0].danger)
        self.assertEqual(2, corners_test_grid.grid[1][0].danger)
        self.assertEqual(2, corners_test_grid.grid[0][1].danger)
        self.assertEqual(2, corners_test_grid.grid[1][1].danger)

    def test_corners_2(self):
        corners_grid_2 = [[0, 1, 1, 0],
                          [1, 1, 1, 0],
                          [0, 1, 0, 0],
                          [1, 0, 0, 0]]

        corners_test_grid_2 = TileGrid.TileGrid(1, 1, 10, 0, corners_grid_2)
        corners_test_grid_2.build_grid()
        corners_test_grid_2.peak_danger_grid()

        self.assertEqual(3, corners_test_grid_2.grid[0][0].danger)
        self.assertEqual(2, corners_test_grid_2.grid[0][3].danger)
        self.assertEqual(1, corners_test_grid_2.grid[3][0].danger)
        self.assertEqual(0, corners_test_grid_2.grid[3][3].danger)

    def test_edges(self):
        edges_grid = [[0, 1, 1, 0], # - 4 3 -
                [1, 1, 1, 0], # 3 - - 2
                [0, 1, 0, 0], # 4 - - 1
                [1, 0, 0, 0]] # - 2 1 -

        test_edges_grid = TileGrid.TileGrid(1, 1, 10, 0, edges_grid)
        test_edges_grid.build_grid()
        test_edges_grid.peak_danger_grid()

        # Top edge
        self.assertEqual(4, test_edges_grid.grid[0][1].danger)
        self.assertEqual(3, test_edges_grid.grid[0][2].danger)

        # Bottom Edge
        self.assertEqual(2, test_edges_grid.grid[3][1].danger)
        self.assertEqual(1, test_edges_grid.grid[3][2].danger)

        # Left Edge
        self.assertEqual(3, test_edges_grid.grid[1][0].danger)
        self.assertEqual(4, test_edges_grid.grid[2][0].danger)

        # Right Edge
        self.assertEqual(2, test_edges_grid.grid[1][3].danger)
        self.assertEqual(1, test_edges_grid.grid[2][3].danger)

    def test_edges_2(self):
        edges_grid_2 = [[1, 0, 1, 0], # - 4 1 -
                [1, 0, 1, 0], # 2 - - 3
                [1, 0, 1, 0], # 2 - - 3
                [1, 0, 1, 0]] # - 4 1 -

        test_edges_grid_2 = TileGrid.TileGrid(1, 1, 10, 0, edges_grid_2)
        test_edges_grid_2.build_grid()
        test_edges_grid_2.peak_danger_grid()

        # Top edge
        self.assertEqual(4, test_edges_grid_2.grid[0][1].danger)
        self.assertEqual(1, test_edges_grid_2.grid[0][2].danger)

        # Bottom Edge
        self.assertEqual(4, test_edges_grid_2.grid[3][1].danger)
        self.assertEqual(1, test_edges_grid_2.grid[3][2].danger)

        # Left Edge
        self.assertEqual(2, test_edges_grid_2.grid[1][0].danger)
        self.assertEqual(2, test_edges_grid_2.grid[2][0].danger)

        # Right Edge
        self.assertEqual(3, test_edges_grid_2.grid[1][3].danger)
        self.assertEqual(3, test_edges_grid_2.grid[2][3].danger)

    def test_middle(self):
        middle_grid = [[0, 0, 1, 1, 0, 0],
                [0, 0, 1, 1, 0, 0],
                [0, 0, 1, 1, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1]]

        test_middle_grid = TileGrid.TileGrid(1, 1, 10, 0, middle_grid)
        test_middle_grid.build_grid()
        test_middle_grid.peak_danger_grid()

        self.assertEqual(3, test_middle_grid.grid[1][1].danger)
        self.assertEqual(3, test_middle_grid.grid[1][4].danger)
        self.assertEqual(3, test_middle_grid.grid[4][1].danger)
        self.assertEqual(3, test_middle_grid.grid[4][4].danger)

    def test_middle_2(self):
        middle_grid_2 = [[1, 0, 1, 1, 0, 0],
                [1, 0, 1, 1, 0, 0],
                [1, 0, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 1, 1],
                [0, 1, 0, 1, 1, 1]]

        test_middle_grid_2 = TileGrid.TileGrid(1, 1, 10, 0, middle_grid_2)
        test_middle_grid_2.build_grid()
        test_middle_grid_2.peak_danger_grid()

        self.assertEqual(6, test_middle_grid_2.grid[1][1].danger)
        self.assertEqual(5, test_middle_grid_2.grid[1][4].danger)
        self.assertEqual(4, test_middle_grid_2.grid[4][1].danger)
        self.assertEqual(7, test_middle_grid_2.grid[4][4].danger)
