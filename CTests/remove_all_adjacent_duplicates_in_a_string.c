#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// Function declaration
char* removeDuplicates(char* s);

// Function implementation
char* removeDuplicates(char* s) {
    int length = strlen(s);
    char* ans = (char*)malloc((length + 1) * sizeof(char));
    int index = 0;

    for (int i = 0; i < length; i++) {
        if (index > 0 && ans[index - 1] == s[i]) {
            index--;
        } else {
            ans[index] = s[i];
            index++;
        }
    }

    ans[index] = '\0';
    return ans;
}

// Test cases
void test_no_duplicates() {
    char s[] = "abcd";
    char* expected = "abcd";

    char* result = removeDuplicates(s);

    printf("Test no_duplicates: ");
    if (strcmp(result, expected) == 0) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }

    free(result);
}

void test_duplicates_at_beginning() {
    char s[] = "aabbcccddd";
    char* expected = "cd";

    char* result = removeDuplicates(s);

    printf("Test duplicates_at_beginning: ");
    if (strcmp(result, expected) == 0) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }

    free(result);
}

void test_duplicates_at_end() {
    char s[] = "abcdefghhh";
    char* expected = "abcdefgh";

    char* result = removeDuplicates(s);

    printf("Test duplicates_at_end: ");
    if (strcmp(result, expected) == 0) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }

    free(result);
}

void test_duplicates_in_middle() {
    char s[] = "kaabbccddeel";
    char* expected = "kl";

    char* result = removeDuplicates(s);

    printf("Test duplicates_in_middle: ");
    if (strcmp(result, expected) == 0) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }

    free(result);
}

void test_empty_string() {
    char s[] = "";
    char* expected = "";

    char* result = removeDuplicates(s);

    printf("Test empty_string: ");
    if (strcmp(result, expected) == 0) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }

    free(result);
}

int main() {
    test_no_duplicates();
    test_duplicates_at_beginning();
    test_duplicates_at_end();
    test_duplicates_in_middle();
    test_empty_string();

    return 0;
}
