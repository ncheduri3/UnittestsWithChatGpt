# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
#
# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
#
# A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

import unittest

def findLHS(nums) -> int:
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    max_length = 0
    for num in freq:
        if num + 1 in freq:
            max_length = max(max_length, freq[num] + freq[num + 1])
    return max_length

class TestFindLHS(unittest.TestCase):
    def test_example_case(self):
        nums = [1, 3, 2, 2, 5, 2, 3, 7]
        expected = 5
        self.assertEqual(findLHS(nums), expected)

    def test_empty_list(self):
        nums = []
        expected = 0
        self.assertEqual(findLHS(nums), expected)

    def test_single_element(self):
        nums = [5]
        expected = 0
        self.assertEqual(findLHS(nums), expected)

    def test_no_consecutive_elements(self):
        nums = [1, 2, 3, 4, 5]
        expected = 0
        # expected = 2
        self.assertEqual(findLHS(nums), expected)

    def test_negative_numbers(self):
        nums = [-1, -2, -2, -2, -3, -4, -5]
        expected = 3
        # expected = 4
        self.assertEqual(findLHS(nums), expected)

    def test_large_input(self):
        nums = [10**9] * 10**4 + [0] * 10**4
        expected = 10**4
        # expected = 0
        self.assertEqual(findLHS(nums), expected)

if __name__ == '__main__':
    unittest.main()

# 3 test cases by chatGPT had to be corrected. Uncomment the lines to run the correct version.
