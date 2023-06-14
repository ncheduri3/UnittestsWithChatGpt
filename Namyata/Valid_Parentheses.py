import unittest
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


def isValid( s: str) -> bool:
    stack = []
    for char in s:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        else:
            if not stack:
                return False
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return not stack




class TestIsValid(unittest.TestCase):

    def test_is_valid(self):
        # Replace YourClass with the actual class name

        # Test Case 1
        s = "()"
        self.assertTrue(isValid(s))

        # Test Case 2
        s = "()[]{}"
        self.assertTrue(isValid(s))

        # Test Case 3
        s = "(]"
        self.assertFalse(isValid(s))

        # Test Case 4
        s = "([)]"
        self.assertFalse(isValid(s))

        # Test Case 5
        s = "{[]}"
        self.assertTrue(isValid(s))

        # Additional Test Case 6
        s = "({[()]})"
        self.assertTrue(isValid(s))

        # Additional Test Case 7
        s = ""
        self.assertTrue(isValid(s))

        # Additional Test Case 8
        s = "[[[]]]"
        self.assertTrue(isValid(s))

        # Additional Test Case 9
        s = "[[[[]]"
        self.assertFalse(isValid(s))

if __name__ == '__main__':
    unittest.main()

# Valid test cases.


