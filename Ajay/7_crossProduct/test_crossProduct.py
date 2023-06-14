import unittest
from crossProduct import cross_product


class TestCalculateCrossProduct(unittest.TestCase):
    def test_cross_product_calculation(self):
        vector1 = [1, 2, 3]
        vector2 = [4, 5, 6]
        expected_result = [-3, 6, -3]
        self.assertEqual(cross_product(vector1, vector2), expected_result)

    def test_invalid_vector_length(self):
        vector1 = [1, 2, 3, 4]
        vector2 = [4, 5, 6]
        self.assertRaises(ValueError, cross_product, vector1, vector2)

        vector1 = [1, 2]
        vector2 = [4, 5, 6]
        self.assertRaises(ValueError, cross_product, vector1, vector2)


if __name__ == '__main__':
    unittest.main()
