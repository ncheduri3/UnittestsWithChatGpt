#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

int sumOfMultiples(int n);

// Function to calculate the sum of multiples of 3, 5, or 7 up to n
int sumOfMultiples(int n) {
    int sum = 0;
    for (int x = 1; x <= n; x++) {
        if (x % 3 == 0 || x % 5 == 0 || x % 7 == 0) {
            sum += x;
        }
    }
    return sum;
}

// Test case 1
void test_sum_of_multiples_1() {
    int result = sumOfMultiples(10);
    assert(result == 40);
    printf("Test Case 1 Passed\n");
}

// Test case 2
void test_sum_of_multiples_2() {
    int result = sumOfMultiples(20);
    assert(result == 119);
    printf("Test Case 2 Passed\n");
}

// Test case 3
void test_sum_of_multiples_3() {
    int result = sumOfMultiples(5);
    assert(result == 8);
    printf("Test Case 3 Passed\n");
}

// Test case 4
void test_sum_of_multiples_4() {
    int result = sumOfMultiples(15);
    assert(result == 81);
    printf("Test Case 4 Passed\n");
}

// Test case 5
void test_sum_of_multiples_5() {
    int result = sumOfMultiples(1);
    assert(result == 0);
    printf("Test Case 5 Passed\n");
}

int main() {
    test_sum_of_multiples_1();
    test_sum_of_multiples_2();
    test_sum_of_multiples_3();
    test_sum_of_multiples_4();
    test_sum_of_multiples_5();

    return 0;
}
