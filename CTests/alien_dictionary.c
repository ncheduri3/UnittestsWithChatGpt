#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>

bool isAlienSorted(char** words, int wordsSize, char* order);

bool isAlienSorted(char** words, int wordsSize, char* order) {
    int orderCounter[26] = {0};
    for (int i = 0; i < 26; i++) {
        orderCounter[order[i] - 'a'] = i;
    }

    for (int i = 0; i < wordsSize - 1; i++) {
        char* word1 = words[i];
        char* word2 = words[i + 1];
        int j = 0;

        while (word1[j] != '\0' && word2[j] != '\0' && word1[j] == word2[j]) {
            j++;
        }

        if (word1[j] != '\0' && word2[j] != '\0') {
            if (orderCounter[word2[j] - 'a'] < orderCounter[word1[j] - 'a']) {
                return false;
            }
        } else if (word1[j] != '\0' && word2[j] == '\0') {
            return false;
        }
    }

    return true;
}

// Test case 1
void test_empty_words() {
    char* words[] = {};
    int wordsSize = 0;
    char order[] = "abcdefghijklmnopqrstuvwxyz";
    bool result = isAlienSorted(words, wordsSize, order);
    assert(result);
    printf("Test Case 1 Passed\n");
}

// Test case 2
void test_single_word() {
    char* words[] = {"apple"};
    int wordsSize = 1;
    char order[] = "abcdefghijklmnopqrstuvwxyz";
    bool result = isAlienSorted(words, wordsSize, order);
    assert(result);
    printf("Test Case 2 Passed\n");
}

// Test case 3
void test_sorted_words() {
    char* words[] = {"hello", "leetcode", "world"};
    int wordsSize = 3;
    char order[] = "hlabcdefgijkmnopqrstuvwxyz";
    bool result = isAlienSorted(words, wordsSize, order);
    assert(result);
    printf("Test Case 3 Passed\n");
}

// Test case 4
void test_unsorted_words() {
    char* words[] = {"word", "world", "hello"};
    int wordsSize = 3;
    char order[] = "hlabcdefgijkmnopqrstuvwxyz";
    bool result = isAlienSorted(words, wordsSize, order);
    assert(!result);
    printf("Test Case 4 Passed\n");
}

// Test case 5
void test_same_starting_letters() {
    char* words[] = {"apple", "ape", "application"};
    int wordsSize = 3;
    char order[] = "abcdefghijklmnopqrstuvwxyz";
    bool result = isAlienSorted(words, wordsSize, order);
    assert(!result);
    printf("Test Case 5 Passed\n");
}

// Test case 6
void test_same_words() {
    char* words[] = {"same", "same", "same"};
    int wordsSize = 3;
    char order[] = "abcdefghijklmnopqrstuvwxyz";
    bool result = isAlienSorted(words, wordsSize, order);
    assert(result);
    printf("Test Case 6 Passed\n");
}

// Test case 7
void test_custom_order() {
    char* words[] = {"word", "leetcode", "hello"};
    int wordsSize = 3;
    char order[] = "olhecdtbwjsykarxvznipgufmq";
    bool result = isAlienSorted(words, wordsSize, order);
    assert(!result);
    printf("Test Case 7 Passed\n");
}

int main() {
    test_empty_words();
    test_single_word();
    test_sorted_words();
    test_unsorted_words();
    test_same_starting_letters();
    test_same_words();
    test_custom_order();

    return 0;
}
