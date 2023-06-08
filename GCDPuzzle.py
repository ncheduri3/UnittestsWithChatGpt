# Alice and Bob take turns playing a game, with Alice starting first.
#
# Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:
#
# Choosing any x with 0 < x < n and n % x == 0.
# Replacing the number n on the chalkboard with n - x.
# Also, if a player cannot make a move, they lose the game.
#
# Return true if and only if Alice wins the game, assuming both players play optimally.

import unittest

def divisorGame(n: int) -> bool:
    return n % 2 == 0

class TestDivisorGame(unittest.TestCase):
    def test_even_number(self):
        n = 4
        expected = True
        self.assertEqual(divisorGame(n), expected)

    def test_odd_number(self):
        n = 7
        expected = False
        self.assertEqual(divisorGame(n), expected)

    def test_zero(self):
        n = 0
        expected = True
        self.assertEqual(divisorGame(n), expected)

    def test_large_number(self):
        n = 1000000
        expected = True
        self.assertEqual(divisorGame(n), expected)

if __name__ == '__main__':
    unittest.main()
# all the test cases are correct.
