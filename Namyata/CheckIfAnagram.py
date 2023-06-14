import unittest
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#



def isAnagram(s, t):
    if len(s) != len(t):
        return False
    for idx in set(s):
        if s.count(idx) != t.count(idx):
            return False
    return True

class IsAnagramTestCase(unittest.TestCase):
    def test_anagram_strings(self):
        s = "listen"
        t = "silent"
        self.assertTrue(isAnagram(s, t))

    def test_non_anagram_strings(self):
        s = "hello"
        t = "world"
        self.assertFalse(isAnagram(s, t))

    def test_anagram_with_duplicate_characters(self):
        s = "anagram"
        t = "nagaram"
        self.assertTrue(isAnagram(s, t))

    def test_different_length_strings(self):
        s = "cat"
        t = "cats"
        self.assertFalse(isAnagram(s, t))

    def test_empty_strings(self):
        s = ""
        t = ""
        self.assertTrue(isAnagram(s, t))

if __name__ == '__main__':
    unittest.main()

#All unit tests are correct and passed