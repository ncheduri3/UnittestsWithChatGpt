import unittest
from rotate_matrix import rotate_matrix


class TestRotateMatrix(unittest.TestCase):

    def test_rotate_matrix_90_degrees(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        expected_rotated_matrix = [
            [9, 5, 1],
            [10, 6, 2],
            [11, 7, 3],
            [12, 8, 4]
        ]
        self.assertEqual(rotate_matrix(matrix, 1), expected_rotated_matrix)

    def test_rotate_matrix_180_degrees(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        expected_rotated_matrix = [
            [12, 11, 10, 9],
            [8, 7, 6, 5],
            [4, 3, 2, 1]
        ]
        self.assertEqual(rotate_matrix(matrix, 2), expected_rotated_matrix)

    def test_rotate_matrix_270_degrees(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        expected_rotated_matrix = [
            [4, 8, 12],
            [3, 7, 11],
            [2, 6, 10],
            [1, 5, 9]
        ]
        self.assertEqual(rotate_matrix(matrix, 3), expected_rotated_matrix)

    def test_rotate_matrix_360_degrees(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        expected_rotated_matrix = matrix
        self.assertEqual(rotate_matrix(matrix, 4), expected_rotated_matrix)


if __name__ == '__main__':
    unittest.main()
