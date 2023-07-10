#include <stdio.h>
#include <stdbool.h>
#include <assert.h>

bool isMonotonic(int* nums, int numsSize) {
    bool increasing = true;
    bool decreasing = true;

    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < nums[i - 1]) {
            increasing = false;
        }
        if (nums[i] > nums[i - 1]) {
            decreasing = false;
        }
    }

    return increasing || decreasing;
}

void test_increasing_list() {
    int nums[] = {1, 2, 3, 4, 5};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    bool result = isMonotonic(nums, numsSize);
    bool expected = true;
    assert(result == expected);
    printf("Test case 'increasing_list' passed\n");
}

void test_decreasing_list() {
    int nums[] = {5, 4, 3, 2, 1};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    bool result = isMonotonic(nums, numsSize);
    bool expected = true;
    assert(result == expected);
    printf("Test case 'decreasing_list' passed\n");
}

void test_monotonic_list() {
    int nums[] = {1, 3, 5, 7, 9};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    bool result = isMonotonic(nums, numsSize);
    bool expected = true;
    assert(result == expected);
    printf("Test case 'monotonic_list' passed\n");
}

void test_non_monotonic_list() {
    int nums[] = {1, 3, 2, 5, 4};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    bool result = isMonotonic(nums, numsSize);
    bool expected = false;
    assert(result == expected);
    printf("Test case 'non_monotonic_list' passed\n");
}

void test_equal_elements_list() {
    int nums[] = {5, 5, 5, 5, 5};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    bool result = isMonotonic(nums, numsSize);
    bool expected = true;
    assert(result == expected);
    printf("Test case 'equal_elements_list' passed\n");
}

int main() {
    test_increasing_list();
    test_decreasing_list();
    test_monotonic_list();
    test_non_monotonic_list();
    test_equal_elements_list();

    return 0;
}
