import unittest
# Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.
#
# Recall that the number of set bits an integer has is the number of 1's present when written in binary.
#
# For example, 21 written in binary is 10101, which has 3 set bits.



def countPrimeSetBits(left: int, right: int) -> int:
    count = 0
    for i in range(left, right + 1):
        print(i, ":", bin(i))
        c = 0
        n = bin(i).count("1")
        for j in range(1, n + 1):
            if n % j == 0:
                c += 1
        if c == 2:
            count += 1
    return count

class TestCountPrimeSetBitsCorrected(unittest.TestCase):
    def test_left_equal_to_right(self):
        left = 10
        right = 10
        expected = 1
        self.assertEqual(countPrimeSetBits(left, right), expected)

    def test_no_prime_set_bits(self):
        left = 1
        right = 10
        expected = 6
        self.assertEqual(countPrimeSetBits(left, right), expected)

    def test_all_prime_set_bits(self):
        left = 10
        right = 15
        expected = 5
        self.assertEqual(countPrimeSetBits(left, right), expected)

    def test_mixed_prime_set_bits(self):
        left = 3
        right = 7
        expected = 4
        self.assertEqual(countPrimeSetBits(left, right), expected)

    def test_large_range(self):
        left = 1000
        right = 1010
        expected = 5
        self.assertEqual(countPrimeSetBits(left, right), expected)



if __name__ == '__main__':
    unittest.main()

#Wrong expected outputs by chat gpt. Corrected the test cases

