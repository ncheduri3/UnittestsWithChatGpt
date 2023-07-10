#include <stdio.h>
#include <stdbool.h>
#include <assert.h>

bool containsDuplicate(int nums[], int length) {
    for (int i = 0; i < length; i++) {
        for (int j = i + 1; j < length; j++) {
            if (nums[i] == nums[j]) {
                return true;
            }
        }
    }
    return false;
}

void test_duplicates_present() {
    int nums[] = {1, 2, 3, 1};
    int length = sizeof(nums) / sizeof(nums[0]);
    bool result = containsDuplicate(nums, length);
    assert(result == true);
    printf("Test case 'duplicates_present' passed\n");
}

void test_no_duplicates() {
    int nums[] = {1, 2, 3, 4};
    int length = sizeof(nums) / sizeof(nums[0]);
    bool result = containsDuplicate(nums, length);
    assert(result == false);
    printf("Test case 'no_duplicates' passed\n");
}

void test_empty_array() {
    int nums[] = {};
    int length = sizeof(nums) / sizeof(nums[0]);
    bool result = containsDuplicate(nums, length);
    assert(result == false);
    printf("Test case 'empty_array' passed\n");
}

void test_single_element_array() {
    int nums[] = {5};
    int length = sizeof(nums) / sizeof(nums[0]);
    bool result = containsDuplicate(nums, length);
    assert(result == false);
    printf("Test case 'single_element_array' passed\n");
}

void test_duplicates_with_negative_numbers() {
    int nums[] = {-1, 2, -1, 4};
    int length = sizeof(nums) / sizeof(nums[0]);
    bool result = containsDuplicate(nums, length);
    assert(result == true);
    printf("Test case 'duplicates_with_negative_numbers' passed\n");
}

int main() {
    test_duplicates_present();
    test_no_duplicates();
    test_empty_array();
    test_single_element_array();
    test_duplicates_with_negative_numbers();

    return 0;
}
