import unittest
from calculate_sum_exceeding_index import calculate_sum_exceed_index


class TestCalculateSumExceedIndex(unittest.TestCase):

    def test_sum_exceed_index_case_1(self):
        # Test case with arr = [1, 3, 5, 7, 9] and x = 12
        self.assertEqual(calculate_sum_exceed_index([1, 3, 5, 7, 9], 12), 3)

    def test_sum_exceed_index_case_2(self):
        # Test case with arr = [2, 4, 6, 8, 10] and x = 20
        self.assertEqual(calculate_sum_exceed_index([2, 4, 6, 8, 10], 20), 4)

    def test_sum_exceed_index_case_3(self):
        # Test case with arr = [1, 2, 3, 4, 5] and x = 10
        self.assertEqual(calculate_sum_exceed_index([1, 2, 3, 4, 5], 10), 4)

    def test_sum_exceed_index_case_4(self):
        # Test case with arr = [1, 2, 3, 4, 5] and x = 100
        self.assertEqual(calculate_sum_exceed_index([1, 2, 3, 4, 5], 100), 5)

    def test_sum_exceed_index_case_5(self):
        # Test case with arr = [] and x = 5 (empty list)
        self.assertEqual(calculate_sum_exceed_index([], 5), 0)


if __name__ == '__main__':
    unittest.main()
