# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
#
# Letters are case sensitive, so "a" is considered a different type of stone from "A".
#
# Constraints:
#
# 1 <= jewels.length, stones.length <= 50
# jewels and stones consist of only English letters.
# All the characters of jewels are unique.

import unittest


def numJewelsInStones(jewels: str, stones: str) -> int:
    counter = 0
    for i in stones:
        if i in jewels:
            counter += 1
    return counter


class TestNumJewelsInStones(unittest.TestCase):

    def test_all_jewels_in_stones(self):
        jewels = "abc"
        stones = "aabbbccc"
        result = numJewelsInStones(jewels, stones)
        self.assertEqual(result, 9) # Comment this and Uncomment the next line
        # self.assertEqual(result, 10)

    def test_no_jewels_in_stones(self):
        jewels = "abc"
        stones = "def"
        result = numJewelsInStones(jewels, stones)
        self.assertEqual(result, 0)

    def test_some_jewels_in_stones(self):
        jewels = "abc"
        stones = "aadefbcc"
        result = numJewelsInStones(jewels, stones)
        self.assertEqual(result, 6) # Comment this and Uncomment the next line
        self.assertEqual(result, 5)

    def test_empty_stones(self):
        jewels = "abc"
        stones = ""
        result = numJewelsInStones(jewels, stones)
        self.assertEqual(result, 0)

    def test_empty_jewels(self):
        jewels = ""
        stones = "abcdef"
        result = numJewelsInStones(jewels, stones)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
