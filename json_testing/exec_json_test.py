import pandas as pd
import unittest
import subprocess
import os
import re


class TestJsonConversion(unittest.TestCase):
    df = pd.read_json('unit_test_combined.json', orient='records', lines=True)

    def test_function_names(self):
        expected_Ajay = ["arrangeCoins", "findDelayedArrivalTime", "findContentChildren", "some_function", "binaryGap", "containsDuplicate", "isAnagram", "numUniqueEmails", "isHappy", "isMonotonic", "checkStraightLine", "detectCapitalUse", "countNegatives", "firstUniqChar", "generatePossibleNextMoves", "divisorGame", "numJewelsInStones", "kItemsWithMaximumSum", "kItemsWithMaximumSum", "largestTriangleArea", "lastStoneWeight", "longestCommonPrefix", "findLHS", "maxProfit", "merge", "mergeTwoLists", "findRestaurant", "moveZeroes", "findOcurrences", "isPalindrome", "check_is_prime", "countPrimeSetBits", "isRectangleOverlap", "removeDuplicates", "removeDuplicates", "removeElement", "removeOuterParentheses", "reverseVowels", "romanToInt", "selfDividingNumbers", "areSentencesSimilar", "sortedSquares", "sumOfMultiples", "surfaceArea", "twoSum", "isValid", "isBoomerang", "validWordAbbreviation", "isAlienSorted"]
        expected_Namyata = ["increasing_triplet", "intersection", "k_smallest_pairs", "kth_smallest_in_matrix", "first_duplicate_in_list", "nth_digit_in_sequence", "cross_product", "fib", "reverse_string_recursive", "caesar_cipher", "indices_of_occurrences", "is_arithmetic_sequence", "reverse_quick_sort", "find_div_by_a_or_b", "transpose_matrix", "count_character_occurrences", "generate_string", "merge_sort", "find_substrings_with_char", "merge_strings_by_ascii", "rotate_matrix", "find_first_repeating_subsequence", "is_valid_email", "is_substring", "sum_circle_areas", "substring_occurs_twice", "calculate_knight_moves", "calculate_sum_exceed_index", "fizz_buzz", "validate_parenthesis_brackets_in_string", "pascal_triangle", "get_directories_from_path", "countdown_strings", "transpose_strings", "heapsort", "length_of_each_word", "min_moves_for_equal_elements", "generate_word", "partition_lists", "count_anagram_substring_pairs", "longest_repeating_substring", "validate_time_format", "generate_frequency_dictionary", "remove_non_alpha_words", "staircase_string", "compute_time_difference", "swap_characters", "find_kth_largest", "count_primes", "h_index", "heapify"]
        expected_Ajay.extend(expected_Namyata)
        expected = expected_Ajay

        check = list(self.df['function_name'])
        self.assertEqual(expected, check)

    def test_headers(self):
        for header in self.df['header']:
            splits = header.split('\n')
            if len(splits) == 3: # No import statements so only function definition
                self.assertEqual('', splits[0])
                self.assertEqual('def ', splits[1][:4])
                self.assertEqual('', splits[2])
            else: # One or more import statement and one function definition
                importlines = []
                for i, line in enumerate(splits):
                    if line == '':
                        break
                    importlines.append(line)
                for importline in importlines:
                    if importline[:4] == 'from': # Check if import line is 'from ___ import ___'
                        regex = r'^from [_a-zA-Z]+ import [_a-zA-Z]+$'
                        if not re.match(regex, importline):
                            self.assertEqual(1, 2) # Raise assertion error
                    else: # Check if import line is 'import ___'
                        regex = r'^import [_a-zA-Z]+$'
                        if not re.match(regex, importline):
                            self.assertEqual(1, 2) # Raise assertion error
                self.assertEqual('', splits[i])
                self.assertEqual('', splits[i + 1])
                self.assertEqual('def ', splits[i + 2][:4])
                self.assertEqual('', splits[i + 3])

    def test_docstrs(self):
        for docstr in self.df['docstr']:
            if docstr != '':
                self.assertEqual(docstr.split('\n')[0], '\'\'\'')
                self.assertEqual(docstr.split('\n')[-2], '\'\'\'')

    def test_combine_and_compile(self):
        for i, row in self.df.iterrows():
            with open('genfile.py', 'w') as out:
                tab = '    '

                out.write(row['docstr'])
                out.write('import unittest\n')
                out.write(row['header'])
                out.write(row['code'])
                out.write('\n\n')

                out.write('class TestClass(unittest.TestCase):\n')
                out.write(row['test'])
                out.write('\n\n')

                out.write('if __name__ == \'__main__\':\n')
                out.write(f'{tab}suite = unittest.TestLoader().loadTestsFromTestCase(TestClass)\n')
                out.write(f'{tab}runner = unittest.TextTestRunner()\n')
                out.write(f'{tab}result = runner.run(suite)\n')
                out.write(f'{tab}if result.wasSuccessful():\n')
                out.write(f'{tab}{tab}print("PASS")\n')

            result = subprocess.run(['python', 'genfile.py'], capture_output=True, text=True)
            self.assertEqual('PASS\n', result.stdout)


if __name__ == '__main__':
    unittest.main()