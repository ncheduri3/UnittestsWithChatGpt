#include <stdio.h>
#include <stdbool.h>

// Function declaration
int removeElement(int* nums, int numsSize, int val);

// Function implementation
int removeElement(int* nums, int numsSize, int val) {
    int i = 0;
    for (int j = 0; j < numsSize; j++) {
        if (nums[j] != val) {
            nums[i] = nums[j];
            i++;
        }
    }
    return i;
}

// Test cases
void test_remove_element() {
    int nums[] = {3, 2, 2, 3};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int val = 3;
    int expected_output = 2;

    int result = removeElement(nums, numsSize, val);

    printf("Test remove_element: ");
    if (result == expected_output && nums[0] == 2 && nums[1] == 2) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_remove_all_elements() {
    int nums[] = {1, 1, 1, 1};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int val = 1;
    int expected_output = 0;

    int result = removeElement(nums, numsSize, val);

    printf("Test remove_all_elements: ");
    if (result == expected_output) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_remove_no_elements() {
    int nums[] = {4, 5, 6};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int val = 1;
    int expected_output = 3;

    int result = removeElement(nums, numsSize, val);

    printf("Test remove_no_elements: ");
    if (result == expected_output && nums[0] == 4 && nums[1] == 5 && nums[2] == 6) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_remove_duplicate_elements() {
    int nums[] = {2, 2, 3, 3, 4};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int val = 3;
    int expected_output = 3;

    int result = removeElement(nums, numsSize, val);

    printf("Test remove_duplicate_elements: ");
    if (result == expected_output && nums[0] == 2 && nums[1] == 2 && nums[2] == 4) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

int main() {
    test_remove_element();
    test_remove_all_elements();
    test_remove_no_elements();
    test_remove_duplicate_elements();

    return 0;
}
