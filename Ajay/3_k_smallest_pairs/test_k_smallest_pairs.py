import unittest
from k_smallest_pairs import k_smallest_pairs


class TestKSmallestPairs(unittest.TestCase):
    def test_empty_lists(self):
        nums1 = []
        nums2 = []
        k = 3
        expected_output = []
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), expected_output)

    def test_single_element_lists(self):
        nums1 = [1]
        nums2 = [2]
        k = 1
        expected_output = [[1, 2]]
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), expected_output)

    def test_duplicate_elements(self):
        nums1 = [1, 1, 2]
        nums2 = [1, 2, 3]
        k = 4
        expected_output = [[1, 1], [1, 1], [1, 2], [1, 2]]
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), expected_output)

    def test_larger_lists(self):
        nums1 = [1, 4, 6]
        nums2 = [2, 3, 5]
        k = 5
        expected_output = [[1, 2], [1, 3], [1, 5], [4, 2], [4, 3]]
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), expected_output)

    def test_k_greater_than_pairs_count(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        k = 9
        expected_output = [[1, 4], [1, 5], [2, 4], [1,6], [2,5], [3, 4], [2, 6], [3, 5], [3, 6]]
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), expected_output)

    def test_empty_result(self):
        nums1 = [5, 6, 7]
        nums2 = [1, 2, 3]
        k = 0
        expected_output = []
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), expected_output)


if __name__ == '__main__':
    unittest.main()
