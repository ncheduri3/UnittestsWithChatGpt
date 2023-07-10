#include <stdio.h>
#include <stdbool.h>
#include <assert.h>

int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
    int onesCount = k < numOnes ? k : numOnes;
    int remainingItems = k - onesCount - numZeros;

    int negOnesCount = 0;
    if (remainingItems > 0)
        negOnesCount = remainingItems < numNegOnes ? remainingItems : numNegOnes;

    return onesCount + (negOnesCount * -1);
}

void test_case_1() {
    assert(kItemsWithMaximumSum(5, 3, 2, 4) == 4);
    printf("Test case 1 passed\n");
}

void test_case_2() {
    assert(kItemsWithMaximumSum(2, 4, 1, 3) == 2);
    printf("Test case 2 passed\n");
}

void test_case_3() {
    assert(kItemsWithMaximumSum(0, 0, 0, 2) == 0);
    printf("Test case 3 passed\n");
}

void test_case_4() {
    assert(kItemsWithMaximumSum(10, 5, 3, 10) == 10);
    printf("Test case 4 passed\n");
}

void test_case_5() {
    assert(kItemsWithMaximumSum(3, 2, 1, 6) == 2);
    printf("Test case 5 passed\n");
}

int main() {
    test_case_1();
    test_case_2();
    test_case_3();
    test_case_4();
    test_case_5();

    return 0;
}
