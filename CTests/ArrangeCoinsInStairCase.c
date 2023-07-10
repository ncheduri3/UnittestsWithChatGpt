#include <stdio.h>
#include <math.h>

int arrangeCoins(int n) {
    return (int)(sqrt(2 * n + 0.25) - 0.50);
}

void test_5_coins() {
    int n = 5;
    int expected = 2;
    int result = arrangeCoins(n);
    if (result == expected) {
        printf("Test 1 passed\n");
    } else {
        printf("Test 1 failed. Expected: %d, Got: %d\n", expected, result);
    }
}

void test_8_coins() {
    int n = 8;
    int expected = 3;
    int result = arrangeCoins(n);
    if (result == expected) {
        printf("Test 2 passed\n");
    } else {
        printf("Test 2 failed. Expected: %d, Got: %d\n", expected, result);
    }
}

void test_10_coins() {
    int n = 10;
    int expected = 4;
    int result = arrangeCoins(n);
    if (result == expected) {
        printf("Test 3 passed\n");
    } else {
        printf("Test 3 failed. Expected: %d, Got: %d\n", expected, result);
    }
}

void test_0_coins() {
    int n = 0;
    int expected = 0;
    int result = arrangeCoins(n);
    if (result == expected) {
        printf("Test 4 passed\n");
    } else {
        printf("Test 4 failed. Expected: %d, Got: %d\n", expected, result);
    }
}

void test_large_number_of_coins() {
    int n = 1000000;
    int expected = 1413;
    int result = arrangeCoins(n);
    if (result == expected) {
        printf("Test 5 passed\n");
    } else {
        printf("Test 5 failed. Expected: %d, Got: %d\n", expected, result);
    }
}

int main() {
    // Run individual test functions
    test_5_coins();
    test_8_coins();
    test_10_coins();
    test_0_coins();
    test_large_number_of_coins();

    return 0;
}
