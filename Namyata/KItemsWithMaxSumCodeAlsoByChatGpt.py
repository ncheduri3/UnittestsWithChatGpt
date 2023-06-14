import unittest
def kItemsWithMaximumSum(numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
    ones_taken = min(k, numOnes)
    remaining_k = k - ones_taken
    neg_ones_taken = min(remaining_k, numNegOnes) * -1 if remaining_k > 0 else 0

    return ones_taken + neg_ones_taken

# wrong code generation. Misses the case when number of zeroes are greater than numones - k.




class TestKItemsWithMaximumSum(unittest.TestCase):

    def test_k_items_with_maximum_sum_corrected(self):
        # Test Case 1
        numOnes = 5
        numZeros = 3
        numNegOnes = 2
        k = 4
        self.assertEqual(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k), 4)

        # Test Case 2
        numOnes = 2
        numZeros = 4
        numNegOnes = 1
        k = 3
        self.assertEqual(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k), 1) # should have been 0 - missed case!!

        # Test Case 3
        numOnes = 0
        numZeros = 0
        numNegOnes = 0
        k = 2
        self.assertEqual(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k), 0)

        # Test Case 4
        numOnes = 10
        numZeros = 5
        numNegOnes = 3
        k = 10
        self.assertEqual(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k), 10)

        # Test Case 5
        numOnes = 3
        numZeros = 2
        numNegOnes = 1
        k = 6
        self.assertEqual(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k), 2)

    # def test_k_items_with_maximum_sum(self):
    #     # Test Case 1
    #     numOnes = 5
    #     numZeros = 3
    #     numNegOnes = 2
    #     k = 4
    #     self.assertEqual(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k), 3)
    #
    #     # Test Case 2
    #     numOnes = 2
    #     numZeros = 4
    #     numNegOnes = 1
    #     k = 3
    #     self.assertEqual(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k), -1)
    #
    #     # Test Case 3
    #     numOnes = 0
    #     numZeros = 0
    #     numNegOnes = 0
    #     k = 2
    #     self.assertEqual(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k), 0)
    #
    #     # Test Case 4
    #     numOnes = 10
    #     numZeros = 5
    #     numNegOnes = 3
    #     k = 10
    #     self.assertEqual(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k), 8)
    #
    #     # Test Case 5
    #     numOnes = 3
    #     numZeros = 2
    #     numNegOnes = 1
    #     k = 6
    #     self.assertEqual(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k), -2)

if __name__ == '__main__':
    unittest.main()