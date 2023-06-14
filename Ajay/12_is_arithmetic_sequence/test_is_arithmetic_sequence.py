import unittest
from is_arithmetic_sequence import is_arithmetic_sequence


class TestIsArithmeticSequence(unittest.TestCase):
    def test_arithmetic_sequence(self):
        # Test cases with arithmetic sequences
        self.assertTrue(is_arithmetic_sequence([1, 3, 5, 7, 9]))
        self.assertTrue(is_arithmetic_sequence([0, 2, 4, 6, 8]))
        self.assertTrue(is_arithmetic_sequence([-1, -3, -5, -7, -9]))
        self.assertTrue(is_arithmetic_sequence([5, 5, 5, 5, 5, 5]))
    
    def test_arithmetic_by_length(self):
        self.assertTrue(is_arithmetic_sequence([10]))
        self.assertTrue(is_arithmetic_sequence([1, 5]))
        self.assertTrue(is_arithmetic_sequence([]))

    def test_non_arithmetic_sequence(self):
        # Test cases with non-arithmetic sequences
        self.assertFalse(is_arithmetic_sequence([1, 3, 6, 10, 15]))
        self.assertFalse(is_arithmetic_sequence([2, 4, 6, 9, 11]))
        self.assertFalse(is_arithmetic_sequence([1, 2, 3, 5, 8]))


if __name__ == '__main__':
    unittest.main()
