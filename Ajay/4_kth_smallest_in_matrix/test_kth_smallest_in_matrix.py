import unittest
from kth_smallest_in_matrix import kth_smallest_in_matrix


class TestKthSmallestInMatrix(unittest.TestCase):
    def test_kth_smallest_square_matrix(self):
        matrix = [
            [1, 3, 5],
            [2, 4, 6],
            [7, 8, 9]
        ]
        k = 5
        self.assertEqual(kth_smallest_in_matrix(matrix, k), 5)

    def test_k_bigger_than_matrix_size(self):
        matrix = [
            [1, 3, 5],
            [2, 4, 6],
            [7, 8, 9]
        ]
        k = 10
        self.assertIsNone(kth_smallest_in_matrix(matrix, k))

    def test_kth_smallest_rectangular_matrix(self):
        matrix = [
            [8, 8, 2],
            [3, 2, 9],
            [88, 12, 3],
            [15, 2, 5]
        ]
        k = 9
        self.assertEqual(kth_smallest_in_matrix(matrix, k), 9)

    def test_kth_smallest_single_row_matrix(self):
        matrix = [[1, 2, 3]]
        k = 2
        self.assertEqual(kth_smallest_in_matrix(matrix, k), 2)

    def test_kth_smallest_single_column_matrix(self):
        matrix = [
            [1],
            [2],
            [3]
        ]
        k = 3
        self.assertEqual(kth_smallest_in_matrix(matrix, k), 3)

    def test_kth_smallest_empty_matrix(self):
        matrix = []
        k = 1
        self.assertIsNone(kth_smallest_in_matrix(matrix, k))

    def test_kth_smallest_single_element_matrix(self):
        matrix = [[5]]
        k = 1
        self.assertEqual(kth_smallest_in_matrix(matrix, k), 5)


if __name__ == '__main__':
    unittest.main()
