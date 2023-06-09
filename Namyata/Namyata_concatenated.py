# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
#
# Given the integer n, return the number of complete rows of the staircase you will build.
#
# Constraints:
#
# 1 <= n <= 231 - 1

import unittest
from math import sqrt
from typing import List


def arrangeCoins(n: int) -> int:
    return int(sqrt(2 * n + 0.25) - 0.50)


class TestArrangeCoins(unittest.TestCase):
    def test_5_coins(self):
        n = 5
        expected = 2
        self.assertEqual(arrangeCoins(n), expected)

    def test_8_coins(self):
        n = 8
        expected = 3
        self.assertEqual(arrangeCoins(n), expected)

    def test_10_coins(self):
        n = 10
        expected = 4
        self.assertEqual(arrangeCoins(n), expected)

    def test_0_coins(self):
        n = 0
        expected = 0
        self.assertEqual(arrangeCoins(n), expected)

    def test_large_number_of_coins(self):
        n = 1000000
        # expected = 1414 chat gpt version
        expected = 1413
        self.assertEqual(arrangeCoins(n), expected)

# One test case is wrong. Uncomment to run the correct version.


def findDelayedArrivalTime( arrivalTime: int, delayedTime: int) -> int:
    return (arrivalTime + delayedTime) % 24


class TestFindDelayedArrivalTime(unittest.TestCase):

    def test_find_delayed_arrival_time(self):
    # Replace YourClass with the actual class name

        # Test Case 1
        self.assertEqual(findDelayedArrivalTime(10, 5), 15)

        # Test Case 2
        self.assertEqual(findDelayedArrivalTime(20, 8), 4)

        # Test Case 3
        self.assertEqual(findDelayedArrivalTime(5, 20), 1)

        # Test Case 4
        self.assertEqual(findDelayedArrivalTime(15, 0), 15)

        # Test Case 5
        self.assertEqual(findDelayedArrivalTime(23, 3), 2)

## All test cases given out by chat gpt are fine.

# Question : - You are given a positive integer arrivalTime denoting the arrival time of a train in hours, and another positive integer delayedTime denoting the amount of delay in hours.
#
# Return the time when the train will arrive at the station.
#
# Note that the time in this problem is in 24-hours format.# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
#
# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with;
# and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i,
# and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
#
# Constraints:
#
# 1 <= g.length <= 3 * 104
# 0 <= s.length <= 3 * 104
# 1 <= g[i], s[j] <= 231 - 1


