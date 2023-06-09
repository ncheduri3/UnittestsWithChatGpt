# We can represent a sentence as an array of words, for example, the sentence "I am happy with leetcode" can be represented as arr = ["I","am",happy","with","leetcode"].

# Given two sentences sentence1 and sentence2 each represented as a string array and given an array of string pairs similarPairs where similarPairs[i] = [xi, yi] indicates that the two words xi and yi are similar.
#
# Return true if sentence1 and sentence2 are similar, or false if they are not similar.
#
# Two sentences are similar if:
#
# They have the same length (i.e., the same number of words)
# sentence1[i] and sentence2[i] are similar.
# Notice that a word is always similar to itself, also notice that the similarity relation is not transitive. For example, if the words a and b are similar, and the words b and c are similar, a and c are not necessarily similar.
#
# Constraints:
#
# 1 <= sentence1.length, sentence2.length <= 1000
# 1 <= sentence1[i].length, sentence2[i].length <= 20
# sentence1[i] and sentence2[i] consist of English letters.
# 0 <= similarPairs.length <= 1000
# similarPairs[i].length == 2
# 1 <= xi.length, yi.length <= 20
# xi and yi consist of lower-case and upper-case English letters.
# All the pairs (xi, yi) are distinct.


import unittest
from typing import List

def areSentencesSimilar(sentence1, sentence2, similarPairs) :
    return len(sentence1) == len(sentence2) and all \
        (s1 == s2 or [s1, s2] in similarPairs or [s2, s1] in similarPairs for s1, s2 in zip(sentence1, sentence2))

class TestAreSentencesSimilar(unittest.TestCase):

    def test_equal_sentences(self):
        sentence1 = ["Hello", "World"]
        sentence2 = ["Hello", "World"]
        similarPairs = []
        result = areSentencesSimilar(sentence1, sentence2, similarPairs)
        self.assertTrue(result)

    def test_similar_pairs(self):
        sentence1 = ["Hello", "World"]
        sentence2 = ["Hola", "Mundo"]
        similarPairs = [["Hello", "Hola"], ["World", "Mundo"]]
        result = areSentencesSimilar(sentence1, sentence2, similarPairs)
        self.assertTrue(result)

    def test_no_similar_pairs(self):
        sentence1 = ["Hello", "World"]
        sentence2 = ["Hola", "Mundo"]
        similarPairs = []
        result = areSentencesSimilar(sentence1, sentence2, similarPairs)
        self.assertFalse(result)

    def test_mismatched_lengths(self):
        sentence1 = ["Hello", "World"]
        sentence2 = ["Hello"]
        similarPairs = []
        result = areSentencesSimilar(sentence1, sentence2, similarPairs)
        self.assertFalse(result)

    def test_empty_sentences(self):
        sentence1 = []
        sentence2 = []
        similarPairs = []
        result = areSentencesSimilar(sentence1, sentence2, similarPairs)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()


# All tests were correct. 