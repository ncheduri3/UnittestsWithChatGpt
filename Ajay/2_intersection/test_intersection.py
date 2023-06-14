import unittest
from intersection import intersection


class TestIntersection(unittest.TestCase):
    def test_empty_arrays(self):
        self.assertEqual(intersection([], []), [])

    def test_no_common_elements(self):
        self.assertEqual(intersection([1, 2, 3], [4, 5, 6]), [])
        self.assertEqual(intersection([1, 2, 3], [4, 5, 6, 7]), [])

    def test_common_elements(self):
        self.assertEqual(intersection([1, 2, 2, 1], [2, 2]), [2, 2])
        self.assertEqual(intersection([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9])
        self.assertEqual(intersection([1, 2, 2, 1, 1, 3], [2, 1, 1, 4]), [1, 1, 2])

    def test_duplicate_elements(self):
        self.assertEqual(intersection([1, 2, 2, 1], [2, 2, 2]), [2, 2])
        self.assertEqual(intersection([1, 2, 2, 1], [2, 2, 1, 1, 1]), [1, 1, 2, 2])
        self.assertEqual(intersection([1, 2, 2, 1], [1, 1]), [1, 1])

    def test_result_order(self):
        self.assertEqual(intersection([4, 2, 9, 1, 5], [9, 4, 1, 2, 8, 4]), [1, 2, 4, 9])


if __name__ == '__main__':
    unittest.main()