def findContentChildren(g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()

    ind = len(s) - 1
    res = 0

    for i in range(len(g) - 1, -1, -1):
        if ind >= 0 and g[i] <= s[ind]:
            res += 1
            ind -= 1

    return res


class TestFindContentChildren(unittest.TestCase):
    def test_equal_sizes(self):
        g = [1, 2, 3]
        s = [1, 2, 3]
        expected = 3
        self.assertEqual(findContentChildren(g, s), expected)

    def test_more_cookies_than_children(self):
        g = [1, 2, 3]
        s = [1, 2, 3, 4, 5]
        expected = 3
        self.assertEqual(findContentChildren(g, s), expected)

    def test_more_children_than_cookies(self):
        g = [1, 2, 3, 4, 5]
        s = [1, 2, 3]
        expected = 3
        self.assertEqual(findContentChildren(g, s), expected)

    def test_no_cookies(self):
        g = [1, 2, 3]
        s = []
        expected = 0
        self.assertEqual(findContentChildren(g, s), expected)

    def test_no_children(self):
        g = []
        s = [1, 2, 3]
        expected = 0
        self.assertEqual(findContentChildren(g, s), expected)

    def test_empty_lists(self):
        g = []
        s = []
        expected = 0
        self.assertEqual(findContentChildren(g, s), expected)

# All the test cases by ChapGPT passed
# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
#
# Return the average salary of employees excluding the minimum and maximum salary.
# Answers within 10-5 of the actual answer will be accepted


def some_function(salary) -> float:
    salary.sort()
    sum = 0
    for s in salary:
        sum += s
    return (sum - salary[0] - salary[-1]) / (len(salary) - 2)


class TestSomeFunction(unittest.TestCase):

    #corrected test cases
    def test_some_function(self):
          # Replace YourClass with the actual class name

        # Test Case 1
        salary = [1000, 2000, 3000, 4000, 5000]
        self.assertAlmostEqual(some_function(salary), 3000.0)

        # Test Case 2
        salary = [500, 800, 1200, 1500]
        self.assertAlmostEqual(some_function(salary), 1000.0)

        # Test Case 3
        salary = [2500, 3500, 2000, 4500]
        self.assertAlmostEqual(some_function(salary), 3000.0)

        # Test Case 4
        salary = [10000, 15000, 12000, 9000, 18000]
        self.assertAlmostEqual(some_function(salary), 12333.333333333334)

        # Test Case 5
        salary = [5000, 3000, 2000, 4000, 6000, 1000]
        self.assertAlmostEqual(some_function(salary), 3500.0)


# Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary
# representation of n. If there are no two adjacent 1's, return 0.
#
# Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the
# absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.



def binaryGap(n: int) -> int:
    s = f'{n:b}'
    result = 0
    for i in range(len(s)):
        if s[i] == '0':
            continue
        for j in range(i + 1, len(s)):
            if s[j] == '0':
                continue
            result = max(result, j - i)
            break
    return result


class TestBinaryGap(unittest.TestCase):

    def test_binary_gap(self):
        n = 22
        result = binaryGap(n)
        self.assertEqual(result, 2)

    def test_no_binary_gap(self):
        n = 8
        result = binaryGap(n)
        self.assertEqual(result, 0)

    def test_multiple_binary_gaps(self):
        n = 37
        result = binaryGap(n)
        # self.assertEqual(result, 2) # Comment This line and uncomment the next one
        self.assertEqual(result, 3)

    def test_single_bit(self):
        n = 1
        result = binaryGap(n)
        self.assertEqual(result, 0)

    def test_maximum_binary_gap(self):
        n = 5
        result = binaryGap(n)
        # self.assertEqual(result, 1) # Uncomment the next line and comment this one
        self.assertEqual(result, 2)


def containsDuplicate(nums):
    return len(set(nums)) != len(nums)


class ContainsDuplicateTestCase(unittest.TestCase):
    def test_duplicates_present(self):
        nums = [1, 2, 3, 1]
        self.assertTrue(containsDuplicate(nums))

    def test_no_duplicates(self):
        nums = [1, 2, 3, 4]
        self.assertFalse(containsDuplicate(nums))

    def test_empty_array(self):
        nums = []
        self.assertFalse(containsDuplicate(nums))

    def test_single_element_array(self):
        nums = [5]
        self.assertFalse(containsDuplicate(nums))

    def test_duplicates_with_negative_numbers(self):
        nums = [-1, 2, -1, 4]
        self.assertTrue(containsDuplicate(nums))

#All unit tests are correct and passed
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#


def isAnagram(s, t):
    if len(s) != len(t):
        return False
    for idx in set(s):
        if s.count(idx) != t.count(idx):
            return False
    return True


class IsAnagramTestCase(unittest.TestCase):
    def test_anagram_strings(self):
        s = "listen"
        t = "silent"
        self.assertTrue(isAnagram(s, t))

    def test_non_anagram_strings(self):
        s = "hello"
        t = "world"
        self.assertFalse(isAnagram(s, t))

    def test_anagram_with_duplicate_characters(self):
        s = "anagram"
        t = "nagaram"
        self.assertTrue(isAnagram(s, t))

    def test_different_length_strings(self):
        s = "cat"
        t = "cats"
        self.assertFalse(isAnagram(s, t))

    def test_empty_strings(self):
        s = ""
        t = ""
        self.assertTrue(isAnagram(s, t))


#All unit tests are correct and passed# Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.
#
# For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
# If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.
#
# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
# If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.
#
# For example, "m.y+name@email.com" will be forwarded to "my@email.com".
# It is possible to use both of these rules at the same time.
#
# Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.


def numUniqueEmails(emails: List[str]) -> int:
    set_ = set()
    for i in emails:
        final_email = ""
        email = i.split("@")
        email[0] = email[0].replace(".", "")
        if "+" in email[0]:
            index = email[0].index("+")
            email[0] = email[0][:index]
        final_email += email[0] + "@" + email[1]
        set_.add(final_email)
    return len(set_)


class TestNumUniqueEmails(unittest.TestCase):
    def test_empty_list(self):
        emails = []
        expected = 0
        self.assertEqual(numUniqueEmails(emails), expected)

    def test_single_email(self):
        emails = ["test.email@example.com"]
        expected = 1
        self.assertEqual(numUniqueEmails(emails), expected)

    def test_duplicate_emails(self):
        emails = ["test.email@example.com", "test.email@example.com"]
        expected = 1
        self.assertEqual(numUniqueEmails(emails), expected)

    def test_unique_emails(self):
        emails = ["test.email@example.com", "test.email2@example.com", "another.email@example.com"]
        expected = 3
        self.assertEqual(numUniqueEmails(emails), expected)

    def test_emails_with_dots(self):
        emails = ["t.est.email@example.com", "testemail@example.com"]
        expected = 1
        self.assertEqual(numUniqueEmails(emails), expected)

    def test_emails_with_plus(self):
        emails = ["test.email+spam@example.com", "test.email@example.com"]
        expected = 1
        self.assertEqual(numUniqueEmails(emails), expected)

    def test_emails_with_com_suffix(self):
        emails = ["test.email@example.com", "test.email@example.org"]
        expected = 2
        self.assertEqual(numUniqueEmails(emails), expected)

#All unit tests are correct and passed
# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.


def isHappy(n: int) -> bool:
    visited = set()  # set to keep track of visited numbers

    while n != 1:  # continue loop until happy or stuck in cycle
        sum_of_squares = 0

        # compute sum of squares of digits in n
        while n > 0:
            digit = n % 10
            sum_of_squares += digit ** 2
            n //= 10

        # check if sum is already visited
        if sum_of_squares in visited:
            return False

        # add sum to visited set
        visited.add(sum_of_squares)

        # set n to be the sum of squares for the next iteration
        n = sum_of_squares

    return True


class TestIsHappy(unittest.TestCase):
    def test_happy_number(self):
        n = 19
        expected = True
        self.assertEqual(isHappy(n), expected)

    def test_unhappy_number(self):
        n = 20
        expected = False
        self.assertEqual(isHappy(n), expected)

    def test_zero(self):
        n = 0
        expected = False
        self.assertEqual(isHappy(n), expected)

    def test_single_digit_happy_number(self):
        n = 7
        expected = True
        self.assertEqual(isHappy(n), expected)

    def test_single_digit_unhappy_number(self):
        n = 4
        expected = False
        self.assertEqual(isHappy(n), expected)


# All test cases by ChatGPT are correct.# An array is monotonic if it is either monotone increasing or monotone decreasing.
#
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if
# for all i <= j, nums[i] >= nums[j].
#
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.


def isMonotonic(nums: List[int]) -> bool:
    return nums == sorted(nums) or nums == sorted(nums, reverse=True)


class TestIsMonotonic(unittest.TestCase):

    def test_increasing_list(self):
        nums = [1, 2, 3, 4, 5]
        expected = True
        self.assertEqual(isMonotonic(nums), expected)

    def test_decreasing_list(self):
        nums = [5, 4, 3, 2, 1]
        expected = True
        self.assertEqual(isMonotonic(nums), expected)

    def test_monotonic_list(self):
        nums = [1, 3, 5, 7, 9]
        expected = True
        self.assertEqual(isMonotonic(nums), expected)

    def test_non_monotonic_list(self):
        nums = [1, 3, 2, 5, 4]
        expected = False
        self.assertEqual(isMonotonic(nums), expected)

    def test_equal_elements_list(self):
        nums = [5, 5, 5, 5, 5]
        expected = True
        self.assertEqual(isMonotonic(nums), expected)


#All unit tests are correct and passed
# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents
# the coordinate of a point. Check if these points make a straight line in the XY plane.


def checkStraightLine(coordinates):
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]

    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        if (x - x0) * (y1 - y0) != (y - y0) * (x1 - x0):
            return False

    return True


class CheckStraightLineTestCase(unittest.TestCase):
    def test_straight_line(self):
        coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
        self.assertTrue(checkStraightLine(coordinates))

    def test_not_straight_line(self):
        coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 7]]
        self.assertFalse(checkStraightLine(coordinates))

    def test_collinear_points(self):
        coordinates = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
        self.assertTrue(checkStraightLine(coordinates))

    def test_vertical_line(self):
        coordinates = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6]]
        self.assertTrue(checkStraightLine(coordinates))

    def test_horizontal_line(self):
        coordinates = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]]
        self.assertTrue(checkStraightLine(coordinates))



#All unit tests are correct and passed# We define the usage of capitals in a word to be right when one of the following cases holds:
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.


def detectCapitalUse(word: str) -> bool:
    return True if word.islower() or word.istitle() or word.isupper() else False


class TestDetectCapitalUse(unittest.TestCase):
    def test_all_lower_case(self):
        word = "hello"
        expected = True
        self.assertEqual(detectCapitalUse(word), expected)

    def test_all_upper_case(self):
        word = "HELLO"
        expected = True
        self.assertEqual(detectCapitalUse(word), expected)

    def test_title_case(self):
        word = "Title"
        expected = True
        self.assertEqual(detectCapitalUse(word), expected)

    def test_mixed_case(self):
        word = "MiXeD"
        expected = False
        self.assertEqual(detectCapitalUse(word), expected)

    def test_single_letter(self):
        word = "A"
        expected = True
        self.assertEqual(detectCapitalUse(word), expected)

# All test cases by ChatGPT are correct.
# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
# return the number of negative numbers in grid
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100

