import unittest
from count_occurrences import count_character_occurrences


class TestCountCharacterOccurrences(unittest.TestCase):

    def test_count_character_occurrences(self):
        string = "hello"
        expected = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        self.assertEqual(count_character_occurrences(string), expected)

    def test_count_character_occurrences_empty_string(self):
        string = ""
        expected = {}
        self.assertEqual(count_character_occurrences(string), expected)

    def test_count_character_occurrences_repeated_characters(self):
        string = "banana"
        expected = {'b': 1, 'a': 3, 'n': 2}
        self.assertEqual(count_character_occurrences(string), expected)

    def test_count_character_occurrences_case_sensitive(self):
        string = "Hello"
        expected = {'H': 1, 'e': 1, 'l': 2, 'o': 1}
        self.assertEqual(count_character_occurrences(string), expected)


if __name__ == '__main__':
    unittest.main()
