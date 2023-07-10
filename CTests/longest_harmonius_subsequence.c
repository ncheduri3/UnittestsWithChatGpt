#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int findLHS(int* nums, int numsSize) {
    int* freq = (int*)calloc(20001, sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        freq[nums[i] + 10000]++;
    }

    int maxLength = 0;
    for (int i = 0; i < 20000; i++) {
        if (freq[i] > 0 && freq[i + 1] > 0) {
            int length = freq[i] + freq[i + 1];
            if (length > maxLength) {
                maxLength = length;
            }
        }
    }

    free(freq);
    return maxLength;
}

bool testExampleCase() {
    int nums[] = {1, 3, 2, 2, 5, 2, 3, 7};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int expected = 5;
    int result = findLHS(nums, numsSize);
    if (result == expected) {
        printf("Example Case: Passed\n");
        return true;
    } else {
        printf("Example Case: Failed\n");
        return false;
    }
}

bool testEmptyList() {
    int nums[] = {};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int expected = 0;
    int result = findLHS(nums, numsSize);
    if (result == expected) {
        printf("Empty List Case: Passed\n");
        return true;
    } else {
        printf("Empty List Case: Failed\n");
        return false;
    }
}

bool testSingleElement() {
    int nums[] = {5};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int expected = 0;
    int result = findLHS(nums, numsSize);
    if (result == expected) {
        printf("Single Element Case: Passed\n");
        return true;
    } else {
        printf("Single Element Case: Failed\n");
        return false;
    }
}

bool testNoConsecutiveElements() {
    int nums[] = {1, 2, 3, 4, 5};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int expected = 2;
    int result = findLHS(nums, numsSize);
    if (result == expected) {
        printf("No Consecutive Elements Case: Passed\n");
        return true;
    } else {
        printf("No Consecutive Elements Case: Failed\n");
        return false;
    }
}

bool testNegativeNumbers() {
    int nums[] = {-1, -2, -2, -2, -3, -4, -5};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int expected = 4;
    int result = findLHS(nums, numsSize);
    if (result == expected) {
        printf("Negative Numbers Case: Passed\n");
        return true;
    } else {
        printf("Negative Numbers Case: Failed\n");
        return false;
    }
}

bool testLargeInput() {
    int* nums = (int*)malloc(20000 * sizeof(int));
    for (int i = 0; i < 10000; i++) {
        nums[i] = 1000000000;
        nums[i + 10000] = 0;
    }
    int expected = 0;
    int result = findLHS(nums, 20000);
    if (result == expected) {
        printf("Large Input Case: Passed\n");
        return true;
    } else {
        printf("Large Input Case: Failed\n");
        return false;
    }
}

void runTestCases() {
    bool success = true;
    success &= testExampleCase();
    success &= testEmptyList();
    success &= testSingleElement();
    success &= testNoConsecutiveElements();
    success &= testNegativeNumbers();
    success &= testLargeInput();
    
    if (success) {
        printf("All test cases passed!\n");
    } else {
        printf("Some test cases failed!\n");
    }
}

int main() {
    runTestCases();

    return 0;
}
