import unittest
from count_anagram_substring_pairs import count_anagram_substring_pairs


class TestCountAnagramSubstringPairs(unittest.TestCase):

    def test_no_anagram_substring_pairs(self):
        string = "abcd"
        expected_count = 0
        self.assertEqual(count_anagram_substring_pairs(string), expected_count)

    def test_single_anagram_substring_pair(self):
        string = "abba"
        expected_count = 4
        self.assertEqual(count_anagram_substring_pairs(string), expected_count)

    def test_multiple_anagram_substring_pairs(self):
        string = "abab"
        expected_count = 5 
        self.assertEqual(count_anagram_substring_pairs(string), expected_count)

    def test_repeated_characters(self):
        string = "aa"
        expected_count = 1
        self.assertEqual(count_anagram_substring_pairs(string), expected_count)

    def test_empty_string(self):
        string = ""
        expected_count = 0
        self.assertEqual(count_anagram_substring_pairs(string), expected_count)


if __name__ == '__main__':
    unittest.main()
