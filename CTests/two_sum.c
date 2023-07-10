#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize);

// Function to find the indices of two numbers that add up to the target
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int* result = (int*)malloc(sizeof(int) * 2);
    int* map = (int*)calloc(100000, sizeof(int));

    for (int i = 0; i < numsSize; i++) {
        int complement = target - nums[i];
        if (map[complement] != 0) {
            result[0] = map[complement] - 1;
            result[1] = i;
            *returnSize = 2;
            return result;
        }
        map[nums[i]] = i + 1;
    }

    *returnSize = 0;
    return NULL;
}

// Test case 1
void test_two_sum_1() {
    int nums[] = {2, 7, 11, 15};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int target = 9;
    int returnSize;
    int* result = twoSum(nums, numsSize, target, &returnSize);
    assert(returnSize == 2);
    assert(result[0] == 0);
    assert(result[1] == 1);
    printf("Test Case 1 Passed\n");
    free(result);
}

// Test case 2
void test_two_sum_2() {
    int nums[] = {3, 6, 8, 12};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int target = 5;
    int returnSize;
    int* result = twoSum(nums, numsSize, target, &returnSize);
    assert(returnSize == 0);
    assert(result == NULL);
    printf("Test Case 2 Passed\n");
}

// Test case 3
void test_two_sum_3() {
    int nums[] = {2, 7, 11, 15, 7};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int target = 14;
    int returnSize;
    int* result = twoSum(nums, numsSize, target, &returnSize);
    assert(returnSize == 2);
    assert(result[0] == 1);
    assert(result[1] == 4);
    printf("Test Case 3 Passed\n");
    free(result);
}

// Test case 4
void test_two_sum_4() {
    int nums[] = {-2, -7, 11, 15};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int target = 9;
    int returnSize;
    int* result = twoSum(nums, numsSize, target, &returnSize);
    assert(returnSize == 2);
    assert(result[0] == 0);
    assert(result[1] == 2);
    printf("Test Case 4 Passed\n");
    free(result);
}

// Test case 5
void test_two_sum_5() {
    int* nums = NULL;
    int numsSize = 0;
    int target = 9;
    int returnSize;
    int* result = twoSum(nums, numsSize, target, &returnSize);
    assert(returnSize == 0);
    assert(result == NULL);
    printf("Test Case 5 Passed\n");
}

int main() {
    test_two_sum_1();
    test_two_sum_2();
    test_two_sum_3();
    test_two_sum_4();
    test_two_sum_5();

    return 0;
}
