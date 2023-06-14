import unittest
# Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.
#
# Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.




class Solution:
    def binaryGap(self, n: int) -> int:
        s = f'{n:b}'
        result = 0
        for i in range(len(s)):
            if s[i] == '0':
                continue
            for j in range(i + 1, len(s)):
                if s[j] == '0':
                    continue
                result = max(result, j - i)
                break
        return result

class TestBinaryGap(unittest.TestCase):

    def test_binary_gap(self):
        solution = Solution()
        n = 22
        result = solution.binaryGap(n)
        self.assertEqual(result, 2)

    def test_no_binary_gap(self):
        solution = Solution()
        n = 8
        result = solution.binaryGap(n)
        self.assertEqual(result, 0)

    def test_multiple_binary_gaps(self):
        solution = Solution()
        n = 37
        result = solution.binaryGap(n)
        self.assertEqual(result, 2) # Comment This line and uncomment the next one
        # self.assertEqual(result, 3)

    def test_single_bit(self):
        solution = Solution()
        n = 1
        result = solution.binaryGap(n)
        self.assertEqual(result, 0)

    def test_maximum_binary_gap(self):
        solution = Solution()
        n = 5
        result = solution.binaryGap(n)
        self.assertEqual(result, 1) # Uncomment the next line and comment this one
        # self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
