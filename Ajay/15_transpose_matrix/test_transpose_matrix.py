import unittest
from transpose_matrix import transpose_matrix


class TestTransposeMatrix(unittest.TestCase):

    def test_transpose_matrix(self):
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        expected = [[1, 4, 7],
                    [2, 5, 8],
                    [3, 6, 9]]
        self.assertEqual(transpose_matrix(matrix), expected)

    def test_transpose_empty_matrix(self):
        matrix = []
        expected = []
        self.assertEqual(transpose_matrix(matrix), expected)

    def test_transpose_single_row_matrix(self):
        matrix = [[1, 2, 3]]
        expected = [[1], [2], [3]]
        self.assertEqual(transpose_matrix(matrix), expected)

    def test_transpose_single_column_matrix(self):
        matrix = [[1], [2], [3]]
        expected = [[1, 2, 3]]
        self.assertEqual(transpose_matrix(matrix), expected)

    def test_transpose_rectangular_matrix(self):
        matrix = [[1, 2, 3],
                  [4, 5, 6]]
        expected = [[1, 4],
                    [2, 5],
                    [3, 6]]
        self.assertEqual(transpose_matrix(matrix), expected)


if __name__ == '__main__':
    unittest.main()
