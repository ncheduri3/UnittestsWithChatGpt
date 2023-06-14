import unittest
from typing import List
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app",
# because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
#
# Constraints:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.




def isAlienSorted(words: List[str], order: str) -> bool:
    order_counter = {value: index for index, value in enumerate(order)}

    for i in range(len(words)-1):
        word1, word2 = words[i], words[i+1]

        for j in range(len(word1)):
            if j == len(word2):
                return False

            if word1[j] != word2[j]:
                if order_counter[word2[j]] < order_counter[word1[j]]:
                    return False

                break

    return True

class TestIsAlienSortedCorrected(unittest.TestCase):
    def test_empty_words(self):
        words = []
        order = "abcdefghijklmnopqrstuvwxyz"
        expected = True
        self.assertEqual(isAlienSorted(words, order), expected)

    def test_single_word(self):
        words = ["apple"]
        order = "abcdefghijklmnopqrstuvwxyz"
        expected = True
        self.assertEqual(isAlienSorted(words, order), expected)

    def test_sorted_words(self):
        words = ["hello", "leetcode", "world"]
        order = "hlabcdefgijkmnopqrstuvwxyz"
        expected = True
        self.assertEqual(isAlienSorted(words, order), expected)

    def test_unsorted_words(self):
        words = ["word", "world", "hello"]
        order = "hlabcdefgijkmnopqrstuvwxyz"
        expected = False
        self.assertEqual(isAlienSorted(words, order), expected)

    def test_same_starting_letters(self):
        words = ["apple", "ape", "application"]
        order = "abcdefghijklmnopqrstuvwxyz"
        expected = False
        self.assertEqual(isAlienSorted(words, order), expected)

    def test_same_words(self):
        words = ["same", "same", "same"]
        order = "abcdefghijklmnopqrstuvwxyz"
        expected = True
        self.assertEqual(isAlienSorted(words, order), expected)

    def test_custom_order(self):
        words = ["word", "leetcode", "hello"]
        order = "olhecdtbwjsykarxvznipgufmq"
        expected = False
        self.assertEqual(isAlienSorted(words, order), expected)

if __name__ == '__main__':
    unittest.main()
