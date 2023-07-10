#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Function declaration
bool selfDividing(int num);
int* selfDividingNumbers(int left, int right, int* returnSize);

// Function to check if a number is self-dividing
bool selfDividing(int num) {
    int temp = num;
    while (temp > 0) {
        int digit = temp % 10;
        if (digit == 0 || num % digit != 0) {
            return false;
        }
        temp /= 10;
    }
    return true;
}

// Function to find self-dividing numbers in the range [left, right]
int* selfDividingNumbers(int left, int right, int* returnSize) {
    int* result = (int*)malloc((right - left + 1) * sizeof(int));
    int count = 0;
    for (int i = left; i <= right; i++) {
        if (selfDividing(i)) {
            result[count++] = i;
        }
    }
    *returnSize = count;
    return result;
}

// Test cases
void test_valid_range() {
    int left = 1;
    int right = 100;
    int* expected_output = (int[]) {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22, 24, 33, 36, 44, 48, 55, 66, 77, 88, 99};
    int expected_size = 23;

    int* result;
    int returnSize;

    result = selfDividingNumbers(left, right, &returnSize);

    printf("Test valid_range: ");

    if (returnSize == expected_size) {

        bool passed = true;
        for (int i = 0; i < returnSize; i++) {
            if (result[i] != expected_output[i]) {
                
                passed = false;
                break;
            }
        }
        if (passed) {
            printf("PASSED\n");
            return;
        }
    }
    printf("FAILED\n");
}



int main() {
    test_valid_range();

    return 0;
}
