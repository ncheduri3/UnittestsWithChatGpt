import unittest
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.



def twoSum(nums, target):
    d = {}
    for i, j in enumerate(nums):
        r = target - j
        if r in d:
            return [d[r], i]
        d[j] = i

class TwoSumTestCase(unittest.TestCase):
    def test_target_present(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected_output = [0, 1]
        self.assertEqual(twoSum(nums, target), expected_output)

    def test_target_not_present(self):
        nums = [3, 6, 8, 12]
        target = 5
        expected_output = None
        self.assertEqual(twoSum(nums, target), expected_output)

    def test_duplicate_values(self):
        nums = [2, 7, 11, 15, 7]
        target = 14
        expected_output = [1, 4]
        self.assertEqual(twoSum(nums, target), expected_output)

    def test_negative_numbers(self):
        nums = [-2, -7, 11, 15]
        target = 9
        expected_output = [0, 2]
        self.assertEqual(twoSum(nums, target), expected_output)

    def test_empty_array(self):
        nums = []
        target = 9
        expected_output = None
        self.assertEqual(twoSum(nums, target), expected_output)

    def test_single_element_array(self):
        nums = [5]
        target = 5
        expected_output = None
        self.assertEqual(twoSum(nums, target), expected_output)

if __name__ == '__main__':
    unittest.main()


#All unit tests are correct and passed

