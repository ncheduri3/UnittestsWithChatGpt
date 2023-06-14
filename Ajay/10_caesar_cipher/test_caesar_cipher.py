import unittest
from caesar_cipher import caesar_cipher


class TestCaesarCipherRecursive(unittest.TestCase):

    def test_caesar_cipher(self):
        string = "Hello, World!"
        key = 3
        expected_result = "Khoor, Zruog!"
        self.assertEqual(caesar_cipher(string, key), expected_result)

    def test_empty_string(self):
        string = ""
        key = 5
        expected_result = ""
        self.assertEqual(caesar_cipher(string, key), expected_result)

    def test_special_characters(self):
        string = "Hello, #123!"
        key = 1
        expected_result = "Ifmmp, #123!"
        self.assertEqual(caesar_cipher(string, key), expected_result)


if __name__ == '__main__':
    unittest.main()
