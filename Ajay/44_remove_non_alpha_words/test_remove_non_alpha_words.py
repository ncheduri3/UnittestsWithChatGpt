import unittest
from remove_non_alpha_words import remove_non_alpha_words


class TestRemoveNonAlphaWords(unittest.TestCase):
    def test_remove_non_alpha_words_with_mix_of_alpha_and_non_alpha(self):
        string = "Hello 123 world! This is a test. with mix123alpha"
        expected_output = "Hello This is a with"
        self.assertEqual(remove_non_alpha_words(string), expected_output)

    def test_remove_non_alpha_words_with_alpha_and_numeric(self):
        string = "Python programming is fun with numbers 123. Alpha123Numeric"
        expected_output = "Python programming is fun with numbers"
        self.assertEqual(remove_non_alpha_words(string), expected_output)

    def test_remove_non_alpha_words_with_hyphen_separated_words(self):
        string = "Keep words with hyphen-separated and alpha-numeric 123a456. MixAlpha123Numeric"
        expected_output = "Keep words with and"
        self.assertEqual(remove_non_alpha_words(string), expected_output)

    def test_remove_non_alpha_words_with_only_alphabetic_words(self):
        string = "Only alphabetic words should remain. MixAlpha123Numeric"
        expected_output = "Only alphabetic words should"
        self.assertEqual(remove_non_alpha_words(string), expected_output)


if __name__ == '__main__':
    unittest.main()
