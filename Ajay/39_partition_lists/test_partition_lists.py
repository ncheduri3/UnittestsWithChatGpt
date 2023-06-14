import unittest
from partition_lists import partition_lists


class TestPartitionLists(unittest.TestCase):
    def test_middle_number(self):
        nums = [4, 2, 5, 1, 3, 6, 2]
        x = 3
        expected_result = ([2, 1, 2], [3], [4, 5, 6])
        result = partition_lists(nums, x)
        self.assertEqual(result, expected_result)

    def test_all_equal(self):
        nums = [10, 10, 10, 10]
        x = 10
        expected_result = ([], [10, 10, 10, 10], [])
        result = partition_lists(nums, x)
        self.assertEqual(result, expected_result)

    def test_all_less(self):
        nums = [2, 1, 5, 4, 3]
        x = 6
        expected_result = ([2, 1, 5, 4, 3], [], [])
        result = partition_lists(nums, x)
        self.assertEqual(result, expected_result)
    
    def test_all_greater(self):
        nums = [1, 2, 3, 4, 5]
        x = 0
        expected_result = ([], [], [1, 2, 3, 4, 5])
        result = partition_lists(nums, x)
        self.assertEqual(result, expected_result)

    def test_empty_list(self):
        nums = []
        x = 3
        expected_result = ([], [], [])
        result = partition_lists(nums, x)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
