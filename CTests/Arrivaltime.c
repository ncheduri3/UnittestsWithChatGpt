#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>

int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
    return (arrivalTime + delayedTime) % 24;
}

void test_case_1() {
    int result = findDelayedArrivalTime(10, 5);
    assert(result == 15);
    printf("Test case 1 passed\n");
}

void test_case_2() {
    int result = findDelayedArrivalTime(20, 8);
    assert(result == 4);
    printf("Test case 2 passed\n");
}

void test_case_3() {
    int result = findDelayedArrivalTime(5, 20);
    assert(result == 1);
    printf("Test case 3 passed\n");
}

void test_case_4() {
    int result = findDelayedArrivalTime(15, 0);
    assert(result == 15);
    printf("Test case 4 passed\n");
}

void test_case_5() {
    int result = findDelayedArrivalTime(23, 3);
    assert(result == 2);
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
