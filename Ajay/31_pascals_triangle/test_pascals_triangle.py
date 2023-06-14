import unittest
from pascals_triangle import pascal_triangle


class TestPascalTriangle(unittest.TestCase):

    def test_pascal_triangle(self):
        # Test case with n = 5
        n = 5
        expected_output = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
        self.assertEqual(pascal_triangle(n), expected_output)

    def test_n_equals_0(self):
        # Test case with n = 0
        n = 0
        expected_output = []
        self.assertEqual(pascal_triangle(n), expected_output)

    def test_n_equals_1(self):
        # Test case with n = 1
        n = 1
        expected_output = [[1]]
        self.assertEqual(pascal_triangle(n), expected_output)

    def test_n_equals_2(self):
        # Test case with n = 2
        n = 2
        expected_output = [[1], [1, 1]]
        self.assertEqual(pascal_triangle(n), expected_output)


if __name__ == '__main__':
    unittest.main()
