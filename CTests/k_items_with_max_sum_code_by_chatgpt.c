#include <stdio.h>
#include <stdbool.h>
#include <assert.h>

int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
    int ones_taken = k < numOnes ? k : numOnes;
    int remaining_k = k - ones_taken;
    int neg_ones_taken = 0;
    if (remaining_k > 0)
        neg_ones_taken = remaining_k < numNegOnes ? remaining_k : numNegOnes;
    return ones_taken + (neg_ones_taken * -1);
}

void test_k_items_with_maximum_sum_corrected() {
    int numOnes, numZeros, numNegOnes, k;

    // Test Case 1
    numOnes = 5;
    numZeros = 3;
    numNegOnes = 2;
    k = 4;
    assert(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k) == 4);
    printf("Test case 1 passed\n");

    // Test Case 2
    numOnes = 2;
    numZeros = 4;
    numNegOnes = 1;
    k = 3;
    assert(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k) == 1);
    printf("Test case 2 passed\n");

    // Test Case 3
    numOnes = 0;
    numZeros = 0;
    numNegOnes = 0;
    k = 2;
    assert(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k) == 0);
    printf("Test case 3 passed\n");

    // Test Case 4
    numOnes = 10;
    numZeros = 5;
    numNegOnes = 3;
    k = 10;
    assert(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k) == 10);
    printf("Test case 4 passed\n");

    // Test Case 5
    numOnes = 3;
    numZeros = 2;
    numNegOnes = 1;
    k = 6;
    assert(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k) == 2);
    printf("Test case 5 passed\n");
}

int main() {
    test_k_items_with_maximum_sum_corrected();
    return 0;
}
