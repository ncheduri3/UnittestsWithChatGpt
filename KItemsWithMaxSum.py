import unittest
# Question :
# There is a bag that consists of items, each item has a number 1, 0, or -1 written on it.
#
# You are given four non-negative integers numOnes, numZeros, numNegOnes, and k.
#
# The bag initially contains:
#
# numOnes items with 1s written on them.
# numZeroes items with 0s written on them.
# numNegOnes items with -1s written on them.
# We want to pick exactly k items among the available items. Return the maximum possible sum of numbers written on the items.

def kItemsWithMaximumSum( numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
    return min((k, numOnes)) + (min((numNegOnes, k - numOnes - numZeros)) * -1 if (k - numOnes - numZeros) > 0 else 0)


# class TestKItemsWithMaximumSum(unittest.TestCase):
#
#     def test_k_items_with_maximum_sum(self):
#          # Replace YourClass with the actual class name
#
#         # Test Case 1
#         self.assertEqual(kItemsWithMaximumSum(5, 3, 2, 4), 4)
#
#         # Test Case 2
#         self.assertEqual(kItemsWithMaximumSum(2, 4, 1, 3), -1)
#
#         # Test Case 3
#         self.assertEqual(kItemsWithMaximumSum(0, 0, 0, 2), 0)
#
#         # Test Case 4
#         self.assertEqual(kItemsWithMaximumSum(10, 5, 3, 10), 8)
#
#         # Test Case 5
#         self.assertEqual(kItemsWithMaximumSum(3, 2, 1, 6), -2)
#
#
# if __name__ == '__main__':
#     unittest.main()

# Wrong interpretation of the code.

class CorrectTestKItemsWithMaximumSum(unittest.TestCase):

    def test_k_items_with_maximum_sum(self):
         # Replace YourClass with the actual class name

        # Test Case 1
        self.assertEqual(kItemsWithMaximumSum(5, 3, 2, 4), 4)

        # Test Case 2
        self.assertEqual(kItemsWithMaximumSum(2, 4, 1, 3), 2)

        # Test Case 3
        self.assertEqual(kItemsWithMaximumSum(0, 0, 0, 2), 0)

        # Test Case 4
        self.assertEqual(kItemsWithMaximumSum(10, 5, 3, 10), 10)

        # Test Case 5
        self.assertEqual(kItemsWithMaximumSum(3, 2, 1, 6), 2)


if __name__ == '__main__':
    unittest.main()
