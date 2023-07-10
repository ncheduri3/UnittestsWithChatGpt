#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Function declaration
void moveZeroes(int* nums, int numsSize);

// Function implementation
void moveZeroes(int* nums, int numsSize) {
    int slow = 0;
    for (int fast = 0; fast < numsSize; fast++) {
        if (nums[fast] != 0 && nums[slow] == 0) {
            int temp = nums[slow];
            nums[slow] = nums[fast];
            nums[fast] = temp;
        }

        // Wait while we find a non-zero element to swap with 'slow'
        if (nums[slow] != 0) {
            slow++;
        }
    }
}

// Test cases
void test_move_zeroes() {
    int nums[] = {0, 1, 0, 3, 12};
    int expected[] = {1, 3, 12, 0, 0};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    moveZeroes(nums, numsSize);

    printf("Test move_zeroes: ");
    bool success = true;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != expected[i]) {
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

void test_no_zeroes() {
    int nums[] = {1, 2, 3, 4, 5};
    int expected[] = {1, 2, 3, 4, 5};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    moveZeroes(nums, numsSize);

    printf("Test no_zeroes: ");
    bool success = true;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != expected[i]) {
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

void test_all_zeroes() {
    int nums[] = {0, 0, 0, 0, 0};
    int expected[] = {0, 0, 0, 0, 0};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    moveZeroes(nums, numsSize);

    printf("Test all_zeroes: ");
    bool success = true;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != expected[i]) {
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

void test_mixed_elements() {
    int nums[] = {0, 2, 0, 1, 0, 3, 0, 0, 12};
    int expected[] = {2, 1, 3, 12, 0, 0, 0, 0, 0};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    moveZeroes(nums, numsSize);

    printf("Test mixed_elements: ");
    bool success = true;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != expected[i]) {
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

int main() {
    test_move_zeroes();
    test_no_zeroes();
    test_all_zeroes();
    test_mixed_elements();

    return 0;
}
