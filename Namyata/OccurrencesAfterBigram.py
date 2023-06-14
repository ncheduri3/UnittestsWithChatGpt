import unittest
from typing import List
# Given two strings first and second, consider occurrences in some text of the form "first second third",
# where second comes immediately after first, and third comes immediately after second.
#
# Return an array of all the words third for each occurrence of "first second third".



def findOcurrences(text: str, first: str, second: str) -> List[str]:
    words = text.split()
    thirds = []
    for word in range(len(words) - 2):
        if words[word] == first and words[word + 1] == second:
            thirds.append(words[word + 2])
    return thirds

class TestFindOcurrencesCorrected(unittest.TestCase):
    def test_empty_text(self):
        text = "There"
        first = "hello"
        second = "world"
        expected = []
        self.assertEqual(findOcurrences(text, first, second), expected)

    def test_no_occurrences(self):
        text = "This is a sample sentence."
        first = "hello"
        second = "world"
        expected = []
        self.assertEqual(findOcurrences(text, first, second), expected)

    def test_single_occurrence(self):
        text = "hello world hello there world"
        first = "hello"
        second = "world"
        expected = ["hello"]
        self.assertEqual(findOcurrences(text, first, second), expected)

    def test_multiple_occurrences(self):
        text = "hello world hello there world hello"
        first = "hello"
        second = "world"
        expected = ["hello"]
        self.assertEqual(findOcurrences(text, first, second), expected)

    def test_consecutive_occurrences(self):
        text = "hello world hello world hello"
        first = "hello"
        second = "world"
        expected = ["hello", "hello"]
        self.assertEqual(findOcurrences(text, first, second), expected)

    def test_long_text(self):
        text = "this is a long text with multiple occurrences of first and second words. first second first second first second."
        first = "first"
        second = "second"
        expected = ["first", "first"]
        self.assertEqual(findOcurrences(text, first, second), expected)


if __name__ == '__main__':
    unittest.main()


#Test cases ensured coverage but were wrong. Added the correct test cases.
