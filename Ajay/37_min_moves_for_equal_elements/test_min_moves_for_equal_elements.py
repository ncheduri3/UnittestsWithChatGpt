import unittest
from min_moves_for_equal_elements import min_moves_for_equal_elements


class TestMinMovesToMakeElementsEqual(unittest.TestCase):

    def test_min_moves_for_equal_elements_with_increment(self):
        nums = [1, 2, 3, 4, 5]
        expected_moves = 6
        self.assertEqual(min_moves_for_equal_elements(nums), expected_moves)

    def test_min_moves_for_equal_elements_with_decrement(self):
        nums = [5, 4, 3, 2, 1]
        expected_moves = 6
        self.assertEqual(min_moves_for_equal_elements(nums), expected_moves)

    def test_min_moves_for_equal_elements_with_positive_and_negative(self):
        nums = [-3, -1, 0, 2, 4]
        expected_moves = 10
        self.assertEqual(min_moves_for_equal_elements(nums), expected_moves)

    def test_min_moves_for_equal_elements_with_single_element(self):
        nums = [7]
        expected_moves = 0
        self.assertEqual(min_moves_for_equal_elements(nums), expected_moves)

    def test_min_moves_for_equal_elements_with_empty_list(self):
        nums = []
        expected_moves = 0
        self.assertEqual(min_moves_for_equal_elements(nums), expected_moves)


if __name__ == '__main__':
    unittest.main()
