# We define the usage of capitals in a word to be right when one of the following cases holds:
#
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

import unittest

def detectCapitalUse(word: str) -> bool:
    return True if word.islower() or word.istitle() or word.isupper() else False

class TestDetectCapitalUse(unittest.TestCase):
    def test_all_lower_case(self):
        word = "hello"
        expected = True
        self.assertEqual(detectCapitalUse(word), expected)

    def test_all_upper_case(self):
        word = "HELLO"
        expected = True
        self.assertEqual(detectCapitalUse(word), expected)

    def test_title_case(self):
        word = "Title"
        expected = True
        self.assertEqual(detectCapitalUse(word), expected)

    def test_mixed_case(self):
        word = "MiXeD"
        expected = False
        self.assertEqual(detectCapitalUse(word), expected)

    def test_single_letter(self):
        word = "A"
        expected = True
        self.assertEqual(detectCapitalUse(word), expected)


if __name__ == '__main__':
    unittest.main()

# All test cases by ChatGPT are correct.
