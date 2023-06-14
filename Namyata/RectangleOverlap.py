import unittest
from typing import List

# An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.
#
# Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.
#
# Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.
#
# rec1.length == 4
# rec2.length == 4
# -109 <= rec1[i], rec2[i] <= 109
# rec1 and rec2 represent a valid rectangle with a non-zero area.


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def overlap(a1, a2, b1, b2):
            if a1 > b1:
                a1, a2, b1, b2 = b1, b2, a1, a2

            if a2 <= b1:
                return False
            else:
                return True

        ax1, ay1, ax2, ay2 = rec1[0], rec1[1], rec1[2], rec1[3]
        bx1, by1, bx2, by2 = rec2[0], rec2[1], rec2[2], rec2[3]
        if not overlap(ax1, ax2, bx1, bx2) or not overlap(ay1, ay2, by1, by2):
            return False
        else:
            return True

class TestIsRectangleOverlap(unittest.TestCase):

    def test_overlap(self):
        solution = Solution()
        rec1 = [0, 0, 2, 2]
        rec2 = [1, 1, 3, 3]
        result = solution.isRectangleOverlap(rec1, rec2)
        self.assertTrue(result)

    def test_no_overlap(self):
        solution = Solution()
        rec1 = [0, 0, 1, 1]
        rec2 = [2, 2, 3, 3]
        result = solution.isRectangleOverlap(rec1, rec2)
        self.assertFalse(result)

    def test_partial_overlap(self):
        solution = Solution()
        rec1 = [0, 0, 2, 2]
        rec2 = [1, 1, 2, 3]
        result = solution.isRectangleOverlap(rec1, rec2)
        self.assertTrue(result)

    def test_same_rectangle(self):
        solution = Solution()
        rec1 = [0, 0, 2, 2]
        rec2 = [0, 0, 2, 2]
        result = solution.isRectangleOverlap(rec1, rec2)
        self.assertTrue(result)

    def test_single_point_overlap(self):
        solution = Solution()
        rec1 = [0, 0, 1, 1]
        rec2 = [1, 1, 2, 2]
        result = solution.isRectangleOverlap(rec1, rec2)
        self.assertFalse(result)

    def test_minimum_area_rectangle(self):
        solution = Solution()
        rec1 = [0, 0, 0, 0]
        rec2 = [0, 0, 0, 0]
        result = solution.isRectangleOverlap(rec1, rec2)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

# All test cases worked.