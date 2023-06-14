import unittest
from staircase_word import generate_word


class TestGenerateWord(unittest.TestCase):
    def test_two_words(self):
        input_str = "run swim"
        expected_output = "rw"
        self.assertEqual(generate_word(input_str), expected_output)
        
    def test_three_words(self):
        input_str = "apple orange banana"
        expected_output = "arn"
        self.assertEqual(generate_word(input_str), expected_output)

    def test_one_words(self):
        input_str = "cat"
        expected_output = "c"
        self.assertEqual(generate_word(input_str), expected_output)

    def test_empty_string(self):
        input_str = ""
        expected_output = ""
        self.assertEqual(generate_word(input_str), expected_output)


if __name__ == '__main__':
    unittest.main()