def countNegatives(grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    negatives = 0
    col = 0
    for row in range(ROWS - 1, -1, -1):
        while col < COLS and grid[row][col] >= 0:
            col += 1
        negatives += COLS - col
    return negatives


class TestCountNegatives(unittest.TestCase):

    def test_no_negatives(self):
        grid = [
            [4, 3, 2],
            [3, 2, 1],
            [2, 1, 0]
        ]
        self.assertEqual(countNegatives(grid), 0)

    def test_all_negatives(self):
        grid = [
            [-1, -2, -3],
            [-4, -5, -6],
            [-7, -8, -9]
        ]
        self.assertEqual(countNegatives(grid), 9)

    def test_mixed_negatives(self):
        grid = [
            [4, 3, -2],
            [3, -5, -6],
            [-7, -8, -9]
        ]
        self.assertEqual(countNegatives(grid), 6)

    def test_large_grid(self):
        grid = [
            [-1, -2, -3, -4, -5],
            [-6, -7, -8, -9, -10],
            [-11, -12, -13, -14, -15]
        ]
        self.assertEqual(countNegatives(grid), 15)

# All unit tests are correct and passed
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of only lowercase English letters.

from collections import Counter
def firstUniqChar(s: str) -> int:
    count = Counter(s)
    for char, freq in count.items():
        if freq == 1:
            return s.index(char)
    return -1


class TestFirstUniqChar(unittest.TestCase):
    def test_no_uniq_char(self):
        s = "ababcc"
        expected = -1
        self.assertEqual(firstUniqChar(s), expected)

    def test_single_uniq_char(self):
        s = "leetcode"
        expected = 0
        self.assertEqual(firstUniqChar(s), expected)

    def test_multiple_uniq_chars(self):
        s = "loveleetcode"
        expected = 2
        self.assertEqual(firstUniqChar(s), expected)

    def test_all_uniq_chars(self):
        s = "abcd"
        expected = 0
        self.assertEqual(firstUniqChar(s), expected)

#All unit tests are correct and passed# You are playing a Flip Game with your friend.
#
# You are given a string currentState that contains only '+' and '-'. You and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move, and therefore the other person will be the winner.
#
# Return all possible states of the string currentState after one valid move. You may return the answer in any order. If there is no valid move, return an empty list [].
# 
# Constraints:
#
# 1 <= currentState.length <= 500
# currentState[i] is either '+' or '-'.


def generatePossibleNextMoves(currentState: str) :
    if not "++" in currentState:
        return []
    splt = [_ for _ in currentState]
    res = []
    i = 0
    while i <= len(currentState) - 2:
        if currentState[i:(i + 2)] == "++":
            tmp = splt.copy()
            tmp[i], tmp[i + 1] = '--'
            res.append(''.join(tmp))
        i += 1
    return res


class TestGeneratePossibleNextMoves(unittest.TestCase):
    def test_no_moves(self):
        currentState = "--"
        expected = []
        self.assertEqual(generatePossibleNextMoves(currentState), expected)

    def test_single_move(self):
        currentState = "++-+"
        # expected = ["--+"]
        expected = ["---+"]
        self.assertEqual(generatePossibleNextMoves(currentState), expected)

    def test_multiple_moves(self):
        currentState = "++++"
        expected = ["--++", "+--+", "++--"]
        self.assertEqual(generatePossibleNextMoves(currentState), expected)

    def test_no_plus_signs(self):
        currentState = "--"
        expected = []
        self.assertEqual(generatePossibleNextMoves(currentState), expected)

# One test case generated by ChapGPT was wrong. uncomment the line to run the correct version.
# Alice and Bob take turns playing a game, with Alice starting first.
#
# Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:
#
# Choosing any x with 0 < x < n and n % x == 0.
# Replacing the number n on the chalkboard with n - x.
# Also, if a player cannot make a move, they lose the game.
#
# Return true if and only if Alice wins the game, assuming both players play optimally.


def divisorGame(n: int) -> bool:
    return n % 2 == 0


class TestDivisorGame(unittest.TestCase):
    def test_even_number(self):
        n = 4
        expected = True
        self.assertEqual(divisorGame(n), expected)

    def test_odd_number(self):
        n = 7
        expected = False
        self.assertEqual(divisorGame(n), expected)

    def test_zero(self):
        n = 0
        expected = True
        self.assertEqual(divisorGame(n), expected)

    def test_large_number(self):
        n = 1000000
        expected = True
        self.assertEqual(divisorGame(n), expected)


# all the test cases are correct.
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you
# have. Each character in stones is a type of stone you have. You want to know how many of the stones you have
# are also jewels.
#
# Letters are case sensitive, so "a" is considered a different type of stone from "A".
#
# Constraints:
#
# 1 <= jewels.length, stones.length <= 50
# jewels and stones consist of only English letters.
# All the characters of jewels are unique.


def numJewelsInStones(jewels: str, stones: str) -> int:
    counter = 0
    for i in stones:
        if i in jewels:
            counter += 1
    return counter


class TestNumJewelsInStones(unittest.TestCase):

    def test_all_jewels_in_stones(self):
        jewels = "abc"
        stones = "aabbbccc"
        result = numJewelsInStones(jewels, stones)
        # self.assertEqual(result, 9) # Comment this and Uncomment the next line
        self.assertEqual(result, 8)

    def test_no_jewels_in_stones(self):
        jewels = "abc"
        stones = "def"
        result = numJewelsInStones(jewels, stones)
        self.assertEqual(result, 0)

    def test_some_jewels_in_stones(self):
        jewels = "abc"
        stones = "aadefbcc"
        result = numJewelsInStones(jewels, stones)
        # self.assertEqual(result, 6) # Comment this and Uncomment the next line
        self.assertEqual(result, 5)

    def test_empty_stones(self):
        jewels = "abc"
        stones = ""
        result = numJewelsInStones(jewels, stones)
        self.assertEqual(result, 0)

    def test_empty_jewels(self):
        jewels = ""
        stones = "abcdef"
        result = numJewelsInStones(jewels, stones)
        self.assertEqual(result, 0)


# Question :
# There is a bag that consists of items, each item has a number 1, 0, or -1 written on it.
#
# You are given four non-negative integers numOnes, numZeros, numNegOnes, and k.
#
# The bag initially contains:
#
# numOnes items with 1s written on them.
# numZeroes items with 0s written on them.
# numNegOnes items with -1s written on them.
# We want to pick exactly k items among the available items. Return the maximum possible sum of numbers written on the
# items.

def kItemsWithMaximumSum( numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
    return min((k, numOnes)) + (min((numNegOnes, k - numOnes - numZeros)) * -1 if (k - numOnes - numZeros) > 0 else 0)


# class TestKItemsWithMaximumSum(unittest.TestCase):
#
#     def test_k_items_with_maximum_sum(self):
#          # Replace YourClass with the actual class name
#
#         # Test Case 1
#         self.assertEqual(kItemsWithMaximumSum(5, 3, 2, 4), 4)
#
#         # Test Case 2
#         self.assertEqual(kItemsWithMaximumSum(2, 4, 1, 3), -1)
#
#         # Test Case 3
#         self.assertEqual(kItemsWithMaximumSum(0, 0, 0, 2), 0)
#
#         # Test Case 4
#         self.assertEqual(kItemsWithMaximumSum(10, 5, 3, 10), 8)
#
#         # Test Case 5
#         self.assertEqual(kItemsWithMaximumSum(3, 2, 1, 6), -2)
#
#
# if __name__ == '__main__':
#     unittest.main()

# Wrong interpretation of the code.

# class CorrectTestKItemsWithMaximumSum(unittest.TestCase):
#
#     def test_k_items_with_maximum_sum(self):
#
#         # Test Case 1
#         self.assertEqual(kItemsWithMaximumSum(5, 3, 2, 4), 4)
#
#         # Test Case 2
#         self.assertEqual(kItemsWithMaximumSum(2, 4, 1, 3), 2)
#
#         # Test Case 3
#         self.assertEqual(kItemsWithMaximumSum(0, 0, 0, 2), 0)
#
#         # Test Case 4
#         self.assertEqual(kItemsWithMaximumSum(10, 5, 3, 10), 10)
#
#         # Test Case 5
#         self.assertEqual(kItemsWithMaximumSum(3, 2, 1, 6), 2)


# def kItemsWithMaximumSum(numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
#     ones_taken = min(k, numOnes)
#     remaining_k = k - ones_taken
#     neg_ones_taken = min(remaining_k, numNegOnes) * -1 if remaining_k > 0 else 0
#
#     return ones_taken + neg_ones_taken

# wrong code generation. Misses the case when number of zeroes are greater than numones - k.


import unittest

class TestKItemsWithMaximumSum(unittest.TestCase):

    def test_k_items_with_maximum_sum_corrected(self):
        # Test Case 1
        numOnes = 5
        numZeros = 3
        numNegOnes = 2
        k = 4
        self.assertEqual(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k), 4)

        # Test Case 2
        numOnes = 2
        numZeros = 4
        numNegOnes = 1
        k = 3
        self.assertEqual(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k), 2) # should have been 0 - missed case!!

        # Test Case 3
        numOnes = 0
        numZeros = 0
        numNegOnes = 0
        k = 2
        self.assertEqual(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k), 0)

        # Test Case 4
        numOnes = 10
        numZeros = 5
        numNegOnes = 3
        k = 10
        self.assertEqual(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k), 10)

        # Test Case 5
        numOnes = 3
        numZeros = 2
        numNegOnes = 1
        k = 6
        self.assertEqual(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k), 2)

    # def test_k_items_with_maximum_sum(self):
    #     # Test Case 1
    #     numOnes = 5
    #     numZeros = 3
    #     numNegOnes = 2
    #     k = 4
    #     self.assertEqual(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k), 3)
    #
    #     # Test Case 2
    #     numOnes = 2
    #     numZeros = 4
    #     numNegOnes = 1
    #     k = 3
    #     self.assertEqual(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k), -1)
    #
    #     # Test Case 3
    #     numOnes = 0
    #     numZeros = 0
    #     numNegOnes = 0
    #     k = 2
    #     self.assertEqual(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k), 0)
    #
    #     # Test Case 4
    #     numOnes = 10
    #     numZeros = 5
    #     numNegOnes = 3
    #     k = 10
    #     self.assertEqual(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k), 8)
    #
    #     # Test Case 5
    #     numOnes = 3
    #     numZeros = 2
    #     numNegOnes = 1
    #     k = 6
    #     self.assertEqual(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k), -2)


