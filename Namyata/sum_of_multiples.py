import unittest


def sumOfMultiples( n: int) -> int:
    ans = 0
    for x in range(1, n + 1):
        if x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
            ans += x

    return ans

class CorrectTestSumOfMultiples(unittest.TestCase):

    def test_sum_of_multiples(self):
        # Replace YourClass with the actual class name

        # Test Case 1
        self.assertEqual(sumOfMultiples(10), 40)

        # Test Case 2
        self.assertEqual(sumOfMultiples(20), 119)

        # Test Case 3
        self.assertEqual(sumOfMultiples(5), 8)

        # Test Case 4
        self.assertEqual(sumOfMultiples(15), 81)

        # Test Case 5
        self.assertEqual(sumOfMultiples(1), 0)


if __name__ == '__main__':
    unittest.main()
