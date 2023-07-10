#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

void merge(int* nums1, int m, int* nums2, int n) {
    int i = m - 1;
    int j = n - 1;
    int k = m + n - 1;

    while (i >= 0 && j >= 0) {
        if (nums1[i] > nums2[j]) {
            nums1[k--] = nums1[i--];
        } else {
            nums1[k--] = nums2[j--];
        }
    }

    while (j >= 0) {
        nums1[k--] = nums2[j--];
    }
}

bool testMergeLists() {
    int nums1[] = {1, 2, 3, 0, 0, 0};
    int m = 3;
    int nums2[] = {2, 5, 6};
    int n = 3;
    int expectedOutput[] = {1, 2, 2, 3, 5, 6};
    merge(nums1, m, nums2, n);

    for (int i = 0; i < m + n; i++) {
        if (nums1[i] != expectedOutput[i]) {
            printf("Merge Lists Case: Failed\n");
            return false;
        }
    }

    printf("Merge Lists Case: Passed\n");
    return true;
}

bool testEmptyList() {
    int nums1[] = {};
    int m = 0;
    int nums2[] = {};
    int n = 0;
    merge(nums1, m, nums2, n);
    printf("Empty List Case: Passed\n");
    return true;
}

bool testMergeIntoEmptyList() {
    int nums1[] = {0, 0, 0};
    int m = 0;
    int nums2[] = {1, 2, 3};
    int n = 3;
    int expectedOutput[] = {1, 2, 3};
    merge(nums1, m, nums2, n);

    for (int i = 0; i < m + n; i++) {
        if (nums1[i] != expectedOutput[i]) {
            printf("Merge Into Empty List Case: Failed\n");
            return false;
        }
    }

    printf("Merge Into Empty List Case: Passed\n");
    return true;
}

bool testMergeWithDuplicateElements() {
    int nums1[] = {1, 2, 3, 0, 0, 0};
    int m = 3;
    int nums2[] = {2, 2, 3};
    int n = 3;
    int expectedOutput[] = {1, 2, 2, 2, 3, 3};
    merge(nums1, m, nums2, n);

    for (int i = 0; i < m + n; i++) {
        if (nums1[i] != expectedOutput[i]) {
            printf("Merge With Duplicate Elements Case: Failed\n");
            return false;
        }
    }

    printf("Merge With Duplicate Elements Case: Passed\n");
    return true;
}


int main() {
    bool success = true;
    success &= testMergeLists();
    success &= testEmptyList();
    success &= testMergeIntoEmptyList();
    success &= testMergeWithDuplicateElements();

    if (success) {
        printf("All test cases passed!\n");
    } else {
        printf("Some test cases failed!\n");
    }

    return 0;
}
