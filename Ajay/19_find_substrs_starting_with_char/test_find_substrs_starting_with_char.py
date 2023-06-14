import unittest
from find_substrs_starting_with_char import find_substrings_with_char


class TestFindSubstringsWithChar(unittest.TestCase):

    def test_find_substrings_with_char(self):
        string = "hello"
        char = "l"
        expected_substrings = ['l', 'll', 'llo', 'lo']
        self.assertEqual(find_substrings_with_char(string, char), expected_substrings)

    def test_find_substrings_with_char_empty_string(self):
        string = ""
        char = "a"
        expected_substrings = []
        self.assertEqual(find_substrings_with_char(string, char), expected_substrings)

    def test_find_substrings_with_char_no_match(self):
        string = "hello"
        char = "x"
        expected_substrings = []
        self.assertEqual(find_substrings_with_char(string, char), expected_substrings)

    def test_find_substrings_with_char_duplicate_chars(self):
        string = "aba"
        char = "a"
        expected_substrings = ['a', 'ab', 'aba']
        self.assertEqual(find_substrings_with_char(string, char), expected_substrings)


if __name__ == '__main__':
    unittest.main()
