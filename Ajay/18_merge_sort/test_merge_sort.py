import unittest
from merge_sort import merge_sort


class MergeSortTest(unittest.TestCase):
    def test_merge_sort_random_list(self):
        # Test case with a random list of integers
        arr = [4, 2, 7, 1, 5, 3, 6]
        sorted_arr = merge_sort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5, 6, 7])

    def test_merge_sort_already_sorted_list(self):
        # Test case with an already sorted list
        arr = [1, 2, 3, 4, 5]
        sorted_arr = merge_sort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_merge_sort_empty_list(self):
        # Test case with an empty list
        arr = []
        sorted_arr = merge_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_merge_sort_single_element_list(self):
        # Test case with a single-element list
        arr = [5]
        sorted_arr = merge_sort(arr)
        self.assertEqual(sorted_arr, [5])

    def test_merge_sort_list_with_duplicates(self):
        # Test case with a list containing duplicate elements
        arr = [2, 4, 3, 2, 1, 4, 5, 1]
        sorted_arr = merge_sort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 2, 3, 4, 4, 5])


if __name__ == '__main__':
    unittest.main()
