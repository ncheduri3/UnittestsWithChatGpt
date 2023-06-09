# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
#


import unittest

def merge(nums1, m, nums2, n):
    for i in range(m, m + n):
        nums1[i] = nums2[i - m]
    nums1.sort()

class MergeTestCase(unittest.TestCase):
    def test_merge_lists(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        merge(nums1, m, nums2, n)
        expected_output = [1, 2, 2, 3, 5, 6]
        self.assertEqual(nums1, expected_output)

    def test_empty_list(self):
        nums1 = []
        m = 0
        nums2 = []
        n = 0
        merge(nums1, m, nums2, n)
        expected_output = []
        self.assertEqual(nums1, expected_output)

    def test_merge_into_empty_list(self):
        nums1 = [0, 0, 0]
        m = 0
        nums2 = [1, 2, 3]
        n = 3
        merge(nums1, m, nums2, n)
        expected_output = [1, 2, 3]
        self.assertEqual(nums1, expected_output)

    def test_merge_with_duplicate_elements(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 2, 3]
        n = 3
        merge(nums1, m, nums2, n)
        expected_output = [1, 2, 2, 2, 3, 3]
        self.assertEqual(nums1, expected_output)

    def test_merge_with_negative_numbers(self):
        nums1 = [-1, 0, 0, 0]
        m = 1
        nums2 = [-2, -3, -4]
        n = 3
        merge(nums1, m, nums2, n)
        expected_output = [-4, -3, -2, -1]
        self.assertEqual(nums1, expected_output)

if __name__ == '__main__':
    unittest.main()
#All unit tests are correct and passed