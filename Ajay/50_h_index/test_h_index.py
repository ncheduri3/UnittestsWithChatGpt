import unittest
from h_index import h_index


class TestHIndex(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(h_index([]), 0)

    def test_single_element_array(self):
        self.assertEqual(h_index([5]), 1)
        self.assertEqual(h_index([0]), 0)

    def test_array_with_repeated_citations(self):
        self.assertEqual(h_index([3, 3, 3, 3, 3]), 3)
        self.assertEqual(h_index([0, 0, 0, 0, 0]), 0)

    def test_array_with_all_citations_greater_than_array_size(self):
        self.assertEqual(h_index([10, 12, 15, 8, 7]), 5)

    def test_array_with_all_citations_smaller_than_array_size(self):
        self.assertEqual(h_index([1, 2, 0, 3, 4]), 2)

    def test_array_with_mix_of_citations(self):
        self.assertEqual(h_index([10, 8, 5, 4, 3]), 4)
        self.assertEqual(h_index([6, 5, 3, 1, 0]), 3)
        self.assertEqual(h_index([25, 8, 5, 3, 3]), 3)
        self.assertEqual(h_index([0, 1, 2, 3, 4]), 2)
        self.assertEqual(h_index([3, 0, 6, 1, 5]), 3)


if __name__ == '__main__':
    unittest.main()
