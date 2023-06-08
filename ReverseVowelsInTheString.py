

import unittest

def reverseVowels(s: str) -> str:
    q = []
    vowels = ['a', 'i', 'e', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for char in s:
        if char in vowels:
            q.append(char)
            s = s.replace(char, '*', 1)
    q.reverse()
    k = 0
    for char in s:
        if char == '*':
            s = s.replace("*", q[k], 1)
            k += 1
    return s

class TestReverseVowels(unittest.TestCase):
    def test_no_vowels(self):
        s = "xyz"
        expected = "xyz"
        self.assertEqual(reverseVowels(s), expected)

    def test_single_vowel(self):
        s = "hello"
        expected = "holle"
        self.assertEqual(reverseVowels(s), expected)

    def test_multiple_vowels(self):
        s = "leetcode"
        expected = "leotcede"
        self.assertEqual(reverseVowels(s), expected)

    def test_same_vowel(self):
        s = "aaeeii"
        expected = "iiEEaa"
        expected = "iieeaa"
        self.assertEqual(reverseVowels(s), expected)

if __name__ == '__main__':
    unittest.main()

# 1 test case by chatgpt are not correct. Uncomment the line to run the correct version
