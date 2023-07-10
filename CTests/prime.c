#include <stdio.h>
#include <stdbool.h>

// Function declaration
bool check_is_prime(int n);

// Function implementation
bool check_is_prime(int n) {
    if (n <= 1) {
        return false;
    }

    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }

    return true;
}

// Test cases
void test_prime_numbers() {
    int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
    int numPrimes = sizeof(primes) / sizeof(primes[0]);

    printf("Test prime_numbers: ");
    bool success = true;
    for (int i = 0; i < numPrimes; i++) {
        if (!check_is_prime(primes[i])) {
            success = false;
            break;
        }
    }
    if (success) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_non_prime_numbers() {
    int nonPrimes[] = {1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20};
    int numNonPrimes = sizeof(nonPrimes) / sizeof(nonPrimes[0]);

    printf("Test non_prime_numbers: ");
    bool success = true;
    for (int i = 0; i < numNonPrimes; i++) {
        if (check_is_prime(nonPrimes[i])) {
            success = false;
            break;
        }
    }
    if (success) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_negative_number() {
    int negativeNumber = -7;

    printf("Test negative_number: ");
    if (!check_is_prime(negativeNumber)) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_zero() {
    int zero = 0;

    printf("Test zero: ");
    if (!check_is_prime(zero)) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_one() {
    int one = 1;

    printf("Test one: ");
    if (!check_is_prime(one)) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

int main() {
    test_prime_numbers();
    test_non_prime_numbers();
    test_negative_number();
    test_zero();
    test_one();

    return 0;
}
