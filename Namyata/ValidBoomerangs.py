import unittest
from typing import List
# Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.
#
# A boomerang is a set of three points that are all distinct and not in a straight line.
#
# Constraints:
#
# points.length == 3
# points[i].length == 2
# 0 <= xi, yi <= 100



def isBoomerang(points: List[List[int]]) -> bool:
    a, b, c = points
    return (b[1] - a[1]) * (c[0] - b[0]) != (c[1] - b[1]) * (b[0] - a[0])

class TestIsBoomerang(unittest.TestCase):
    def test_valid_boomerang(self):
        points = [[1, 1], [2, 3], [3, 2]]
        expected = True
        self.assertEqual(isBoomerang(points), expected)

    def test_invalid_boomerang(self):
        points = [[1, 1], [2, 2], [3, 3]]
        expected = False
        self.assertEqual(isBoomerang(points), expected)

    def test_horizontal_line(self):
        points = [[1, 1], [2, 1], [3, 1]]
        expected = False
        self.assertEqual(isBoomerang(points), expected)

    def test_vertical_line(self):
        points = [[1, 1], [1, 2], [1, 3]]
        expected = False
        self.assertEqual(isBoomerang(points), expected)

    def test_same_points(self):
        points = [[1, 1], [1, 1], [1, 1]]
        expected = False
        self.assertEqual(isBoomerang(points), expected)

if __name__ == '__main__':
    unittest.main()
# all unit tests passed