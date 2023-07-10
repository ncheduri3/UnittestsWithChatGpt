#include <stdio.h>
#include <stdbool.h>
#include <assert.h>
#include <ctype.h>
#include <string.h>

bool detectCapitalUse(const char* word) {
    int len = strlen(word);
    bool allLower = true;
    bool allUpper = true;
    bool firstUpper = true;

    for (int i = 0; i < len; i++) {
        if (islower(word[i])) {
            allUpper = false;
            // firstUpper = false;
        } else if (isupper(word[i])) {
            allLower = false;
            if (i > 0) {
                firstUpper = false;
            }
        } else {
            return false;
        }
    }

    return allLower || allUpper || firstUpper;
}

void test_all_lower_case() {
    const char* word = "hello";
    bool result = detectCapitalUse(word);
    bool expected = true;
    assert(result == expected);
    printf("Test case 'all_lower_case' passed\n");
}

void test_all_upper_case() {
    const char* word = "HELLO";
    bool result = detectCapitalUse(word);
    bool expected = true;
    assert(result == expected);
    printf("Test case 'all_upper_case' passed\n");
}

void test_title_case() {
    const char* word = "Title";
    bool result = detectCapitalUse(word);
    bool expected = true;
    assert(result == expected);
    printf("Test case 'title_case' passed\n");
}

void test_mixed_case() {
    const char* word = "MiXeD";
    bool result = detectCapitalUse(word);
    bool expected = false;
    assert(result == expected);
    printf("Test case 'mixed_case' passed\n");
}

void test_single_letter() {
    const char* word = "A";
    bool result = detectCapitalUse(word);
    bool expected = true;
    assert(result == expected);
    printf("Test case 'single_letter' passed\n");
}

int main() {
    test_all_lower_case();
    test_all_upper_case();
    test_title_case();
    test_mixed_case();
    test_single_letter();

    return 0;
}
