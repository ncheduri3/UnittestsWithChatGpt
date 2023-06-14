import unittest
from firstDuplicateInList import first_duplicate_in_list


class TestFirstDuplicateInList(unittest.TestCase):
    def test_duplicate_found(self):
        lst = [1, 2, 3, 4, 3, 5]
        self.assertEqual(first_duplicate_in_list(lst), 3)

        lst = ['a', 'b', 'c', 'd', 'c', 'e']
        self.assertEqual(first_duplicate_in_list(lst), 'c')

        lst = [2.71, 3.14, 1.41, 2.71, 3.14]
        self.assertEqual(first_duplicate_in_list(lst), 2.71)

    def test_no_duplicate_found(self):
        lst = [1, 2, 3, 4, 5]
        self.assertIsNone(first_duplicate_in_list(lst))

        lst = ['a', 'b', 'c', 'd', 'e']
        self.assertIsNone(first_duplicate_in_list(lst))

        lst = [2.71, 3.14, 1.41]
        self.assertIsNone(first_duplicate_in_list(lst))


if __name__ == '__main__':
    unittest.main()
