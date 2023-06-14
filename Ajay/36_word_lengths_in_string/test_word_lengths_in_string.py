import unittest
from word_lengths_in_string import length_of_each_word


class TestLengthOfEachWord(unittest.TestCase):
    def test_multiple_words(self):
        s = "Hello World"
        expected_lengths = [5, 5]
        self.assertEqual(length_of_each_word(s), expected_lengths)

    def test_single_word(self):
        s = "Python"
        expected_lengths = [6]
        self.assertEqual(length_of_each_word(s), expected_lengths)

    def test_trailing_spaces(self):
        s = "   OpenAI   Language   Model   "
        expected_lengths = [6, 8, 5]
        self.assertEqual(length_of_each_word(s), expected_lengths)

    def test_only_spaces(self):
        s = "   "
        expected_lengths = []
        self.assertEqual(length_of_each_word(s), expected_lengths)

    def test_empty_string(self):
        s = ""
        expected_lengths = []
        self.assertEqual(length_of_each_word(s), expected_lengths)


if __name__ == '__main__':
    unittest.main()
