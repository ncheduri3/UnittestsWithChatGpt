import unittest
from typing import List
from bisect import insort_left
# You are given an array of integers stones where stones[i] is the weight of the ith stone.
#
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
#
# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.
#
# Return the weight of the last remaining stone. If there are no stones left, return 0.
#
# Constraints:
#
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000



def lastStoneWeight(stones: List[int]) -> int:
    stones.sort()

    while stones:
        s1 = stones.pop()

        if not stones:
            return s1

        s2 = stones.pop()

        if s1 > s2:
            insort_left(stones, s1 - s2)

    return 0

class TestLastStoneWeight(unittest.TestCase):
    def test_single_stone(self):
        stones = [5]
        expected = 5
        self.assertEqual(lastStoneWeight(stones), expected)

    def test_two_stones(self):
        stones = [3, 7]
        expected = 4
        self.assertEqual(lastStoneWeight(stones), expected)

    def test_multiple_stones(self):
        stones = [2, 7, 4, 1, 8, 1]
        expected = 1
        self.assertEqual(lastStoneWeight(stones), expected)

    def test_same_weight_stones(self):
        stones = [5, 5, 5, 5]
        expected = 0
        self.assertEqual(lastStoneWeight(stones), expected)

    def test_empty_list(self):
        stones = []
        expected = 0
        self.assertEqual(lastStoneWeight(stones), expected)

if __name__ == '__main__':
    unittest.main()
# all the test cases passed.
