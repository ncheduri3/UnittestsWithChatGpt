import unittest
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".



def longestCommonPrefix(strs):
    ans = ""
    v = sorted(strs)
    first = v[0]
    last = v[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return ans
        ans += first[i]
    return ans

class LongestCommonPrefixTestCase(unittest.TestCase):
    def test_common_prefix_present(self):
        strs = ["flower", "flow", "flight"]
        expected_output = "fl"
        self.assertEqual(longestCommonPrefix(strs), expected_output)

    def test_no_common_prefix(self):
        strs = ["dog", "racecar", "car"]
        expected_output = ""
        self.assertEqual(longestCommonPrefix(strs), expected_output)

    def test_single_element_array(self):
        strs = ["apple"]
        expected_output = "apple"
        self.assertEqual(longestCommonPrefix(strs), expected_output)

    def test_common_prefix_with_empty_string(self):
        strs = ["apple", ""]
        expected_output = ""
        self.assertEqual(longestCommonPrefix(strs), expected_output)

if __name__ == '__main__':
    unittest.main()
