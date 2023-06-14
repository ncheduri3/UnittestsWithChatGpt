import unittest
# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
#
# A common string is a string that appeared in both list1 and list2.
#
# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
#
# Return all the common strings with the least index sum. Return the answer in any order.




class Solution:
    def findRestaurant(self, list1, list2) :
        d = {}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    d[list1[i]] = i + j
        lst = []
        for i, j in d.items():
            if j == min(d.values()):
                lst.append(i)
        return lst


class TestFindRestaurant(unittest.TestCase):
    def test_example_case(self):
        s = Solution()
        list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
        list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
        expected = ["Shogun"]
        self.assertEqual(s.findRestaurant(list1, list2), expected)

    def test_multiple_common_restaurants(self):
        s = Solution()
        list1 = ["KFC", "Burger King", "Pizza Hut", "McDonald's"]
        list2 = ["Burger King", "Pizza Hut", "McDonald's", "KFC"]
        expected = ["Burger King", "Pizza Hut", "McDonald's", "KFC"]
        # expected = ["Burger King"]
        self.assertEqual(s.findRestaurant(list1, list2), expected)

    def test_no_common_restaurant(self):
        s = Solution()
        list1 = ["Subway", "Starbucks", "Chipotle"]
        list2 = ["McDonald's", "Taco Bell", "Wendy's"]
        expected = []
        self.assertEqual(s.findRestaurant(list1, list2), expected)

    def test_empty_lists(self):
        s = Solution()
        list1 = []
        list2 = []
        expected = []
        self.assertEqual(s.findRestaurant(list1, list2), expected)

    def test_large_input(self):
        s = Solution()
        list1 = ["Restaurant" + str(i) for i in range(1000)]
        list2 = ["Cafe" + str(i) for i in range(1000)]
        expected = ["Restaurant0", "Cafe0"]
        # expected = []
        self.assertEqual(s.findRestaurant(list1, list2), expected)


if __name__ == '__main__':
    unittest.main()

# 2 tests failed. Uncomment to run correct versions.