# Given an array of points on the X-Y plane points where points[i] = [xi, yi],
# return the area of the largest triangle that can be formed by any three different points.
# Answers within 10-5 of the actual answer will be accepted.
#
# Constraints:
#
# 3 <= points.length <= 50
# -50 <= xi, yi <= 50
# All the given points are unique.

import unittest
from typing import List



def largestTriangleArea( points: List[List[int]]) -> float:
    area = 0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            for k in range(j + 1, n):
                x3, y3 = points[k]
                curr = abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
                if curr > area:
                    area = curr
    return area


class TestLargestTriangleArea(unittest.TestCase):

    def test_valid_triangle_area(self):
        points = [[0, 0], [0, 1], [1, 0]]
        result = largestTriangleArea(points)
        self.assertAlmostEqual(result, 0.5, places=6)

    def test_zero_area(self):
        points = [[0, 0], [0, 0], [0, 0]]
        result = largestTriangleArea(points)
        self.assertAlmostEqual(result, 0, places=6)

    def test_large_triangle_area(self):
        solution = Solution()
        points = [[-50, -50], [0, 0], [50, -50], [0, 25]]
        result = largestTriangleArea(points)
        # self.assertAlmostEqual(result, 1250, places=6) # comment this and uncomment the next line to run
        self.assertAlmostEqual(result, 3750, places=6)

    def test_single_point(self):
        points = [[0, 0]]
        result = largestTriangleArea(points)
        self.assertAlmostEqual(result, 0, places=6)

    def test_minimum_points(self):
        points = [[0, 0], [1, 1], [2, 2]]
        result = largestTriangleArea(points)
        self.assertAlmostEqual(result, 0, places=6)


if __name__ == '__main__':
    unittest.main()
# You are given an array of integers stones where stones[i] is the weight of the ith stone.
#
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
#
# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.
#
# Return the weight of the last remaining stone. If there are no stones left, return 0.
#
# Constraints:
#
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000

import unittest
from typing import List
from bisect import insort_left

def lastStoneWeight(stones: List[int]) -> int:
    stones.sort()

    while stones:
        s1 = stones.pop()

        if not stones:
            return s1

        s2 = stones.pop()

        if s1 > s2:
            insort_left(stones, s1 - s2)

    return 0

class TestLastStoneWeight(unittest.TestCase):
    def test_single_stone(self):
        stones = [5]
        expected = 5
        self.assertEqual(lastStoneWeight(stones), expected)

    def test_two_stones(self):
        stones = [3, 7]
        expected = 4
        self.assertEqual(lastStoneWeight(stones), expected)

    def test_multiple_stones(self):
        stones = [2, 7, 4, 1, 8, 1]
        expected = 1
        self.assertEqual(lastStoneWeight(stones), expected)

    def test_same_weight_stones(self):
        stones = [5, 5, 5, 5]
        expected = 0
        self.assertEqual(lastStoneWeight(stones), expected)

    def test_empty_list(self):
        stones = []
        expected = 0
        self.assertEqual(lastStoneWeight(stones), expected)


# all the test cases passed.


# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".

import unittest

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
# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
#
# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
#
# A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

import unittest

def findLHS(nums) -> int:
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    max_length = 0
    for num in freq:
        if num + 1 in freq:
            max_length = max(max_length, freq[num] + freq[num + 1])
    return max_length

