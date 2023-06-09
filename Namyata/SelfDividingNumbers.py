# A self-dividing number is a number that is divisible by every digit it contains.
#
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.
#
# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].
#
# 1 <= left <= right <= 104

import unittest
from typing import List


def selfDividingNumbers(left: int, right: int) -> List[int]:
    list1 = []

    def selfdiv(num):
        current = 0
        x = num
        while num > 0:
            current = num % 10
            if current == 0:
                return False
            if x % current != 0:
                return False
            num = num // 10
        return True

    for i in range(left, right + 1):
        if selfdiv(i):
            list1.append(i)
    return list1


class TestSelfDividingNumbers(unittest.TestCase):

    def test_valid_range(self):
        result = selfDividingNumbers(1, 100)
        self.assertListEqual(result,
                             [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22, 24, 33, 36, 44, 48, 55, 66, 77, 88, 99])

    def test_empty_range(self):
        result = selfDividingNumbers(10, 9)
        self.assertListEqual(result, [])

    def test_single_number(self):
        result = selfDividingNumbers(22, 22)
        self.assertListEqual(result, [22])

    def test_no_self_dividing_numbers(self):
        result = selfDividingNumbers(30, 35)
        self.assertListEqual(result, []) # comment this and uncomment the next line
        # self.assertListEqual(result, [33])

    def test_all_self_dividing_numbers(self):
        result = selfDividingNumbers(1, 100)
        self.assertListEqual(result,
                             [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22, 24, 33, 36, 44, 48, 55, 66, 77, 88, 99])


if __name__ == '__main__':
    unittest.main()

# One test failed. Uncomment the line to run the correct version

