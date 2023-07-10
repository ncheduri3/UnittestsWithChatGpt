#include <stdio.h>
#include <stdbool.h>

// Function declaration
int countPrimeSetBits(int left, int right);

// Function implementation
int countPrimeSetBits(int left, int right) {
    int count = 0;
    for (int i = left; i <= right; i++) {
        int n = i;
        int setBits = 0;

        while (n > 0) {
            if (n % 2 == 1) {
                setBits++;
            }
            n /= 2;
        }

        int divisors = 0;
        for (int j = 1; j <= setBits; j++) {
            if (setBits % j == 0) {
                divisors++;
            }
        }

        if (divisors == 2) {
            count++;
        }
    }
    return count;
}

// Test cases
void test_left_equal_to_right() {
    int left = 10;
    int right = 10;
    int expected = 1;

    int result = countPrimeSetBits(left, right);

    printf("Test left_equal_to_right: ");
    if (result == expected) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_no_prime_set_bits() {
    int left = 1;
    int right = 10;
    int expected = 6;

    int result = countPrimeSetBits(left, right);

    printf("Test no_prime_set_bits: ");
    if (result == expected) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_all_prime_set_bits() {
    int left = 10;
    int right = 15;
    int expected = 5;

    int result = countPrimeSetBits(left, right);

    printf("Test all_prime_set_bits: ");
    if (result == expected) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_mixed_prime_set_bits() {
    int left = 3;
    int right = 7;
    int expected = 4;

    int result = countPrimeSetBits(left, right);

    printf("Test mixed_prime_set_bits: ");
    if (result == expected) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_large_range() {
    int left = 1000;
    int right = 1010;
    int expected = 5;

    int result = countPrimeSetBits(left, right);

    printf("Test large_range: ");
    if (result == expected) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

int main() {
    test_left_equal_to_right();
    test_no_prime_set_bits();
    test_all_prime_set_bits();
    test_mixed_prime_set_bits();
    test_large_range();

    return 0;
}
