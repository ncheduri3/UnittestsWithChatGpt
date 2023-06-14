import unittest
from longest_repeating_substring import longest_repeating_substring


class TestLongestRepeatingSubstring(unittest.TestCase):
    def test_non_empty_string_with_repeating_substring(self):
        s = "banana"
        expected_result = "ana"
        self.assertEqual(longest_repeating_substring(s), expected_result)

    def test_non_empty_string_with_no_repeating_substring(self):
        s = "abcdefg"
        expected_result = ""
        self.assertEqual(longest_repeating_substring(s), expected_result)

    def test_empty_string(self):
        s = ""
        expected_result = ""
        self.assertEqual(longest_repeating_substring(s), expected_result)

    def test_non_empty_string_with_multiple_repeating_substrings(self):
        s = "aabbaabbcc"
        expected_result = "aabb"
        self.assertEqual(longest_repeating_substring(s), expected_result)

    def test_non_empty_string_with_repeating_substring_at_end(self):
        s = "xyzxyzxyz"
        expected_result = "xyzxyz"
        self.assertEqual(longest_repeating_substring(s), expected_result)


if __name__ == '__main__':
    unittest.main()
