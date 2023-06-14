import unittest
from freq_dict import generate_frequency_dictionary


class TestGenerateFrequencyDictionary(unittest.TestCase):
    def test_empty_string(self):
        string = ""
        expected = {}
        self.assertEqual(generate_frequency_dictionary(string), expected)

    def test_single_character_string(self):
        string = "a"
        expected = {"a": 1}
        self.assertEqual(generate_frequency_dictionary(string), expected)

    def test_repeated_characters(self):
        string = "abracadabra"
        expected = {"a": 5, "b": 2, "r": 2, "c": 1, "d": 1}
        self.assertEqual(generate_frequency_dictionary(string), expected)

    def test_unique_characters(self):
        string = "xyz123"
        expected = {"x": 1, "y": 1, "z": 1, "1": 1, "2": 1, "3": 1}
        self.assertEqual(generate_frequency_dictionary(string), expected)


if __name__ == '__main__':
    unittest.main()
