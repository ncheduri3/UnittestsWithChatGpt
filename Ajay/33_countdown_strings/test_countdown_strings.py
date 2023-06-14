import unittest
from countdown_strings import countdown_strings


class TestCountdownStrings(unittest.TestCase):
    def test_countdown_strings(self):
        # Test case 1
        result = countdown_strings(5)
        expected = ['1', '2 1', '3 2 1', '4 3 2 1', '5 4 3 2 1']
        self.assertEqual(result, expected)

    def test_for_3(self):
        # Test case 2
        result = countdown_strings(3)
        expected = ['1', '2 1', '3 2 1']
        self.assertEqual(result, expected)

    def test_with_1(self):
        # Test case 3
        result = countdown_strings(1)
        expected = ['1']
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
