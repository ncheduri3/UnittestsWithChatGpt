import unittest
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
#
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
#
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.




def removeDuplicates(nums):
    j = 0
    for i in range(1, len(nums)):
        if nums[j] != nums[i]:
            j += 1
            nums[j] = nums[i]
    return j + 1

class RemoveDuplicatesTestCase(unittest.TestCase):
    def test_no_duplicates(self):
        nums = [1, 2, 3, 4, 5]
        expected_output = 5
        self.assertEqual(removeDuplicates(nums), expected_output)
        self.assertEqual(nums[:expected_output], [1, 2, 3, 4, 5])

    def test_duplicates_present(self):
        nums = [1, 1, 2, 2, 3]
        expected_output = 3
        self.assertEqual(removeDuplicates(nums), expected_output)
        self.assertEqual(nums[:expected_output], [1, 2, 3])

    def test_single_element_list(self):
        nums = [5]
        expected_output = 1
        self.assertEqual(removeDuplicates(nums), expected_output)
        self.assertEqual(nums[:expected_output], [5])

    def test_all_duplicates(self):
        nums = [2, 2, 2, 2, 2]
        expected_output = 1
        self.assertEqual(removeDuplicates(nums), expected_output)
        self.assertEqual(nums[:expected_output], [2])

if __name__ == '__main__':
    unittest.main()

#All unit tests are correct and passed