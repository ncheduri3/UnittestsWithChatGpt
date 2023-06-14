import unittest
# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.




def isHappy(n: int) -> bool:
    visited = set()  # set to keep track of visited numbers

    while n != 1:  # continue loop until happy or stuck in cycle
        sum_of_squares = 0

        # compute sum of squares of digits in n
        while n > 0:
            digit = n % 10
            sum_of_squares += digit ** 2
            n //= 10

        # check if sum is already visited
        if sum_of_squares in visited:
            return False

        # add sum to visited set
        visited.add(sum_of_squares)

        # set n to be the sum of squares for the next iteration
        n = sum_of_squares

    return True


class TestIsHappy(unittest.TestCase):
    def test_happy_number(self):
        n = 19
        expected = True
        self.assertEqual(isHappy(n), expected)

    def test_unhappy_number(self):
        n = 20
        expected = False
        self.assertEqual(isHappy(n), expected)

    def test_zero(self):
        n = 0
        expected = False
        self.assertEqual(isHappy(n), expected)

    def test_single_digit_happy_number(self):
        n = 7
        expected = True
        self.assertEqual(isHappy(n), expected)

    def test_single_digit_unhappy_number(self):
        n = 4
        expected = False
        self.assertEqual(isHappy(n), expected)


if __name__ == '__main__':
    unittest.main()

# All test cases by ChatGPT are correct.