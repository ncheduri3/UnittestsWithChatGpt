import unittest
from nth_digit_in_sequence import nth_digit_in_sequence


class TestNthDigitInSequence(unittest.TestCase):
    def test_with_n_equal_zero(self):
        self.assertEqual(nth_digit_in_sequence(0), None)
        
    def test_nth_digit_in_sequence(self):
        self.assertEqual(nth_digit_in_sequence(1), 1)
        self.assertEqual(nth_digit_in_sequence(2), 2)
        self.assertEqual(nth_digit_in_sequence(10), 1)
        self.assertEqual(nth_digit_in_sequence(11), 0)
        self.assertEqual(nth_digit_in_sequence(12), 1)
        self.assertEqual(nth_digit_in_sequence(15), 2)
        self.assertEqual(nth_digit_in_sequence(20), 1)
        self.assertEqual(nth_digit_in_sequence(21), 5)
        self.assertEqual(nth_digit_in_sequence(30), 2)
        self.assertEqual(nth_digit_in_sequence(100), 5)
        self.assertEqual(nth_digit_in_sequence(500), 0)
        self.assertEqual(nth_digit_in_sequence(1000), 3)


if __name__ == '__main__':
    unittest.main()
