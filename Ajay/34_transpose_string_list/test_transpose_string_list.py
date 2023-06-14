import unittest
from transpose_string_list import transpose_strings


class TestTransposeStrings(unittest.TestCase):
    def test_strings_len_6(self):
        # Test case 1
        input_list = ['runner', 'atomic', 'dry in']
        expected = ['rad', 'utr', 'noy', 'nm ', 'eii', 'rcn']
        result = transpose_strings(input_list)
        self.assertEqual(result, expected)

    def test_strings_len_3(self):
        # Test case 2
        input_list = ['abc', 'def', 'ghi']
        expected = ['adg', 'beh', 'cfi']
        result = transpose_strings(input_list)
        self.assertEqual(result, expected)

    def test_empty_strings(self):
        # Test case 3
        input_list = ['', '', '']
        expected = []
        result = transpose_strings(input_list)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
