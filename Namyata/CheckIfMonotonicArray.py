import unittest
from typing import List
# An array is monotonic if it is either monotone increasing or monotone decreasing.
#
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
#
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.



def isMonotonic(nums: List[int]) -> bool:
    return nums == sorted(nums) or nums == sorted(nums, reverse=True)

class TestIsMonotonic(unittest.TestCase):

    def test_increasing_list(self):
        nums = [1, 2, 3, 4, 5]
        expected = True
        self.assertEqual(isMonotonic(nums), expected)

    def test_decreasing_list(self):
        nums = [5, 4, 3, 2, 1]
        expected = True
        self.assertEqual(isMonotonic(nums), expected)

    def test_monotonic_list(self):
        nums = [1, 3, 5, 7, 9]
        expected = True
        self.assertEqual(isMonotonic(nums), expected)

    def test_non_monotonic_list(self):
        nums = [1, 3, 2, 5, 4]
        expected = False
        self.assertEqual(isMonotonic(nums), expected)

    def test_equal_elements_list(self):
        nums = [5, 5, 5, 5, 5]
        expected = True
        self.assertEqual(isMonotonic(nums), expected)

if __name__ == '__main__':
    unittest.main()

#All unit tests are correct and passed
