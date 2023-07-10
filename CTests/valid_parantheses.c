#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>

bool isValid(char* s);

// Function to check if the input string is valid
bool isValid(char* s) {
    int len = strlen(s);
    char stack[len];
    int top = -1;

    for (int i = 0; i < len; i++) {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
            stack[++top] = s[i];
        } else {
            if (top == -1) {
                return false;
            }

            if ((s[i] == ')' && stack[top] == '(') ||
                (s[i] == '}' && stack[top] == '{') ||
                (s[i] == ']' && stack[top] == '[')) {
                top--;
            } else {
                return false;
            }
        }
    }

    return top == -1;
}

// Test case 1
void test_is_valid_1() {
    char* s = "()";
    bool result = isValid(s);
    assert(result);
    printf("Test Case 1 Passed\n");
}

// Test case 2
void test_is_valid_2() {
    char* s = "()[]{}";
    bool result = isValid(s);
    assert(result);
    printf("Test Case 2 Passed\n");
}

// Test case 3
void test_is_valid_3() {
    char* s = "(]";
    bool result = isValid(s);
    assert(!result);
    printf("Test Case 3 Passed\n");
}

// Test case 4
void test_is_valid_4() {
    char* s = "([)]";
    bool result = isValid(s);
    assert(!result);
    printf("Test Case 4 Passed\n");
}

// Test case 5
void test_is_valid_5() {
    char* s = "{[]}";
    bool result = isValid(s);
    assert(result);
    printf("Test Case 5 Passed\n");
}

// Test case 6
void test_is_valid_6() {
    char* s = "({[()]})";
    bool result = isValid(s);
    assert(result);
    printf("Test Case 6 Passed\n");
}

// Test case 7
void test_is_valid_7() {
    char* s = "";
    bool result = isValid(s);
    assert(result);
    printf("Test Case 7 Passed\n");
}

// Test case 8
void test_is_valid_8() {
    char* s = "[[[]]]";
    bool result = isValid(s);
    assert(result);
    printf("Test Case 8 Passed\n");
}

// Test case 9
void test_is_valid_9() {
    char* s = "[[[[]]";
    bool result = isValid(s);
    assert(!result);
    printf("Test Case 9 Passed\n");
}

int main() {
    test_is_valid_1();
    test_is_valid_2();
    test_is_valid_3();
    test_is_valid_4();
    test_is_valid_5();
    test_is_valid_6();
    test_is_valid_7();
    test_is_valid_8();
    test_is_valid_9();

    return 0;
}
