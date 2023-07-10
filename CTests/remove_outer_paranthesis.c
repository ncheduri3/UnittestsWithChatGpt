#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// Function declaration
char* removeOuterParentheses(char* s);

// Function implementation
char* removeOuterParentheses(char* s) {
    int length = strlen(s);
    char* ans = (char*)malloc((length + 1) * sizeof(char));
    int ansIndex = 0;
    int openedCount = 0;

    for (int i = 0; i < length; i++) {
        if (s[i] == '(') {
            if (openedCount > 0) {
                ans[ansIndex] = '(';
                ansIndex++;
            }
            openedCount++;
        } else if (s[i] == ')') {
            openedCount--;
            if (openedCount > 0) {
                ans[ansIndex] = ')';
                ansIndex++;
            }
        }
    }

    ans[ansIndex] = '\0';
    return ans;
}

// Test cases
void test_single_parentheses() {
    char s[] = "()";
    char* expected = "";

    char* result = removeOuterParentheses(s);

    printf("Test single_parentheses: ");
    if (strcmp(result, expected) == 0) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }

    free(result);
}

void test_nested_parentheses() {
    char s[] = "(()())";
    char* expected = "()()";

    char* result = removeOuterParentheses(s);

    printf("Test nested_parentheses: ");
    if (strcmp(result, expected) == 0) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }

    free(result);
}

void test_multiple_groups() {
    char s[] = "()()(()())";
    char* expected = "()()";

    char* result = removeOuterParentheses(s);

    printf("Test multiple_groups: ");
    if (strcmp(result, expected) == 0) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }

    free(result);
}

void test_no_outer_parentheses() {
    char s[] = "()()()";
    char* expected = "";

    char* result = removeOuterParentheses(s);

    printf("Test no_outer_parentheses: ");
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

    char* result = removeOuterParentheses(s);

    printf("Test empty_string: ");
    if (strcmp(result, expected) == 0) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }

    free(result);
}

int main() {
    test_single_parentheses();
    test_nested_parentheses();
    test_multiple_groups();
    test_no_outer_parentheses();
    test_empty_string();

    return 0;
}
