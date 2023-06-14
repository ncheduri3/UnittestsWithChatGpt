import unittest
from validate_parenthesis_brackets_in_string import validate_parenthesis_brackets_in_string


class TestValidateParenthesisBracketsInString(unittest.TestCase):
    def test_valid_string(self):
        # Valid strings with balanced parentheses and brackets
        self.assertTrue(validate_parenthesis_brackets_in_string(""))
        self.assertTrue(validate_parenthesis_brackets_in_string("()"))
        self.assertTrue(validate_parenthesis_brackets_in_string("[]"))
        self.assertTrue(validate_parenthesis_brackets_in_string("()[]"))
        self.assertTrue(validate_parenthesis_brackets_in_string("([])"))
        self.assertTrue(validate_parenthesis_brackets_in_string("[()]"))
        self.assertTrue(validate_parenthesis_brackets_in_string("[()[]]"))

    def test_invalid_string(self):
        # Invalid strings with unbalanced parentheses and brackets
        self.assertFalse(validate_parenthesis_brackets_in_string("("))
        self.assertFalse(validate_parenthesis_brackets_in_string(")"))
        self.assertFalse(validate_parenthesis_brackets_in_string("["))
        self.assertFalse(validate_parenthesis_brackets_in_string("]"))
        self.assertFalse(validate_parenthesis_brackets_in_string(")("))
        self.assertFalse(validate_parenthesis_brackets_in_string("(]"))
        self.assertFalse(validate_parenthesis_brackets_in_string("([)]"))
        self.assertFalse(validate_parenthesis_brackets_in_string("[(]"))

    def test_other_characters(self):
        # Strings with other characters
        self.assertTrue(validate_parenthesis_brackets_in_string("A(B)C[D]E"))
        self.assertTrue(validate_parenthesis_brackets_in_string("(3 + 2) * [5 - 1]"))
        self.assertTrue(validate_parenthesis_brackets_in_string("Hello (World) [{Wo}w!]"))
        self.assertFalse(validate_parenthesis_brackets_in_string("(3 + [2) * {}5 - 1]"))

    def test_empty_string(self):
        # Empty string
        self.assertTrue(validate_parenthesis_brackets_in_string(""))


if __name__ == "__main__":
    unittest.main()
