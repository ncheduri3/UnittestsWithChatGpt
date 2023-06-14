import unittest
from find_div_by_a_or_b import find_div_by_a_or_b


class TestDivisibleByAOrB(unittest.TestCase):

    def test_divisible_by_a_or_b(self):
        numbers = [15, 24, 25, 30, 35, 40, 45, 50]
        a = 4
        b = 10
        expected = [24, 30, 50]
        self.assertEqual(find_div_by_a_or_b(numbers, a, b), expected)

    def test_no_numbers_divisible(self):
        numbers = [11, 17, 23, 29, 31, 37]
        a = 3
        b = 5
        expected = []
        self.assertEqual(find_div_by_a_or_b(numbers, a, b), expected)

    def test_all_numbers_divisible(self):
        numbers = [10, 20, 30, 40, 50]
        a = 10
        b = 5
        expected = []
        self.assertEqual(find_div_by_a_or_b(numbers, a, b), expected)

    def test_empty_list(self):
        numbers = []
        a = 5
        b = 10
        expected = []
        self.assertEqual(find_div_by_a_or_b(numbers, a, b), expected)


if __name__ == '__main__':
    unittest.main()
