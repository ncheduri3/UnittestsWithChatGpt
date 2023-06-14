import unittest
from increasing_triplet import increasing_triplet


class TestIncreasingTriplet(unittest.TestCase):
    def test_empty_array(self):
        self.assertFalse(increasing_triplet([]))
    
    def test_single_element_array(self):
        self.assertFalse(increasing_triplet([5]))
        self.assertFalse(increasing_triplet([0]))
    
    def test_all_equal_elements(self):
        self.assertFalse(increasing_triplet([3, 3, 3, 3, 3]))
        self.assertFalse(increasing_triplet([0, 0, 0, 0, 0]))
    
    def test_all_increasing_elements(self):
        self.assertTrue(increasing_triplet([1, 2, 3, 4, 5]))
    
    def test_no_triplet_exists(self):
        self.assertFalse(increasing_triplet([5, 4, 3, 2, 1]))
    
    def test_triplet_exists(self):
        self.assertTrue(increasing_triplet([1, 3, 2, 4, 5]))
        self.assertTrue(increasing_triplet([5, 2, 4, 1, 3, 7]))


if __name__ == '__main__':
    unittest.main()
