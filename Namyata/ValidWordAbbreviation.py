import unittest

def validWordAbbreviation(word: str, abbr: str) -> bool:
    p1 = p2 = 0
    while p1 < len(word) and p2 < len(abbr):
        if abbr[p2].isdigit():
            if abbr[p2] == '0':  # leading zeros are invalid
                return False
            shift = 0
            while p2 < len(abbr) and abbr[p2].isdigit():
                shift = (shift * 10) + int(abbr[p2])
                p2 += 1
            p1 += shift
        else:
            if word[p1] != abbr[p2]:
                return False
            p1 += 1
            p2 += 1
    return p1 == len(word) and p2 == len(abbr)



class TestValidWordAbbreviation(unittest.TestCase):
    def test_valid_abbreviation(self):
        word = "international"
        abbr = "i12al"
        # abbr = "i10al"
        expected = True
        self.assertEqual(validWordAbbreviation(word, abbr), expected)

    def test_invalid_abbreviation(self):
        word = "apple"
        abbr = "a4e"
        expected = False
        self.assertEqual(validWordAbbreviation(word, abbr), expected)

    def test_leading_zeros(self):
        word = "algorithm"
        abbr = "0l9m"
        expected = False
        self.assertEqual(validWordAbbreviation(word, abbr), expected)

    def test_same_length_word_and_abbr(self):
        word = "python"
        abbr = "p6n"
        expected = False
        self.assertEqual(validWordAbbreviation(word, abbr), expected)

if __name__ == '__main__':
    unittest.main()

# One positve branch test case is wrong. Uncomment to run the correct version.
