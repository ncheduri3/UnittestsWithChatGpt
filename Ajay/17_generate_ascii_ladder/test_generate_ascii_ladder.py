import unittest
from generate_ascii_ladder import generate_string


class TestGenerateString(unittest.TestCase):

    def test_generate_string(self):
        n = 5
        k = 65
        expected = "ABCDE"
        self.assertEqual(generate_string(n, k), expected)

    def test_generate_string_with_empty_input(self):
        n = 0
        k = 65
        expected = ""
        self.assertEqual(generate_string(n, k), expected)

    def test_generate_string_with_negative_n(self):
        n = -3
        k = 65
        expected = ""
        self.assertEqual(generate_string(n, k), expected)

    def test_generate_string_with_zero_k(self):
        n = 5
        k = 0
        expected = "\x00\x01\x02\x03\x04"
        self.assertEqual(generate_string(n, k), expected)


if __name__ == '__main__':
    unittest.main()
