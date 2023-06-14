import unittest
from typing import List
# Given an array of points on the X-Y plane points where points[i] = [xi, yi],
# return the area of the largest triangle that can be formed by any three different points.
# Answers within 10-5 of the actual answer will be accepted.
#
# Constraints:
#
# 3 <= points.length <= 50
# -50 <= xi, yi <= 50
# All the given points are unique.




class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area = 0
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    curr = abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
                    if curr > area:
                        area = curr
        return area


class TestLargestTriangleArea(unittest.TestCase):

    def test_valid_triangle_area(self):
        solution = Solution()
        points = [[0, 0], [0, 1], [1, 0]]
        result = solution.largestTriangleArea(points)
        self.assertAlmostEqual(result, 0.5, places=6)

    def test_zero_area(self):
        solution = Solution()
        points = [[0, 0], [0, 0], [0, 0]]
        result = solution.largestTriangleArea(points)
        self.assertAlmostEqual(result, 0, places=6)

    def test_large_triangle_area(self):
        solution = Solution()
        points = [[-50, -50], [0, 0], [50, -50], [0, 25]]
        result = solution.largestTriangleArea(points)
        self.assertAlmostEqual(result, 1250, places=6) # comment this and uncomment the next line to run
        # self.assertAlmostEqual(result, 3750, places=6)

    def test_single_point(self):
        solution = Solution()
        points = [[0, 0]]
        result = solution.largestTriangleArea(points)
        self.assertAlmostEqual(result, 0, places=6)

    def test_minimum_points(self):
        solution = Solution()
        points = [[0, 0], [1, 1], [2, 2]]
        result = solution.largestTriangleArea(points)
        self.assertAlmostEqual(result, 0, places=6)


if __name__ == '__main__':
    unittest.main()
