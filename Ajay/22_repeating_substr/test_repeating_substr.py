import unittest
from repeating_substr import find_first_repeating_subsequence


class TestFindFirstRepeatingSubsequence(unittest.TestCase):

    def test_find_repeating_subsequence(self):
        # Test case with a repeating subsequence
        string = "ababcabade"
        expected_subsequence = "aba"
        self.assertEqual(find_first_repeating_subsequence(string), expected_subsequence)

    def test_find_no_repeating_subsequence(self):
        # Test case with no repeating subsequence
        string = "abcdefgh"
        expected_subsequence = ""
        self.assertEqual(find_first_repeating_subsequence(string), expected_subsequence)

    def test_find_repeating_subsequence_size_3(self):
        # Test case with a repeating subsequence of size 3
        string = "abcdefgijklabc"
        expected_subsequence = "abc"
        self.assertEqual(find_first_repeating_subsequence(string), expected_subsequence)

    def test_find_repeating_subsequence_size_3_simple(self):
        # Test case with a repeating subsequence of size 3 simple
        string = "bacbac"
        expected_subsequence = "bac"
        self.assertEqual(find_first_repeating_subsequence(string), expected_subsequence)


if __name__ == '__main__':
    unittest.main()
