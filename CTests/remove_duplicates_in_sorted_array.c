#include <stdio.h>
#include <stdbool.h>

// Function declaration
int removeDuplicates(int* nums, int numsSize);

// Function implementation
int removeDuplicates(int* nums, int numsSize) {
    if (numsSize == 0) {
        return 0;
    }

    int j = 0;
    for (int i = 1; i < numsSize; i++) {
        if (nums[j] != nums[i]) {
            j++;
            nums[j] = nums[i];
        }
    }

    return j + 1;
}

// Test cases
void test_no_duplicates() {
    int nums[] = {1, 2, 3, 4, 5};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int expected_output = 5;

    int result = removeDuplicates(nums, numsSize);

    printf("Test no_duplicates: ");
    if (result == expected_output) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_duplicates_present() {
    int nums[] = {1, 1, 2, 2, 3};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int expected_output = 3;

    int result = removeDuplicates(nums, numsSize);

    printf("Test duplicates_present: ");
    if (result == expected_output) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_single_element_list() {
    int nums[] = {5};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int expected_output = 1;

    int result = removeDuplicates(nums, numsSize);

    printf("Test single_element_list: ");
    if (result == expected_output) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_all_duplicates() {
    int nums[] = {2, 2, 2, 2, 2};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int expected_output = 1;

    int result = removeDuplicates(nums, numsSize);

    printf("Test all_duplicates: ");
    if (result == expected_output) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

int main() {
    test_no_duplicates();
    test_duplicates_present();
    test_single_element_list();
    test_all_duplicates();

    return 0;
}
