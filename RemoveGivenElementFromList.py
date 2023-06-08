import unittest

def removeElement(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)

class RemoveElementTestCase(unittest.TestCase):
    def test_remove_element(self):
        nums = [3, 2, 2, 3]
        val = 3
        expected_output = 2
        self.assertEqual(removeElement(nums, val), expected_output)
        self.assertEqual(nums, [2, 2])

    def test_remove_all_elements(self):
        nums = [1, 1, 1, 1]
        val = 1
        expected_output = 0
        self.assertEqual(removeElement(nums, val), expected_output)
        self.assertEqual(nums, [])

    def test_remove_no_elements(self):
        nums = [4, 5, 6]
        val = 1
        expected_output = 3
        self.assertEqual(removeElement(nums, val), expected_output)
        self.assertEqual(nums, [4, 5, 6])


    def test_remove_duplicate_elements(self):
        nums = [2, 2, 3, 3, 4]
        val = 3
        expected_output = 3
        self.assertEqual(removeElement(nums, val), expected_output)
        self.assertEqual(nums, [2, 2, 4])

if __name__ == '__main__':
    unittest.main()

#All unit tests are correct and passed
