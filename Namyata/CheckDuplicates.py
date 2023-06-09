import unittest

def containsDuplicate(nums):
    return len(set(nums)) != len(nums)

class ContainsDuplicateTestCase(unittest.TestCase):
    def test_duplicates_present(self):
        nums = [1, 2, 3, 1]
        self.assertTrue(containsDuplicate(nums))

    def test_no_duplicates(self):
        nums = [1, 2, 3, 4]
        self.assertFalse(containsDuplicate(nums))

    def test_empty_array(self):
        nums = []
        self.assertFalse(containsDuplicate(nums))

    def test_single_element_array(self):
        nums = [5]
        self.assertFalse(containsDuplicate(nums))

    def test_duplicates_with_negative_numbers(self):
        nums = [-1, 2, -1, 4]
        self.assertTrue(containsDuplicate(nums))

if __name__ == '__main__':
    unittest.main()
#All unit tests are correct and passed
