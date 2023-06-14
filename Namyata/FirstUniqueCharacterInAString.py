import unittest
from collections import Counter
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of only lowercase English letters.



def firstUniqChar(s: str) -> int:
    count = Counter(s)
    for char, freq in count.items():
        if freq == 1:
            return s.index(char)
    return -1

class TestFirstUniqChar(unittest.TestCase):
    def test_no_uniq_char(self):
        s = "ababcc"
        expected = -1
        self.assertEqual(firstUniqChar(s), expected)

    def test_single_uniq_char(self):
        s = "leetcode"
        expected = 0
        self.assertEqual(firstUniqChar(s), expected)

    def test_multiple_uniq_chars(self):
        s = "loveleetcode"
        expected = 2
        self.assertEqual(firstUniqChar(s), expected)

    def test_all_uniq_chars(self):
        s = "abcd"
        expected = 0
        self.assertEqual(firstUniqChar(s), expected)

if __name__ == '__main__':
    unittest.main()

#All unit tests are correct and passed