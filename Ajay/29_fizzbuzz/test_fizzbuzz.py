import unittest
from fizzbuzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz_case_1(self):
        # Test case with x = 15
        expected_output = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz',
                           '13', '14', 'FizzBuzz']
        self.assertEqual(fizz_buzz(15), expected_output)

    def test_fizz_buzz_case_2(self):
        # Test case with x = 20
        expected_output = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13',
                           '14', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz']
        self.assertEqual(fizz_buzz(20), expected_output)

    def test_fizz_buzz_case_3(self):
        # Test case with x = 7
        expected_output = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7']
        self.assertEqual(fizz_buzz(7), expected_output)

    def test_fizz_buzz_case_4(self):
        # Test case with x = 1
        expected_output = ['1']
        self.assertEqual(fizz_buzz(1), expected_output)


if __name__ == '__main__':
    unittest.main()
