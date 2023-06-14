import unittest
from find_kth_largest_element import find_kth_largest


class TestFindKthLargest(unittest.TestCase):
    def test_find_kth_largest(self):
        nums = [3, 1, 4, 2, 5]
        k = 2
        expected_output = 4
        self.assertEqual(find_kth_largest(nums, k), expected_output)
        
        nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        k = 5
        expected_output = 5
        self.assertEqual(find_kth_largest(nums, k), expected_output)
        
        nums = [1, 2, 3, 4, 5]
        k = 1
        expected_output = 5
        self.assertEqual(find_kth_largest(nums, k), expected_output)
        
        nums = [-1, -5, -2, -3, -4]
        k = 3
        expected_output = -3
        self.assertEqual(find_kth_largest(nums, k), expected_output)


if __name__ == '__main__':
    unittest.main()
