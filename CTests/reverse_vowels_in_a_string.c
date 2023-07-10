#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// Function declaration
char* reverseVowels(char* s);

// Function implementation
char* reverseVowels(char* s) {
    int length = strlen(s);
    char* result = (char*)malloc((length + 1) * sizeof(char));
    strcpy(result, s);
    
    char* vowels = "aieouAIEOU";
    int left = 0;
    int right = length - 1;

    while (left < right) {
        while (left < right && !strchr(vowels, result[left])) {
            left++;
        }
        while (left < right && !strchr(vowels, result[right])) {
            right--;
        }
        
        if (left < right) {
            char temp = result[left];
            result[left] = result[right];
            result[right] = temp;
            left++;
            right--;
        }
    }
    
    return result;
}

// Test cases
void test_no_vowels() {
    char s[] = "xyz";
    char expected[] = "xyz";

    char* result = reverseVowels(s);

    printf("Test no_vowels: ");
    if (strcmp(result, expected) == 0) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }

    free(result);
}

void test_single_vowel() {
    char s[] = "hello";
    char expected[] = "holle";

    char* result = reverseVowels(s);

    printf("Test single_vowel: ");
    if (strcmp(result, expected) == 0) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }

    free(result);
}

void test_multiple_vowels() {
    char s[] = "leetcode";
    char expected[] = "leotcede";

    char* result = reverseVowels(s);

    printf("Test multiple_vowels: ");
    if (strcmp(result, expected) == 0) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }

    free(result);
}

void test_same_vowel() {
    char s[] = "aaeeii";
    char expected[] = "iieeaa";

    char* result = reverseVowels(s);

    printf("Test same_vowel: ");
    if (strcmp(result, expected) == 0) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }

    free(result);
}

int main() {
    test_no_vowels();
    test_single_vowel();
    test_multiple_vowels();
    test_same_vowel();

    return 0;
}
