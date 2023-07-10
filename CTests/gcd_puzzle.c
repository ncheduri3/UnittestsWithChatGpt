#include <stdio.h>
#include <stdbool.h>
#include <assert.h>

bool divisorGame(int n) {
    return n % 2 == 0;
}

void test_even_number() {
    int n = 4;
    bool result = divisorGame(n);
    bool expected = true;
    assert(result == expected);
    printf("Test case 'even_number' passed\n");
}

void test_odd_number() {
    int n = 7;
    bool result = divisorGame(n);
    bool expected = false;
    assert(result == expected);
    printf("Test case 'odd_number' passed\n");
}

void test_zero() {
    int n = 0;
    bool result = divisorGame(n);
    bool expected = true;
    assert(result == expected);
    printf("Test case 'zero' passed\n");
}

void test_large_number() {
    int n = 1000000;
    bool result = divisorGame(n);
    bool expected = true;
    assert(result == expected);
    printf("Test case 'large_number' passed\n");
}

int main() {
    test_even_number();
    test_odd_number();
    test_zero();
    test_large_number();

    return 0;
}
