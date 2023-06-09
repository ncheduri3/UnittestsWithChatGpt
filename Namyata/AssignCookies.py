# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
#
# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with;
# and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i,
# and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
#
# Constraints:
#
# 1 <= g.length <= 3 * 104
# 0 <= s.length <= 3 * 104
# 1 <= g[i], s[j] <= 231 - 1

import unittest
from typing import List

def findContentChildren(g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()

    ind = len(s) - 1
    res = 0

    for i in range(len(g) - 1, -1, -1):
        if ind >= 0 and g[i] <= s[ind]:
            res += 1
            ind -= 1

    return res

class TestFindContentChildren(unittest.TestCase):
    def test_equal_sizes(self):
        g = [1, 2, 3]
        s = [1, 2, 3]
        expected = 3
        self.assertEqual(findContentChildren(g, s), expected)

    def test_more_cookies_than_children(self):
        g = [1, 2, 3]
        s = [1, 2, 3, 4, 5]
        expected = 3
        self.assertEqual(findContentChildren(g, s), expected)

    def test_more_children_than_cookies(self):
        g = [1, 2, 3, 4, 5]
        s = [1, 2, 3]
        expected = 3
        self.assertEqual(findContentChildren(g, s), expected)

    def test_no_cookies(self):
        g = [1, 2, 3]
        s = []
        expected = 0
        self.assertEqual(findContentChildren(g, s), expected)

    def test_no_children(self):
        g = []
        s = [1, 2, 3]
        expected = 0
        self.assertEqual(findContentChildren(g, s), expected)

    def test_empty_lists(self):
        g = []
        s = []
        expected = 0
        self.assertEqual(findContentChildren(g, s), expected)

if __name__ == '__main__':
    unittest.main()


# All the test cases by ChapGPT passed