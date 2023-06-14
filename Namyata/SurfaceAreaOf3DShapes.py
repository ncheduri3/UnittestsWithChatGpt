import unittest
from typing import List
# You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each value v = grid[i][j] represents a tower of v cubes placed on top of cell (i, j).
#
# After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.
#
# Return the total surface area of the resulting shapes.
#
# Note: The bottom face of each shape counts toward its surface area.





def surfaceArea(grid: List[List[int]]) -> int:
    l = len(grid)
    area = 0
    for row in range(l):
        for col in range(l):
            if grid[row][col]:
                area += (grid[row][col] * 4) + 2  # surface area of each block if blocks weren't connected
            if row:  # row > 0
                area -= min(grid[row][col], grid[row - 1][col]) * 2  # subtracting as area is common among two blocks
            if col:  # col > 0
                area -= min(grid[row][col], grid[row][col - 1]) * 2  # subtracting as area is common among two blocks
    return area
class TestSurfaceArea(unittest.TestCase):
    def test_empty_grid(self):
        grid = []
        expected = 0
        self.assertEqual(surfaceArea(grid), expected)

    def test_single_block(self):
        grid = [[1]]
        expected = 6
        self.assertEqual(surfaceArea(grid), expected)

    def test_multiple_blocks(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = 102
        self.assertEqual(surfaceArea(grid), expected)

    def test_zero_blocks(self):
        grid = [[0, 0], [0, 0]]
        expected = 0
        self.assertEqual(surfaceArea(grid), expected)

    def test_large_grid(self):
        grid = [[3, 2, 1, 0, 4], [2, 5, 6, 7, 3], [1, 0, 3, 4, 2], [2, 1, 0, 3, 2], [4, 3, 2, 1, 0]]
        expected = 164
        self.assertEqual(surfaceArea(grid), expected)

class TestSurfaceArea(unittest.TestCase):
    def test_empty_grid(self):
        grid = []
        expected = 0
        self.assertEqual(surfaceArea(grid), expected)

    def test_single_block(self):
        grid = [[1]]
        expected = 6
        self.assertEqual(surfaceArea(grid), expected)

    def test_multiple_blocks(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = 104
        self.assertEqual(surfaceArea(grid), expected)

    def test_zero_blocks(self):
        grid = [[0, 0], [0, 0]]
        expected = 0
        self.assertEqual(surfaceArea(grid), expected)

    def test_large_grid(self):
        grid = [[3, 2, 1, 0, 4], [2, 5, 6, 7, 3], [1, 0, 3, 4, 2], [2, 1, 0, 3, 2], [4, 3, 2, 1, 0]]
        expected = 108
        self.assertEqual(surfaceArea(grid), expected)

if __name__ == '__main__':
    unittest.main()

#A few test cases were wrong.
