import unittest
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.



def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0 and nums[slow] == 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]

        # wait while we find a non-zero element to swap with you
        if nums[slow] != 0:
            slow += 1


class TestMoveZeroes(unittest.TestCase):
    def test_move_zeroes(self):
        nums = [0, 1, 0, 3, 12]
        expected = [1, 3, 12, 0, 0]
        moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_no_zeroes(self):
        nums = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_all_zeroes(self):
        nums = [0, 0, 0, 0, 0]
        expected = [0, 0, 0, 0, 0]
        moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_mixed_elements(self):
        nums = [0, 2, 0, 1, 0, 3, 0, 0, 12]
        expected = [2, 1, 3, 12, 0, 0, 0, 0, 0]
        moveZeroes(nums)
        self.assertEqual(nums, expected)

if __name__ == '__main__':
    unittest.main()

# All test cases by ChatGPT are correct.