class TestFindLHS(unittest.TestCase):
    def test_example_case(self):
        nums = [1, 3, 2, 2, 5, 2, 3, 7]
        expected = 5
        self.assertEqual(findLHS(nums), expected)

    def test_empty_list(self):
        nums = []
        expected = 0
        self.assertEqual(findLHS(nums), expected)

    def test_single_element(self):
        nums = [5]
        expected = 0
        self.assertEqual(findLHS(nums), expected)

    def test_no_consecutive_elements(self):
        nums = [1, 2, 3, 4, 5]
        # expected = 0
        expected = 2
        self.assertEqual(findLHS(nums), expected)

    def test_negative_numbers(self):
        nums = [-1, -2, -2, -2, -3, -4, -5]
        # expected = 3
        expected = 4
        self.assertEqual(findLHS(nums), expected)

    def test_large_input(self):
        nums = [10**9] * 10**4 + [0] * 10**4
        # expected = 10**4
        expected = 0
        self.assertEqual(findLHS(nums), expected)

if __name__ == '__main__':
    unittest.main()

# 3 test cases by chatGPT had to be corrected. Uncomment the lines to run the correct version.
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



import unittest

def maxProfit(prices):
    left = 0  # Buy
    right = 1  # Sell
    max_profit = 0
    while right < len(prices):
        current_profit = prices[right] - prices[left]  # our current Profit
        if prices[left] < prices[right]:
            max_profit = max(current_profit, max_profit)
        else:
            left = right
        right += 1
    return max_profit

