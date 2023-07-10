#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>

bool validWordAbbreviation(char* word, char* abbr);

bool validWordAbbreviation(char* word, char* abbr) {
    int p1 = 0, p2 = 0;
    int wordLen = strlen(word);
    int abbrLen = strlen(abbr);
    
    while (p1 < wordLen && p2 < abbrLen) {
        if (isdigit(abbr[p2])) {
            if (abbr[p2] == '0') {
                return false; // leading zeros are invalid
            }
            int shift = 0;
            while (p2 < abbrLen && isdigit(abbr[p2])) {
                shift = (shift * 10) + (abbr[p2] - '0');
                p2++;
            }
            p1 += shift;
        } else {
            if (word[p1] != abbr[p2]) {
                return false;
            }
            p1++;
            p2++;
        }
    }
    
    return p1 == wordLen && p2 == abbrLen;
}

// Test case 1
void test_valid_abbreviation() {
    char word[] = "international";
    char abbr[] = "i10al";
    bool result = validWordAbbreviation(word, abbr);
    assert(result);
    printf("Test Case 1 Passed\n");
}

// Test case 2
void test_invalid_abbreviation() {
    char word[] = "apple";
    char abbr[] = "a4e";
    bool result = validWordAbbreviation(word, abbr);
    assert(!result);
    printf("Test Case 2 Passed\n");
}

// Test case 3
void test_leading_zeros() {
    char word[] = "algorithm";
    char abbr[] = "0l9m";
    bool result = validWordAbbreviation(word, abbr);
    assert(!result);
    printf("Test Case 3 Passed\n");
}

// Test case 4
void test_same_length_word_and_abbr() {
    char word[] = "python";
    char abbr[] = "p6n";
    bool result = validWordAbbreviation(word, abbr);
    assert(!result);
    printf("Test Case 4 Passed\n");
}

int main() {
    test_valid_abbreviation();
    test_invalid_abbreviation();
    test_leading_zeros();
    test_same_length_word_and_abbr();

    return 0;
}
