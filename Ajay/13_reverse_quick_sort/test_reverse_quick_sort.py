import unittest
from reverse_quick_sort import reverse_quick_sort


class TestReverseQuickSort(unittest.TestCase):

    def test_reverse_quick_sort(self):
        arr = [9, 3, 2, 7, 6, 8, 1, 5, 4]
        expected = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(reverse_quick_sort(arr), expected)

    def test_reverse_quick_sort_empty(self):
        arr = []
        expected = []
        self.assertEqual(reverse_quick_sort(arr), expected)

    def test_reverse_quick_sort_single_element(self):
        arr = [5]
        expected = [5]
        self.assertEqual(reverse_quick_sort(arr), expected)

    def test_reverse_quick_sort_already_sorted(self):
        arr = [10, 8, 6, 4, 2]
        expected = [10, 8, 6, 4, 2]
        self.assertEqual(reverse_quick_sort(arr), expected)

    def test_reverse_quick_sort_duplicate_elements(self):
        arr = [5, 2, 7, 2, 1, 5]
        expected = [7, 5, 5, 2, 2, 1]
        self.assertEqual(reverse_quick_sort(arr), expected)


if __name__ == '__main__':
    unittest.main()
