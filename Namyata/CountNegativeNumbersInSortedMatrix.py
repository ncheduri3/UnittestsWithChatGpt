import unittest
from typing import List
# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
# return the number of negative numbers in grid
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100





def countNegatives(grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    negatives = 0
    col = 0
    for row in range(ROWS - 1, -1, -1):
        while col < COLS and grid[row][col] >= 0:
            col += 1
        negatives += COLS - col
    return negatives

class TestCountNegatives(unittest.TestCase):

    def test_no_negatives(self):
        grid = [
            [4, 3, 2],
            [3, 2, 1],
            [2, 1, 0]
        ]
        self.assertEqual(countNegatives(grid), 0)

    def test_all_negatives(self):
        grid = [
            [-1, -2, -3],
            [-4, -5, -6],
            [-7, -8, -9]
        ]
        self.assertEqual(countNegatives(grid), 9)

    def test_mixed_negatives(self):
        grid = [
            [4, 3, -2],
            [3, -5, -6],
            [-7, -8, -9]
        ]
        self.assertEqual(countNegatives(grid), 6)

    def test_large_grid(self):
        grid = [
            [-1, -2, -3, -4, -5],
            [-6, -7, -8, -9, -10],
            [-11, -12, -13, -14, -15]
        ]
        self.assertEqual(countNegatives(grid), 15)

if __name__ == '__main__':
    unittest.main()

#All unit tests are correct and passed
