#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h> 
// Function declaration
char** findRestaurant(char** list1, int list1Size, char** list2, int list2Size, int* returnSize);

// Function implementation
char** findRestaurant(char** list1, int list1Size, char** list2, int list2Size, int* returnSize) {
    int* indexSum = (int*)malloc(sizeof(int) * list1Size);
    memset(indexSum, -1, sizeof(int) * list1Size);
    char** result = (char**)malloc(sizeof(char*) * list1Size);
    *returnSize = 0;
    int minIndexSum = INT_MAX;

    // Calculate index sum for common strings
    for (int i = 0; i < list1Size; i++) {
        for (int j = 0; j < list2Size; j++) {
            if (strcmp(list1[i], list2[j]) == 0) {
                int sum = i + j;
                if (sum < minIndexSum) {
                    minIndexSum = sum;
                    *returnSize = 0;
                }
                if (sum == minIndexSum) {
                    result[*returnSize] = (char*)malloc(sizeof(char) * (strlen(list1[i]) + 1));
                    strcpy(result[*returnSize], list1[i]);
                    indexSum[*returnSize] = sum;
                    (*returnSize)++;
                }
            }
        }
    }

    // Free memory and return result
    for (int i = 0; i < list1Size; i++) {
        if (indexSum[i] != minIndexSum) {
            free(result[i]);
        }
    }
    free(indexSum);
    return result;
}

// Test cases
void test_example_case() {
    char* list1[] = {"Shogun", "Tapioca Express", "Burger King", "KFC"};
    int list1Size = sizeof(list1) / sizeof(list1[0]);
    char* list2[] = {"Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"};
    int list2Size = sizeof(list2) / sizeof(list2[0]);
    int expectedSize = 1;
    char** expected = (char**)malloc(sizeof(char*) * expectedSize);
    expected[0] = (char*)malloc(sizeof(char) * (strlen("Shogun") + 1));
    strcpy(expected[0], "Shogun");

    int returnSize;
    char** result = findRestaurant(list1, list1Size, list2, list2Size, &returnSize);

    printf("Test example_case: ");
    if (returnSize == expectedSize) {
        int i;
        for (i = 0; i < returnSize; i++) {
            if (strcmp(result[i], expected[i]) != 0) {
                printf("FAILED\n");
                break;
            }
        }
        if (i == returnSize) {
            printf("PASSED\n");
        }
    } else {
        printf("FAILED\n");
    }

    // Free memory
    for (int i = 0; i < returnSize; i++) {
        free(result[i]);
    }
    free(result);
    for (int i = 0; i < expectedSize; i++) {
        free(expected[i]);
    }
    free(expected);
}

void test_multiple_common_restaurants() {
    char* list1[] = {"KFC", "Burger King", "Pizza Hut", "McDonald's"};
    int list1Size = sizeof(list1) / sizeof(list1[0]);
    char* list2[] = {"Burger King", "Pizza Hut", "McDonald's", "KFC"};
    int list2Size = sizeof(list2) / sizeof(list2[0]);
    int expectedSize = 1;
    char** expected = (char**)malloc(sizeof(char*) * expectedSize);
    expected[0] = (char*)malloc(sizeof(char) * (strlen("Burger King") + 1));
    strcpy(expected[0], "Burger King");

    int returnSize;
    char** result = findRestaurant(list1, list1Size, list2, list2Size, &returnSize);

    printf("Test multiple_common_restaurants: ");
    if (returnSize == expectedSize) {
        int i;
        for (i = 0; i < returnSize; i++) {
            if (strcmp(result[i], expected[i]) != 0) {
                printf("FAILED\n");
                break;
            }
        }
        if (i == returnSize) {
            printf("PASSED\n");
        }
    } else {
        printf("FAILED\n");
    }

    // Free memory
    for (int i = 0; i < returnSize; i++) {
        free(result[i]);
    }
    free(result);
    for (int i = 0; i < expectedSize; i++) {
        free(expected[i]);
    }
    free(expected);
}

void test_no_common_restaurant() {
    char* list1[] = {"Subway", "Starbucks", "Chipotle"};
    int list1Size = sizeof(list1) / sizeof(list1[0]);
    char* list2[] = {"McDonald's", "Taco Bell", "Wendy's"};
    int list2Size = sizeof(list2) / sizeof(list2[0]);
    int expectedSize = 0;
    char** expected = NULL;

    int returnSize;
    char** result = findRestaurant(list1, list1Size, list2, list2Size, &returnSize);

    printf("Test no_common_restaurant: ");
    if (returnSize == expectedSize) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }

    // Free memory
    for (int i = 0; i < returnSize; i++) {
        free(result[i]);
    }
    free(result);
}

void test_empty_lists() {
    char* list1[] = {};
    int list1Size = sizeof(list1) / sizeof(list1[0]);
    char* list2[] = {};
    int list2Size = sizeof(list2) / sizeof(list2[0]);
    int expectedSize = 0;
    char** expected = NULL;

    int returnSize;
    char** result = findRestaurant(list1, list1Size, list2, list2Size, &returnSize);

    printf("Test empty_lists: ");
    if (returnSize == expectedSize) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }

    // Free memory
    for (int i = 0; i < returnSize; i++) {
        free(result[i]);
    }
    free(result);
}

int main() {
    test_empty_lists();
    test_no_common_restaurant();
    test_multiple_common_restaurants();
}
