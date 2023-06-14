import unittest
# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.
#
# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.
#
# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
#
# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.
#
# Constraints:
#
# 1 <= s.length <= 105
# s[i] is either '(' or ')'.
# s is a valid parentheses string.




def removeOuterParentheses(s: str) -> str:
    ans, cnt = [], 0
    for ch in s:
        if ch == '(' and cnt > 0:
            ans.append(ch)
        if ch == ')' and cnt > 1:
            ans.append(ch)
        cnt += 1 if ch == '(' else -1
    return "".join(ans)

class TestRemoveOuterParenthesesCorrected(unittest.TestCase):
    def test_single_parentheses(self):
        s = "()"
        expected = ""
        self.assertEqual(removeOuterParentheses(s), expected)

    def test_nested_parentheses(self):
        s = "(()())"
        expected = "()()"
        self.assertEqual(removeOuterParentheses(s), expected)

    def test_multiple_groups(self):
        s = "()()(()())"
        expected = "()()"
        self.assertEqual(removeOuterParentheses(s), expected)

    def test_no_outer_parentheses(self):
        s = "()()()"
        expected = ""
        self.assertEqual(removeOuterParentheses(s), expected)

    def test_empty_string(self):
        s = ""
        expected = ""
        self.assertEqual(removeOuterParentheses(s), expected)

if __name__ == '__main__':
    unittest.main()


#The test cases by the chapGPT were wrong. Corrected them.