class MaxProfitTestCase(unittest.TestCase):
    def test_profit_possible(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected_output = 5
        self.assertEqual(maxProfit(prices), expected_output)

    def test_no_profit_possible(self):
        prices = [7, 6, 4, 3, 1]
        expected_output = 0
        self.assertEqual(maxProfit(prices), expected_output)

    def test_empty_array(self):
        prices = []
        expected_output = 0
        self.assertEqual(maxProfit(prices), expected_output)

    def test_single_element_array(self):
        prices = [5]
        expected_output = 0
        self.assertEqual(maxProfit(prices), expected_output)

    def test_constant_price(self):
        prices = [3, 3, 3, 3, 3]
        expected_output = 0
        self.assertEqual(maxProfit(prices), expected_output)

if __name__ == '__main__':
    unittest.main()
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
#


import unittest

def merge(nums1, m, nums2, n):
    for i in range(m, m + n):
        nums1[i] = nums2[i - m]
    nums1.sort()

class MergeTestCase(unittest.TestCase):
    def test_merge_lists(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        merge(nums1, m, nums2, n)
        expected_output = [1, 2, 2, 3, 5, 6]
        self.assertEqual(nums1, expected_output)

    def test_empty_list(self):
        nums1 = []
        m = 0
        nums2 = []
        n = 0
        merge(nums1, m, nums2, n)
        expected_output = []
        self.assertEqual(nums1, expected_output)

    def test_merge_into_empty_list(self):
        nums1 = [0, 0, 0]
        m = 0
        nums2 = [1, 2, 3]
        n = 3
        merge(nums1, m, nums2, n)
        expected_output = [1, 2, 3]
        self.assertEqual(nums1, expected_output)

    def test_merge_with_duplicate_elements(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 2, 3]
        n = 3
        merge(nums1, m, nums2, n)
        expected_output = [1, 2, 2, 2, 3, 3]
        self.assertEqual(nums1, expected_output)

    def test_merge_with_negative_numbers(self):
        nums1 = [-1, 0, 0, 0]
        m = 1
        nums2 = [-2, -3, -4]
        n = 3
        merge(nums1, m, nums2, n)
        expected_output = [-4, -3, -2, -1]
        self.assertEqual(nums1, expected_output)

if __name__ == '__main__':
    unittest.main()
#All unit tests are correct and passed# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.

import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    head = ListNode()
    current = head
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 or list2
    return head.next


class MergeTwoListsCorrectedTestCase(unittest.TestCase):
    def test_merge_lists(self):
        # Create the input lists
        # list1: 1 -> 2 -> 4
        list1 = ListNode(1)
        list1.next = ListNode(2)
        list1.next.next = ListNode(4)

        # list2: 1 -> 3 -> 4
        list2 = ListNode(1)
        list2.next = ListNode(3)
        list2.next.next = ListNode(4)

        # Expected merged list: 1 -> 1 -> 2 -> 3 -> 4 -> 4
        expected_output = ListNode(1)
        expected_output.next = ListNode(1)
        expected_output.next.next = ListNode(2)
        expected_output.next.next.next = ListNode(3)
        expected_output.next.next.next.next = ListNode(4)
        expected_output.next.next.next.next.next = ListNode(4)

        finalList = mergeTwoLists(list1, list2)
        fl = []
        while finalList:
            fl.append(finalList.val)
            finalList = finalList.next
        # Call the function and compare the output
        self.assertEqual(fl, [1,1,2,3,4,4])

    def test_empty_lists(self):
        # Empty list1 and list2
        list1 = None
        list2 = None

        # Merged list should be empty as well
        expected_output = None

        self.assertEqual(mergeTwoLists(list1, list2), expected_output)

    def test_one_empty_list(self):
        # list1: 1 -> 2 -> 3
        list1 = ListNode(1)
        list1.next = ListNode(2)
        list1.next.next = ListNode(3)

        # Empty list2
        list2 = None

        # Merged list should be list1 itself
        expected_output = list1

        self.assertEqual(mergeTwoLists(list1, list2), expected_output)

    def test_same_values(self):
        # list1: 1 -> 1 -> 1
        list1 = ListNode(1)
        list1.next = ListNode(1)
        list1.next.next = ListNode(1)

        # list2: 1 -> 1 -> 1
        list2 = ListNode(1)
        list2.next = ListNode(1)
        list2.next.next = ListNode(1)

        # Expected merged list: 1 -> 1 -> 1 -> 1 -> 1 -> 1
        finalList = mergeTwoLists(list1, list2)
        fl = []
        while finalList:
            fl.append(finalList.val)
            finalList = finalList.next
        self.assertEqual(fl, [1,1,1,1,1,1])



#can''t compare the address locations of the nodes
#Added the correct test cases.
# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
#
# A common string is a string that appeared in both list1 and list2.
#
# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
#
# Return all the common strings with the least index sum. Return the answer in any order.




def findRestaurant(list1, list2) :
    d = {}
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                d[list1[i]] = i + j
    lst = []
    for i, j in d.items():
        if j == min(d.values()):
            lst.append(i)
    return lst


class TestFindRestaurant(unittest.TestCase):
    def test_example_case(self):
        list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
        list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
        expected = ["Shogun"]
        self.assertEqual(findRestaurant(list1, list2), expected)

    def test_multiple_common_restaurants(self):
        list1 = ["KFC", "Burger King", "Pizza Hut", "McDonald's"]
        list2 = ["Burger King", "Pizza Hut", "McDonald's", "KFC"]
        # expected = ["Burger King", "Pizza Hut", "McDonald's", "KFC"]
        expected = ["Burger King"]
        self.assertEqual(findRestaurant(list1, list2), expected)

    def test_no_common_restaurant(self):
        list1 = ["Subway", "Starbucks", "Chipotle"]
        list2 = ["McDonald's", "Taco Bell", "Wendy's"]
        expected = []
        self.assertEqual(findRestaurant(list1, list2), expected)

    def test_empty_lists(self):
        list1 = []
        list2 = []
        expected = []
        self.assertEqual(findRestaurant(list1, list2), expected)

    def test_large_input(self):
        list1 = ["Restaurant" + str(i) for i in range(1000)]
        list2 = ["Cafe" + str(i) for i in range(1000)]
        # expected = ["Restaurant0", "Cafe0"]
        expected = []
        self.assertEqual(findRestaurant(list1, list2), expected)


if __name__ == '__main__':
    unittest.main()

# 2 tests failed. Uncomment to run correct versions.
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.

import unittest

def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0 and nums[slow] == 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]

        # wait while we find a non-zero element to swap with you
        if nums[slow] != 0:
            slow += 1


class TestMoveZeroes(unittest.TestCase):
    def test_move_zeroes(self):
        nums = [0, 1, 0, 3, 12]
        expected = [1, 3, 12, 0, 0]
        moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_no_zeroes(self):
        nums = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_all_zeroes(self):
        nums = [0, 0, 0, 0, 0]
        expected = [0, 0, 0, 0, 0]
        moveZeroes(nums)
        self.assertEqual(nums, expected)

    def test_mixed_elements(self):
        nums = [0, 2, 0, 1, 0, 3, 0, 0, 12]
        expected = [2, 1, 3, 12, 0, 0, 0, 0, 0]
        moveZeroes(nums)
        self.assertEqual(nums, expected)

if __name__ == '__main__':
    unittest.main()

# All test cases by ChatGPT are correct.
# Given two strings first and second, consider occurrences in some text of the form "first second third",
# where second comes immediately after first, and third comes immediately after second.
#
# Return an array of all the words third for each occurrence of "first second third".

import unittest
from typing import List

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


#Test cases ensured coverage but were wrong. Added the correct test cases.
# Given an integer x, return true if x is a
# palindrome
# , and false otherwise.

import unittest

def isPalindrome(x):
    if x < 0:
        return False

    inputNum = x
    newNum = 0
    while x > 0:
        newNum = newNum * 10 + x % 10
        x = x // 10
    return newNum == inputNum

class IsPalindromeTestCase(unittest.TestCase):
    def test_palindrome_number(self):
        x = 121
        self.assertTrue(isPalindrome(x))

    def test_non_palindrome_number(self):
        x = 123
        self.assertFalse(isPalindrome(x))

    def test_negative_number(self):
        x = -121
        self.assertFalse(isPalindrome(x))

    def test_single_digit_number(self):
        x = 5
        self.assertTrue(isPalindrome(x))

    def test_zero(self):
        x = 0
        self.assertTrue(isPalindrome(x))

if __name__ == '__main__':
    unittest.main()

#All unit tests are correct and passed
import unittest

def check_is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class TestCheckIsPrime(unittest.TestCase):
    def test_prime_numbers(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for prime in primes:
            self.assertTrue(check_is_prime(prime), f"{prime} should be prime")

    def test_non_prime_numbers(self):
        non_primes = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
        for non_prime in non_primes:
            self.assertFalse(check_is_prime(non_prime), f"{non_prime} should not be prime")

    def test_negative_number(self):
        negative_number = -7
        self.assertFalse(check_is_prime(negative_number), f"{negative_number} should not be prime")

    def test_zero(self):
        zero = 0
        self.assertFalse(check_is_prime(zero), f"{zero} should not be prime")

    def test_one(self):
        one = 1
        self.assertFalse(check_is_prime(one), f"{one} should not be prime")

if __name__ == '__main__':
    unittest.main()
# Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.
#
# Recall that the number of set bits an integer has is the number of 1's present when written in binary.
#
# For example, 21 written in binary is 10101, which has 3 set bits.

import unittest

def countPrimeSetBits(left: int, right: int) -> int:
    count = 0
    for i in range(left, right + 1):
        print(i, ":", bin(i))
        c = 0
        n = bin(i).count("1")
        for j in range(1, n + 1):
            if n % j == 0:
                c += 1
        if c == 2:
            count += 1
    return count

class TestCountPrimeSetBitsCorrected(unittest.TestCase):
    def test_left_equal_to_right(self):
        left = 10
        right = 10
        expected = 1
        self.assertEqual(countPrimeSetBits(left, right), expected)

    def test_no_prime_set_bits(self):
        left = 1
        right = 10
        expected = 6
        self.assertEqual(countPrimeSetBits(left, right), expected)

    def test_all_prime_set_bits(self):
        left = 10
        right = 15
        expected = 5
        self.assertEqual(countPrimeSetBits(left, right), expected)

    def test_mixed_prime_set_bits(self):
        left = 3
        right = 7
        expected = 4
        self.assertEqual(countPrimeSetBits(left, right), expected)

    def test_large_range(self):
        left = 1000
        right = 1010
        expected = 5
        self.assertEqual(countPrimeSetBits(left, right), expected)



#Wrong expected outputs by chat gpt. Corrected the test cases

# An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.
#
# Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.
#
# Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.
#
# rec1.length == 4
# rec2.length == 4
# -109 <= rec1[i], rec2[i] <= 109
# rec1 and rec2 represent a valid rectangle with a non-zero area.



def isRectangleOverlap(rec1: List[int], rec2: List[int]) -> bool:
    def overlap(a1, a2, b1, b2):
        if a1 > b1:
            a1, a2, b1, b2 = b1, b2, a1, a2

        if a2 <= b1:
            return False
        else:
            return True

    ax1, ay1, ax2, ay2 = rec1[0], rec1[1], rec1[2], rec1[3]
    bx1, by1, bx2, by2 = rec2[0], rec2[1], rec2[2], rec2[3]
    if not overlap(ax1, ax2, bx1, bx2) or not overlap(ay1, ay2, by1, by2):
        return False
    else:
        return True

class TestIsRectangleOverlap(unittest.TestCase):

    def test_overlap(self):
        rec1 = [0, 0, 2, 2]
        rec2 = [1, 1, 3, 3]
        result = isRectangleOverlap(rec1, rec2)
        self.assertTrue(result)

    def test_no_overlap(self):
        rec1 = [0, 0, 1, 1]
        rec2 = [2, 2, 3, 3]
        result = isRectangleOverlap(rec1, rec2)
        self.assertFalse(result)

    def test_partial_overlap(self):
        rec1 = [0, 0, 2, 2]
        rec2 = [1, 1, 2, 3]
        result = isRectangleOverlap(rec1, rec2)
        self.assertTrue(result)

    def test_same_rectangle(self):
        rec1 = [0, 0, 2, 2]
        rec2 = [0, 0, 2, 2]
        result = isRectangleOverlap(rec1, rec2)
        self.assertTrue(result)

    def test_single_point_overlap(self):
        rec1 = [0, 0, 1, 1]
        rec2 = [1, 1, 2, 2]
        result = isRectangleOverlap(rec1, rec2)
        self.assertFalse(result)

    def test_minimum_area_rectangle(self):
        rec1 = [0, 0, 0, 0]
        rec2 = [0, 0, 0, 0]
        result = isRectangleOverlap(rec1, rec2)
        self.assertFalse(result)


# All test cases worked.import unittest

def removeDuplicatesString(s: str) -> str:
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
        self.assertEqual(removeDuplicatesString(s), expected)

    def test_duplicates_at_beginning(self):
        s = "aabbcccddd"
        expected = "cd"
        self.assertEqual(removeDuplicatesString(s), expected)

    def test_duplicates_at_end(self):
        s = "abcdefghhh"
        expected = "abcdefgh"
        self.assertEqual(removeDuplicatesString(s), expected)

    def test_duplicates_in_middle(self):
        s = "kaabbccddeel"
        expected = "kl"
        self.assertEqual(removeDuplicatesString(s), expected)

    def test_empty_string(self):
        s = ""
        expected = ""
        self.assertEqual(removeDuplicatesString(s), expected)





#Few test cases by chatGPT are wrong. Corrected them.

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
#
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
#
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.


import unittest

def removeDuplicates(nums):
    j = 0
    for i in range(1, len(nums)):
        if nums[j] != nums[i]:
            j += 1
            nums[j] = nums[i]
    return j + 1

class RemoveDuplicatesTestCase(unittest.TestCase):
    def test_no_duplicates(self):
        nums = [1, 2, 3, 4, 5]
        expected_output = 5
        self.assertEqual(removeDuplicates(nums), expected_output)
        self.assertEqual(nums[:expected_output], [1, 2, 3, 4, 5])

    def test_duplicates_present(self):
        nums = [1, 1, 2, 2, 3]
        expected_output = 3
        self.assertEqual(removeDuplicates(nums), expected_output)
        self.assertEqual(nums[:expected_output], [1, 2, 3])

    def test_single_element_list(self):
        nums = [5]
        expected_output = 1
        self.assertEqual(removeDuplicates(nums), expected_output)
        self.assertEqual(nums[:expected_output], [5])

    def test_all_duplicates(self):
        nums = [2, 2, 2, 2, 2]
        expected_output = 1
        self.assertEqual(removeDuplicates(nums), expected_output)
        self.assertEqual(nums[:expected_output], [2])

if __name__ == '__main__':
    unittest.main()

#All unit tests are correct and passedimport unittest

def removeElement(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)

class RemoveElementTestCase(unittest.TestCase):
    def test_remove_element(self):
        nums = [3, 2, 2, 3]
        val = 3
        expected_output = 2
        self.assertEqual(removeElement(nums, val), expected_output)
        self.assertEqual(nums, [2, 2])

    def test_remove_all_elements(self):
        nums = [1, 1, 1, 1]
        val = 1
        expected_output = 0
        self.assertEqual(removeElement(nums, val), expected_output)
        self.assertEqual(nums, [])

    def test_remove_no_elements(self):
        nums = [4, 5, 6]
        val = 1
        expected_output = 3
        self.assertEqual(removeElement(nums, val), expected_output)
        self.assertEqual(nums, [4, 5, 6])


    def test_remove_duplicate_elements(self):
        nums = [2, 2, 3, 3, 4]
        val = 3
        expected_output = 3
        self.assertEqual(removeElement(nums, val), expected_output)
        self.assertEqual(nums, [2, 2, 4])

if __name__ == '__main__':
    unittest.main()

#All unit tests are correct and passed
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


import unittest

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

import unittest

def reverseVowels(s: str) -> str:
    q = []
    vowels = ['a', 'i', 'e', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for char in s:
        if char in vowels:
            q.append(char)
            s = s.replace(char, '*', 1)
    q.reverse()
    k = 0
    for char in s:
        if char == '*':
            s = s.replace("*", q[k], 1)
            k += 1
    return s

class TestReverseVowels(unittest.TestCase):
    def test_no_vowels(self):
        s = "xyz"
        expected = "xyz"
        self.assertEqual(reverseVowels(s), expected)

    def test_single_vowel(self):
        s = "hello"
        expected = "holle"
        self.assertEqual(reverseVowels(s), expected)

    def test_multiple_vowels(self):
        s = "leetcode"
        expected = "leotcede"
        self.assertEqual(reverseVowels(s), expected)

    def test_same_vowel(self):
        s = "aaeeii"
        expected = "iiEEaa"
        expected = "iieeaa"
        self.assertEqual(reverseVowels(s), expected)

if __name__ == '__main__':
    unittest.main()

# 1 test case by chatgpt are not correct. Uncomment the line to run the correct version
#
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

import unittest

def romanToInt(s):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0
    for i in range(len(s) - 1):
        if roman[s[i]] < roman[s[i + 1]]:
            number -= roman[s[i]]
        else:
            number += roman[s[i]]
    return number + roman[s[-1]]

class RomanToIntTestCase(unittest.TestCase):
    def test_single_roman_symbol(self):
        s = "X"
        expected_output = 10
        self.assertEqual(romanToInt(s), expected_output)

    def test_roman_symbols_in_ascending_order(self):
        s = "VII"
        expected_output = 7
        self.assertEqual(romanToInt(s), expected_output)

    def test_roman_symbols_in_descending_order(self):
        s = "IX"
        expected_output = 9
        self.assertEqual(romanToInt(s), expected_output)

    def test_roman_symbols_mixed_order(self):
        s = "MCMXCIV"
        expected_output = 1994
        self.assertEqual(romanToInt(s), expected_output)


if __name__ == '__main__':
    unittest.main()

#All unit tests are correct and passed
# A self-dividing number is a number that is divisible by every digit it contains.
#
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.
#
# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].
#
# 1 <= left <= right <= 104

import unittest
from typing import List


def selfDividingNumbers(left: int, right: int) -> List[int]:
    list1 = []

    def selfdiv(num):
        current = 0
        x = num
        while num > 0:
            current = num % 10
            if current == 0:
                return False
            if x % current != 0:
                return False
            num = num // 10
        return True

    for i in range(left, right + 1):
        if selfdiv(i):
            list1.append(i)
    return list1


class TestSelfDividingNumbers(unittest.TestCase):

    def test_valid_range(self):
        result = selfDividingNumbers(1, 100)
        self.assertListEqual(result,
                             [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22, 24, 33, 36, 44, 48, 55, 66, 77, 88, 99])

    def test_empty_range(self):
        result = selfDividingNumbers(10, 9)
        self.assertListEqual(result, [])

    def test_single_number(self):
        result = selfDividingNumbers(22, 22)
        self.assertListEqual(result, [22])

    def test_no_self_dividing_numbers(self):
        result = selfDividingNumbers(30, 35)
        # self.assertListEqual(result, []) # comment this and uncomment the next line
        self.assertListEqual(result, [33])

    def test_all_self_dividing_numbers(self):
        result = selfDividingNumbers(1, 100)
        self.assertListEqual(result,
                             [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22, 24, 33, 36, 44, 48, 55, 66, 77, 88, 99])


if __name__ == '__main__':
    unittest.main()

# One test failed. Uncomment the line to run the correct version

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


# All tests were correct. # Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

import unittest
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a = [i * i for i in nums]
        return sorted(a)

class TestSortedSquares(unittest.TestCase):

    def test_sorted_squares(self):
        solution = Solution()
        nums = [-4, -1, 0, 3, 10]
        result = solution.sortedSquares(nums)
        self.assertEqual(result, [0, 1, 9, 16, 100])

    def test_sorted_squares_negative_numbers(self):
        solution = Solution()
        nums = [-7, -3, -2, 0, 5]
        result = solution.sortedSquares(nums)
        self.assertEqual(result, [0, 4, 9, 25, 49])

    def test_sorted_squares_positive_numbers(self):
        solution = Solution()
        nums = [1, 2, 3, 4, 5]
        result = solution.sortedSquares(nums)
        self.assertEqual(result, [1, 4, 9, 16, 25])

    def test_sorted_squares_zero(self):
        solution = Solution()
        nums = [0]
        result = solution.sortedSquares(nums)
        self.assertEqual(result, [0])

    def test_sorted_squares_empty_list(self):
        solution = Solution()
        nums = []
        result = solution.sortedSquares(nums)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()

# All test cases worked!import unittest


def sumOfMultiples( n: int) -> int:
    ans = 0
    for x in range(1, n + 1):
        if x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
            ans += x

    return ans

#Generated by Chat GPT

# class TestSumOfMultiples(unittest.TestCase):

#     def test_sum_of_multiples(self):
#         # Replace YourClass with the actual class name
#
#         # Test Case 1
#         self.assertEqual(sumOfMultiples(10), 33)
#
#         # Test Case 2
#         self.assertEqual(sumOfMultiples(20), 98)
#
#         # Test Case 3
#         self.assertEqual(sumOfMultiples(5), 8)
#
#         # Test Case 4
#         self.assertEqual(sumOfMultiples(15), 45)
#
#         # Test Case 5
#         self.assertEqual(sumOfMultiples(1), 0)
#
#
# if __name__ == '__main__':
#     unittest.main()


##Remarks
# Didn't understand that the code was to give out mutliples of 3, 5, or 7 from [1, n] with n inclusive. ' \
# It gave out test cases with n excluded. Also it was just random


class CorrectTestSumOfMultiples(unittest.TestCase):

    def test_sum_of_multiples(self):
        # Replace YourClass with the actual class name

        # Test Case 1
        self.assertEqual(sumOfMultiples(10), 40)

        # Test Case 2
        self.assertEqual(sumOfMultiples(20), 119)

        # Test Case 3
        self.assertEqual(sumOfMultiples(5), 8)

        # Test Case 4
        self.assertEqual(sumOfMultiples(15), 81)

        # Test Case 5
        self.assertEqual(sumOfMultiples(1), 0)


if __name__ == '__main__':
    unittest.main()
# You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each value v = grid[i][j] represents a tower of v cubes placed on top of cell (i, j).
#
# After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.
#
# Return the total surface area of the resulting shapes.
#
# Note: The bottom face of each shape counts toward its surface area.



import unittest
from typing import List

def surfaceArea(grid: List[List[int]]) -> int:
    l = len(grid)
    area = 0
    for row in range(l):
        for col in range(l):
            if grid[row][col]:
                area += (grid[row][col] * 4) + 2  # surface area of each block if blocks weren't connected
            if row:  # row > 0
                area -= min(grid[row][col], grid[row - 1][col]) * 2  # subtracting as area is common among two blocks
            if col:  # col > 0
                area -= min(grid[row][col], grid[row][col - 1]) * 2  # subtracting as area is common among two blocks
    return area
class TestSurfaceArea(unittest.TestCase):
    def test_empty_grid(self):
        grid = []
        expected = 0
        self.assertEqual(surfaceArea(grid), expected)

    def test_single_block(self):
        grid = [[1]]
        expected = 6
        self.assertEqual(surfaceArea(grid), expected)

    def test_multiple_blocks(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = 102
        self.assertEqual(surfaceArea(grid), expected)

    def test_zero_blocks(self):
        grid = [[0, 0], [0, 0]]
        expected = 0
        self.assertEqual(surfaceArea(grid), expected)

    def test_large_grid(self):
        grid = [[3, 2, 1, 0, 4], [2, 5, 6, 7, 3], [1, 0, 3, 4, 2], [2, 1, 0, 3, 2], [4, 3, 2, 1, 0]]
        expected = 164
        self.assertEqual(surfaceArea(grid), expected)



#A few test cases were wrong.
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

import unittest

def twoSum(nums, target):
    d = {}
    for i, j in enumerate(nums):
        r = target - j
        if r in d:
            return [d[r], i]
        d[j] = i

class TwoSumTestCase(unittest.TestCase):
    def test_target_present(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected_output = [0, 1]
        self.assertEqual(twoSum(nums, target), expected_output)

    def test_target_not_present(self):
        nums = [3, 6, 8, 12]
        target = 5
        expected_output = None
        self.assertEqual(twoSum(nums, target), expected_output)

    def test_duplicate_values(self):
        nums = [2, 7, 11, 15, 7]
        target = 14
        expected_output = [1, 4]
        self.assertEqual(twoSum(nums, target), expected_output)

    def test_negative_numbers(self):
        nums = [-2, -7, 11, 15]
        target = 9
        expected_output = [0, 2]
        self.assertEqual(twoSum(nums, target), expected_output)

    def test_empty_array(self):
        nums = []
        target = 9
        expected_output = None
        self.assertEqual(twoSum(nums, target), expected_output)

    def test_single_element_array(self):
        nums = [5]
        target = 5
        expected_output = None
        self.assertEqual(twoSum(nums, target), expected_output)

if __name__ == '__main__':
    unittest.main()


#All unit tests are correct and passed

# Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.
#
# A boomerang is a set of three points that are all distinct and not in a straight line.
#
# Constraints:
#
# points.length == 3
# points[i].length == 2
# 0 <= xi, yi <= 100

import unittest
from typing import List

def isBoomerang(points: List[List[int]]) -> bool:
    a, b, c = points
    return (b[1] - a[1]) * (c[0] - b[0]) != (c[1] - b[1]) * (b[0] - a[0])

class TestIsBoomerang(unittest.TestCase):
    def test_valid_boomerang(self):
        points = [[1, 1], [2, 3], [3, 2]]
        expected = True
        self.assertEqual(isBoomerang(points), expected)

    def test_invalid_boomerang(self):
        points = [[1, 1], [2, 2], [3, 3]]
        expected = False
        self.assertEqual(isBoomerang(points), expected)

    def test_horizontal_line(self):
        points = [[1, 1], [2, 1], [3, 1]]
        expected = False
        self.assertEqual(isBoomerang(points), expected)

    def test_vertical_line(self):
        points = [[1, 1], [1, 2], [1, 3]]
        expected = False
        self.assertEqual(isBoomerang(points), expected)

    def test_same_points(self):
        points = [[1, 1], [1, 1], [1, 1]]
        expected = False
        self.assertEqual(isBoomerang(points), expected)

if __name__ == '__main__':
    unittest.main()
# all unit tests passedimport unittest

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
        # abbr = "i12al"
        abbr = "i10al"
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


import unittest

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


import unittest
from typing import List

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
