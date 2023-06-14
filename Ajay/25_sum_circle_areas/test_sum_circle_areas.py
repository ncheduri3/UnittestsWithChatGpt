import unittest
import math
from sum_circle_areas import sum_circle_areas


class TestSumCircleAreas(unittest.TestCase):

    def test_sum_circle_areas(self):
        self.assertAlmostEqual(sum_circle_areas(0), 0)
        self.assertAlmostEqual(sum_circle_areas(1), math.pi)
        self.assertAlmostEqual(sum_circle_areas(2), math.pi + 4 * math.pi)
        self.assertAlmostEqual(sum_circle_areas(3), math.pi + 4 * math.pi + 9 * math.pi)
        self.assertAlmostEqual(sum_circle_areas(5), math.pi + 4 * math.pi + 9 * math.pi + 16 * math.pi + 25 * math.pi)


if __name__ == '__main__':
    unittest.main()
