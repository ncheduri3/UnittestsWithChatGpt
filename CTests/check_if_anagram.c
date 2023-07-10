#include <stdio.h>
#include <stdbool.h>
#include <assert.h>
#include <string.h>

bool isAnagram(const char* s, const char* t) {
    int s_length = strlen(s);
    int t_length = strlen(t);

    if (s_length != t_length) {
        return false;
    }

    int s_count[26] = {0};
    int t_count[26] = {0};

    for (int i = 0; i < s_length; i++) {
        s_count[s[i] - 'a']++;
        t_count[t[i] - 'a']++;
    }

    for (int i = 0; i < 26; i++) {
        if (s_count[i] != t_count[i]) {
            return false;
        }
    }

    return true;
}

void test_anagram_strings() {
    const char* s = "listen";
    const char* t = "silent";
    bool result = isAnagram(s, t);
    assert(result == true);
    printf("Test case 'anagram_strings' passed\n");
}

void test_non_anagram_strings() {
    const char* s = "hello";
    const char* t = "world";
    bool result = isAnagram(s, t);
    assert(result == false);
    printf("Test case 'non_anagram_strings' passed\n");
}

void test_anagram_with_duplicate_characters() {
    const char* s = "anagram";
    const char* t = "nagaram";
    bool result = isAnagram(s, t);
    assert(result == true);
    printf("Test case 'anagram_with_duplicate_characters' passed\n");
}

void test_different_length_strings() {
    const char* s = "cat";
    const char* t = "cats";
    bool result = isAnagram(s, t);
    assert(result == false);
    printf("Test case 'different_length_strings' passed\n");
}

void test_empty_strings() {
    const char* s = "";
    const char* t = "";
    bool result = isAnagram(s, t);
    assert(result == true);
    printf("Test case 'empty_strings' passed\n");
}

int main() {
    test_anagram_strings();
    test_non_anagram_strings();
    test_anagram_with_duplicate_characters();
    test_different_length_strings();
    test_empty_strings();

    return 0;
}
