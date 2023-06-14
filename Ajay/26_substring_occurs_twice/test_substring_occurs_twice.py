import unittest
from substring_occurs_twice import substring_occurs_twice


class TestSubstringOccursTwice(unittest.TestCase):

    def test_substring_occurs_twice(self):
        # Test case with substring occurs exactly twice
        self.assertTrue(substring_occurs_twice("Hello, Hello, how are you?", "Hello"))

    def test_substring_less_than_twice(self):
        # Test case with substring repeated less than twice
        self.assertFalse(substring_occurs_twice("hello, how are you?", "hello"))

    def test_substring_more_than_twice(self):
        # Test case with substring repeated more than twice
        self.assertFalse(substring_occurs_twice("hello, hello, hello, how are you?", "hello"))

    def test_empty_string(self):
        # Test case with empty string
        self.assertFalse(substring_occurs_twice("", "hello"))

    def test_empty_substring(self):
        # Test case with empty substring
        self.assertFalse(substring_occurs_twice("Hello, hello, how are you?", ""))


if __name__ == '__main__':
    unittest.main()
