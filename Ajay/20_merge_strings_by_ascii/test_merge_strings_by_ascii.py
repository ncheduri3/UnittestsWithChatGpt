import unittest
from merge_strings_by_ascii import merge_strings_by_ascii


class TestMergeStringsByAscii(unittest.TestCase):

    def test_merge_strings_by_ascii(self):
        str1 = "ace"
        str2 = "bdf"
        expected_merged_string = "abcdef"
        self.assertEqual(merge_strings_by_ascii(str1, str2), expected_merged_string)

    def test_merge_strings_by_ascii_empty_strings(self):
        str1 = ""
        str2 = ""
        expected_merged_string = ""
        self.assertEqual(merge_strings_by_ascii(str1, str2), expected_merged_string)

    def test_merge_strings_by_ascii_one_empty_string(self):
        str1 = "abc"
        str2 = ""
        expected_merged_string = "abc"
        self.assertEqual(merge_strings_by_ascii(str1, str2), expected_merged_string)

    def test_merge_strings_by_ascii_same_characters(self):
        str1 = "abc"
        str2 = "aabbcc"
        expected_merged_string = "aaabbbccc"
        self.assertEqual(merge_strings_by_ascii(str1, str2), expected_merged_string)


if __name__ == '__main__':
    unittest.main()
