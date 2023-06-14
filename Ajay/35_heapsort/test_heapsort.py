import unittest
from heapsort import heapsort


class TestHeapsort(unittest.TestCase):
    def test_heapsort_positive_integers(self):
        arr = [9, 5, 7, 1, 3]
        expected_output = [1, 3, 5, 7, 9]
        self.assertEqual(heapsort(arr), expected_output)

    def test_heapsort_negative_integers(self):
        arr = [-4, -9, -2, -7, -1]
        expected_output = [-9, -7, -4, -2, -1]
        self.assertEqual(heapsort(arr), expected_output)

    def test_heapsort_mixed_integers(self):
        arr = [-3, 2, -5, 1, 0]
        expected_output = [-5, -3, 0, 1, 2]
        self.assertEqual(heapsort(arr), expected_output)

    def test_heapsort_duplicate_elements(self):
        arr = [4, 1, 4, 2, 3]
        expected_output = [1, 2, 3, 4, 4]
        self.assertEqual(heapsort(arr), expected_output)

    def test_heapsort_already_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(heapsort(arr), expected_output)

    def test_heapsort_empty_array(self):
        arr = []
        expected_output = []
        self.assertEqual(heapsort(arr), expected_output)

    def test_heapsort_single_element_array(self):
        arr = [42]
        expected_output = [42]
        self.assertEqual(heapsort(arr), expected_output)


if __name__ == '__main__':
    unittest.main()
