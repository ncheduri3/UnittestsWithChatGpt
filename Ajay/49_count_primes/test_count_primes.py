import unittest
from count_primes import count_primes


class TestCountPrimes(unittest.TestCase):
    def test_count_primes(self):
        self.assertEqual(count_primes(10), 4)
        self.assertEqual(count_primes(20), 8)
        self.assertEqual(count_primes(30), 10)
        self.assertEqual(count_primes(50), 15)
        self.assertEqual(count_primes(100), 25)


if __name__ == '__main__':
    unittest.main()
