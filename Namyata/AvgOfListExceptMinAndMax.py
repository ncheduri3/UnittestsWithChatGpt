import unittest
# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
#
# Return the average salary of employees excluding the minimum and maximum salary.
# Answers within 10-5 of the actual answer will be accepted

def some_function( salary) -> float:
    salary.sort()
    sum = 0
    for s in salary:
        sum += s
    return (sum - salary[0] - salary[-1]) / (len(salary) - 2)


class TestSomeFunction(unittest.TestCase):

    #corrected test cases
    def test_some_function(self):
          # Replace YourClass with the actual class name

        # Test Case 1
        salary = [1000, 2000, 3000, 4000, 5000]
        self.assertAlmostEqual(some_function(salary), 3000.0)

        # Test Case 2
        salary = [500, 800, 1200, 1500]
        self.assertAlmostEqual(some_function(salary), 1000.0)

        # Test Case 3
        salary = [2500, 3500, 2000, 4500]
        self.assertAlmostEqual(some_function(salary), 3000.0)

        # Test Case 4
        salary = [10000, 15000, 12000, 9000, 18000]
        self.assertAlmostEqual(some_function(salary), 12333.333333333334)

        # Test Case 5
        salary = [5000, 3000, 2000, 4000, 6000, 1000]
        self.assertAlmostEqual(some_function(salary), 3500.0)


if __name__ == '__main__':
    unittest.main()
