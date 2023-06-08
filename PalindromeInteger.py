# Given an integer x, return true if x is a
# palindrome
# , and false otherwise.

import unittest

def isPalindrome(x):
    if x < 0:
        return False

    inputNum = x
    newNum = 0
    while x > 0:
        newNum = newNum * 10 + x % 10
        x = x // 10
    return newNum == inputNum

class IsPalindromeTestCase(unittest.TestCase):
    def test_palindrome_number(self):
        x = 121
        self.assertTrue(isPalindrome(x))

    def test_non_palindrome_number(self):
        x = 123
        self.assertFalse(isPalindrome(x))

    def test_negative_number(self):
        x = -121
        self.assertFalse(isPalindrome(x))

    def test_single_digit_number(self):
        x = 5
        self.assertTrue(isPalindrome(x))

    def test_zero(self):
        x = 0
        self.assertTrue(isPalindrome(x))

if __name__ == '__main__':
    unittest.main()
