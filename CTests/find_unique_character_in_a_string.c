#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <assert.h>

int firstUniqChar(const char* s) {
    int count[26] = {0};

    // Count the frequency of each character
    for (int i = 0; s[i] != '\0'; i++) {
        count[s[i] - 'a']++;
    }

    // Find the first non-repeating character
    for (int i = 0; s[i] != '\0'; i++) {
        if (count[s[i] - 'a'] == 1) {
            return i;
        }
    }

    return -1;
}

void test_no_uniq_char() {
    const char* s = "ababcc";
    int result = firstUniqChar(s);
    int expected = -1;
    assert(result == expected);
    printf("Test case 'no_uniq_char' passed\n");
}

void test_single_uniq_char() {
    const char* s = "leetcode";
    int result = firstUniqChar(s);
    int expected = 0;
    assert(result == expected);
    printf("Test case 'single_uniq_char' passed\n");
}

void test_multiple_uniq_chars() {
    const char* s = "loveleetcode";
    int result = firstUniqChar(s);
    int expected = 2;
    assert(result == expected);
    printf("Test case 'multiple_uniq_chars' passed\n");
}

void test_all_uniq_chars() {
    const char* s = "abcd";
    int result = firstUniqChar(s);
    int expected = 0;
    assert(result == expected);
    printf("Test case 'all_uniq_chars' passed\n");
}

int main() {
    test_no_uniq_char();
    test_single_uniq_char();
    test_multiple_uniq_chars();
    test_all_uniq_chars();

    return 0;
}
