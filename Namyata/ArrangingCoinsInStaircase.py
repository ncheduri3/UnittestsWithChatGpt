import unittest
from math import sqrt
# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
#
# Given the integer n, return the number of complete rows of the staircase you will build.
#
# Constraints:
#
# 1 <= n <= 231 - 1



def arrangeCoins(n: int) -> int:
    return int(sqrt(2 * n + 0.25) - 0.50)

class TestArrangeCoins(unittest.TestCase):
    def test_5_coins(self):
        n = 5
        expected = 2
        self.assertEqual(arrangeCoins(n), expected)

    def test_8_coins(self):
        n = 8
        expected = 3
        self.assertEqual(arrangeCoins(n), expected)

    def test_10_coins(self):
        n = 10
        expected = 4
        self.assertEqual(arrangeCoins(n), expected)

    def test_0_coins(self):
        n = 0
        expected = 0
        self.assertEqual(arrangeCoins(n), expected)

    def test_large_number_of_coins(self):
        n = 1000000
        expected = 1414
        # expected = 1413
        self.assertEqual(arrangeCoins(n), expected)

if __name__ == '__main__':
    unittest.main()

# One test case is wrong. Uncomment to run the correct version.

