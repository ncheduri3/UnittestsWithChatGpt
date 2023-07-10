#include <stdio.h>
#include <stdbool.h>
#include <assert.h>

int computeSumOfSquares(int n) {
    int sum_of_squares = 0;
    while (n > 0) {
        int digit = n % 10;
        sum_of_squares += digit * digit;
        n /= 10;
    }
    return sum_of_squares;
}

bool isHappy(int n) {
    int visited[1000] = {0};
    int index = 0;

    while (n != 1) {
        n = computeSumOfSquares(n);

        // Check if sum is already visited
        for (int i = 0; i < index; i++) {
            if (n == visited[i]) {
                return false;
            }
        }

        visited[index++] = n;
    }

    return true;
}

void test_happy_number() {
    int n = 19;
    bool result = isHappy(n);
    bool expected = true;
    assert(result == expected);
    printf("Test case 'happy_number' passed\n");
}

void test_unhappy_number() {
    int n = 20;
    bool result = isHappy(n);
    bool expected = false;
    assert(result == expected);
    printf("Test case 'unhappy_number' passed\n");
}

void test_zero() {
    int n = 0;
    bool result = isHappy(n);
    bool expected = false;
    assert(result == expected);
    printf("Test case 'zero' passed\n");
}

void test_single_digit_happy_number() {
    int n = 7;
    bool result = isHappy(n);
    bool expected = true;
    assert(result == expected);
    printf("Test case 'single_digit_happy_number' passed\n");
}

void test_single_digit_unhappy_number() {
    int n = 4;
    bool result = isHappy(n);
    bool expected = false;
    assert(result == expected);
    printf("Test case 'single_digit_unhappy_number' passed\n");
}

int main() {
    test_happy_number();
    test_unhappy_number();
    test_zero();
    test_single_digit_happy_number();
    test_single_digit_unhappy_number();

    return 0;
}
