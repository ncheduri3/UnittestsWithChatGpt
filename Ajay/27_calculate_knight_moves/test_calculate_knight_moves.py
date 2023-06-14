import unittest
from calculate_knight_moves import calculate_knight_moves


class TestCalculateKnightMoves(unittest.TestCase):

    def test_knight_moves_3x3(self):
        # Test case with a 3x3 chess board and knight at position (1, 1)
        self.assertEqual(calculate_knight_moves(3, 3, 1, 1), 0)

    def test_knight_moves_5x5(self):
        # Test case with a 5x5 chess board and knight at position (2, 2)
        self.assertEqual(calculate_knight_moves(5, 5, 2, 2), 8)

    def test_knight_moves_8x8_starting_at_0_0(self):
        # Test case with a 8x8 chess board and knight at position (0, 0)
        self.assertEqual(calculate_knight_moves(8, 8, 0, 0), 2)

    def test_knight_moves_8x8_starting_at_7_7(self):
        # Test case with a 8x8 chess board and knight at position (7, 7)
        self.assertEqual(calculate_knight_moves(8, 8, 7, 7), 2)


if __name__ == '__main__':
    unittest.main()
