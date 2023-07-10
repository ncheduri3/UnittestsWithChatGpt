#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Function declaration
int* sortedSquares(int* nums, int numsSize, int* returnSize);

// Function to return array of squares of each number sorted in non-decreasing order
int* sortedSquares(int* nums, int numsSize, int* returnSize) {
    int* result = (int*)malloc(numsSize * sizeof(int));
    *returnSize = numsSize;

    int left = 0;
    int right = numsSize - 1;
    int index = numsSize - 1;

    while (left <= right) {
        int leftSquare = nums[left] * nums[left];
        int rightSquare = nums[right] * nums[right];

        if (leftSquare > rightSquare) {
            result[index--] = leftSquare;
            left++;
        } else {
            result[index--] = rightSquare;
            right--;
        }
    }

    return result;
}

// Test cases
void test_sorted_squares() {
    bool success = true;
    int nums[] = {-4, -1, 0, 3, 10};
    int expected[] = {0, 1, 9, 16, 100};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    int returnSize;
    int* result = sortedSquares(nums, numsSize, &returnSize);

    printf("Test sorted_squares: ");
    if (numsSize == returnSize ) {
        for (int i = 0; i < returnSize; i++) {
            if(result[i] != expected[i]){
                 success = false;
                 break;
            }
               


        }
    }
    if(success) {
        printf(" Test sorted squares passed");
    } else {
        printf(" Test sorted squares failed");
    }

    printf("\n");

    free(result);
}

void test_sorted_squares_negative_numbers() {
    bool success = true;
    int nums[] = {-7, -3, -2, 0, 5};
    int expected[] = {0, 4, 9, 25, 49};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    int returnSize;
    int* result = sortedSquares(nums, numsSize, &returnSize);


   
    if (numsSize == returnSize ) {
        for (int i = 0; i < returnSize; i++) {
            if(result[i] != expected[i]){
                 success = false;
                 break;
            }
               


        }
    }
    if(success) {
        printf(" Test sorted_squares_negative_numbers passed");
    } else {
        printf(" Test sorted_squares_negative_numbers failed");
    }
     printf("\n");
    free(result);
}

void test_sorted_squares_positive_numbers() {
    bool success = true;
    int nums[] = {1, 2, 3, 4, 5};
    int expected[] = {1, 4, 9, 16, 25};
    int numsSize = sizeof(nums) / sizeof(nums[0]);

    int returnSize;
    int* result = sortedSquares(nums, numsSize, &returnSize);


     if (numsSize == returnSize ) {
        for (int i = 0; i < returnSize; i++) {
            if(result[i] != expected[i]){
                 success = false;
                 break;
            }
               


        }
    }
    if(success) {
        printf(" Test sorted_squares_positive_numbers passed");
    } else {
        printf(" Test sorted_squares_positive_numbers failed");
    }
    printf("\n");

    free(result);
}




int main() {
    test_sorted_squares();
    test_sorted_squares_negative_numbers();
    test_sorted_squares_positive_numbers();


    return 0;
}
