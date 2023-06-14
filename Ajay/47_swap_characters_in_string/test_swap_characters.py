import unittest
from swap_characters_in_string import swap_characters


class TestSwapCharacters(unittest.TestCase):
    def test_swap_characters_valid(self):
        self.assertEqual(swap_characters("Hello, World!", 1, 8), "Hollo, Werld!")
        self.assertEqual(swap_characters("Python", 0, 5), "nythoP")
        self.assertEqual(swap_characters("Testing", 2, 6), "Tegtins")
        self.assertEqual(swap_characters("OpenAI", 3, 4), "OpeAnI")
        
    def test_swap_invalid_indices(self):
        self.assertEqual(swap_characters("Hello", -1, 2), "Hello")
        self.assertEqual(swap_characters("Python", 4, 10), "Python")
        self.assertEqual(swap_characters("", 0, 3), "")
        
    def test_empty_string(self):
        self.assertEqual(swap_characters("", 0, 0), "")


if __name__ == '__main__':
    unittest.main()
