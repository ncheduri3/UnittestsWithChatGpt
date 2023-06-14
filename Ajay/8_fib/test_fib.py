import unittest
from fib import fib


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_sequence(self):
        n = 10
        expected_result = [1, 1, 2, 3, 5, 8]
        self.assertEqual(fib(n), expected_result)

    def test_empty_sequence(self):
        n = 1
        expected_result = []
        self.assertEqual(fib(n), expected_result)

    def test_single_value_sequence(self):
        n = 2
        expected_result = [1, 1]
        self.assertEqual(fib(n), expected_result)


if __name__ == '__main__':
    unittest.main()
