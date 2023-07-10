#include <stdio.h>
#include <stdbool.h>

// Function declaration
bool isPalindrome(int x);

// Function implementation
bool isPalindrome(int x) {
    if (x < 0) {
        return false;
    }

    int inputNum = x;
    int newNum = 0;
    while (x > 0) {
        newNum = newNum * 10 + x % 10;
        x = x / 10;
    }

    return newNum == inputNum;
}

// Test cases
void test_palindrome_number() {
    int x = 121;
    bool result = isPalindrome(x);

    printf("Test palindrome_number: ");
    if (result) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_non_palindrome_number() {
    int x = 123;
    bool result = isPalindrome(x);

    printf("Test non_palindrome_number: ");
    if (!result) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_negative_number() {
    int x = -121;
    bool result = isPalindrome(x);

    printf("Test negative_number: ");
    if (!result) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_single_digit_number() {
    int x = 5;
    bool result = isPalindrome(x);

    printf("Test single_digit_number: ");
    if (result) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_zero() {
    int x = 0;
    bool result = isPalindrome(x);

    printf("Test zero: ");
    if (result) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

int main() {
    test_palindrome_number();
    test_non_palindrome_number();
    test_negative_number();
    test_single_digit_number();
    test_zero();

    return 0;
}
