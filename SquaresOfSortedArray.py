# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

import unittest
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a = [i * i for i in nums]
        return sorted(a)

class TestSortedSquares(unittest.TestCase):

    def test_sorted_squares(self):
        solution = Solution()
        nums = [-4, -1, 0, 3, 10]
        result = solution.sortedSquares(nums)
        self.assertEqual(result, [0, 1, 9, 16, 100])

    def test_sorted_squares_negative_numbers(self):
        solution = Solution()
        nums = [-7, -3, -2, 0, 5]
        result = solution.sortedSquares(nums)
        self.assertEqual(result, [0, 4, 9, 25, 49])

    def test_sorted_squares_positive_numbers(self):
        solution = Solution()
        nums = [1, 2, 3, 4, 5]
        result = solution.sortedSquares(nums)
        self.assertEqual(result, [1, 4, 9, 16, 25])

    def test_sorted_squares_zero(self):
        solution = Solution()
        nums = [0]
        result = solution.sortedSquares(nums)
        self.assertEqual(result, [0])

    def test_sorted_squares_empty_list(self):
        solution = Solution()
        nums = []
        result = solution.sortedSquares(nums)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()

# All test cases worked!