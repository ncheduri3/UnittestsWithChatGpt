import unittest
from reverse_string_recursive import reverse_string_recursive


class TestReverseStringRecursive(unittest.TestCase):

    def test_reverse_string(self):
        string = "Hello, World!"
        expected_result = "!dlroW ,olleH"
        self.assertEqual(reverse_string_recursive(string), expected_result)

    def test_empty_string(self):
        string = ""
        expected_result = ""
        self.assertEqual(reverse_string_recursive(string), expected_result)

    def test_single_character_string(self):
        string = "A"
        expected_result = "A"
        self.assertEqual(reverse_string_recursive(string), expected_result)


if __name__ == '__main__':
    unittest.main()
    