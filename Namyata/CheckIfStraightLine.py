import unittest
# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents
# the coordinate of a point. Check if these points make a straight line in the XY plane.



def checkStraightLine(coordinates):
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]

    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        if (x - x0) * (y1 - y0) != (y - y0) * (x1 - x0):
            return False

    return True

class CheckStraightLineTestCase(unittest.TestCase):
    def test_straight_line(self):
        coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
        self.assertTrue(checkStraightLine(coordinates))

    def test_not_straight_line(self):
        coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 7]]
        self.assertFalse(checkStraightLine(coordinates))

    def test_collinear_points(self):
        coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
        self.assertTrue(checkStraightLine(coordinates))

    def test_vertical_line(self):
        coordinates = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6]]
        self.assertTrue(checkStraightLine(coordinates))

    def test_horizontal_line(self):
        coordinates = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]]
        self.assertTrue(checkStraightLine(coordinates))

if __name__ == '__main__':
    unittest.main()

#All unit tests are correct and passed