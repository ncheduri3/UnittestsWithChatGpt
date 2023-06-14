import unittest
from indices_of_occurrences import indices_of_occurrences


class TestGetIndices(unittest.TestCase):

    def test_indices_exist(self):
        string = "Hello, World!"
        char = "o"
        expected_result = [4, 8]
        self.assertEqual(indices_of_occurrences(string, char), expected_result)

    def test_no_indices_exist(self):
        string = "Hello, World!"
        char = "x"
        expected_result = []
        self.assertEqual(indices_of_occurrences(string, char), expected_result)

    def test_empty_string(self):
        string = ""
        char = "a"
        expected_result = []
        self.assertEqual(indices_of_occurrences(string, char), expected_result)

    def test_case_sensitive(self):
        string = "HelLo, WorLd!"
        char = "L"
        expected_result = [3, 10]
        self.assertEqual(indices_of_occurrences(string, char), expected_result)


if __name__ == '__main__':
    unittest.main()
