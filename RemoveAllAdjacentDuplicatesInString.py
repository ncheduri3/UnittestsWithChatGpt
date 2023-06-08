import unittest

def removeDuplicates(s: str) -> str:
    ans = []
    for a in s:
        if len(ans) > 0 and ans[-1] == a:
            ans.pop()
        else:
            ans.append(a)
    return "".join(ans)

class TestRemoveDuplicatesCorrected(unittest.TestCase):
    def test_no_duplicates(self):
        s = "abcd"
        expected = "abcd"
        self.assertEqual(removeDuplicates(s), expected)

    def test_duplicates_at_beginning(self):
        s = "aabbcccddd"
        expected = "cd"
        self.assertEqual(removeDuplicates(s), expected)

    def test_duplicates_at_end(self):
        s = "abcdefghhh"
        expected = "abcdefgh"
        self.assertEqual(removeDuplicates(s), expected)

    def test_duplicates_in_middle(self):
        s = "kaabbccddeel"
        expected = "kl"
        self.assertEqual(removeDuplicates(s), expected)

    def test_empty_string(self):
        s = ""
        expected = ""
        self.assertEqual(removeDuplicates(s), expected)

class TestRemoveDuplicates(unittest.TestCase):
    def test_no_duplicates(self):
        s = "abcd"
        expected = "abcd"
        self.assertEqual(removeDuplicates(s), expected)

    def test_duplicates_at_beginning(self):
        s = "aabbccdd"
        expected = "abcd"
        self.assertEqual(removeDuplicates(s), expected)

    def test_duplicates_at_end(self):
        s = "abcdefghhh"
        expected = "abcdefgh"
        self.assertEqual(removeDuplicates(s), expected)

    def test_duplicates_in_middle(self):
        s = "aabbccddee"
        expected = "abcde"
        self.assertEqual(removeDuplicates(s), expected)

    def test_empty_string(self):
        s = ""
        expected = ""
        self.assertEqual(removeDuplicates(s), expected)

if __name__ == '__main__':
    unittest.main()


#Few test cases by chatGPT are wrong. Corrected them.

