import unittest
from check_substr import is_substring


class TestSubstring(unittest.TestCase):

    def test_substring_exists(self):
        string = "Hello, world!"
        self.assertTrue(is_substring("world", string))
        self.assertTrue(is_substring("Hello", string))
        self.assertTrue(is_substring("lo, w", string))
        self.assertTrue(is_substring("!", string))

    def test_substring_does_not_exist(self):
        string = "Hello, world!"
        self.assertFalse(is_substring("World", string))
        self.assertFalse(is_substring("hello", string))
        self.assertFalse(is_substring("lo, w!", string))
        self.assertFalse(is_substring("foo", string))

    def test_empty_substring(self):
        string = "Hello, world!"
        self.assertTrue(is_substring("", string))

    def test_empty_string(self):
        substring = "Hello"
        self.assertFalse(is_substring(substring, ""))


if __name__ == '__main__':
    unittest.main()
