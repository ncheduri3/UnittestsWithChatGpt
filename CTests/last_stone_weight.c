#include <stdio.h>
#include <stdbool.h>
#include <assert.h>
#include <stdlib.h>

int compareInt(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int lastStoneWeight(int stones[], int n) {
    qsort(stones, n, sizeof(int), compareInt);

    while (n > 1) {
        int s1 = stones[n - 1];
        int s2 = stones[n - 2];
        n -= 2;

        if (s1 > s2) {
            stones[n] = s1 - s2;
            n++;
            qsort(stones, n, sizeof(int), compareInt);
        }
    }

    return (n == 1) ? stones[0] : 0;
}

void test_single_stone() {
    int stones[] = {5};
    int n = sizeof(stones) / sizeof(stones[0]);
    int result = lastStoneWeight(stones, n);
    assert(result == 5);
    printf("Test case 'single_stone' passed\n");
}

void test_two_stones() {
    int stones[] = {3, 7};
    int n = sizeof(stones) / sizeof(stones[0]);
    int result = lastStoneWeight(stones, n);
    assert(result == 4);
    printf("Test case 'two_stones' passed\n");
}

void test_multiple_stones() {
    int stones[] = {2, 7, 4, 1, 8, 1};
    int n = sizeof(stones) / sizeof(stones[0]);
    int result = lastStoneWeight(stones, n);
    assert(result == 1);
    printf("Test case 'multiple_stones' passed\n");
}

void test_same_weight_stones() {
    int stones[] = {5, 5, 5, 5};
    int n = sizeof(stones) / sizeof(stones[0]);
    int result = lastStoneWeight(stones, n);
    assert(result == 0);
    printf("Test case 'same_weight_stones' passed\n");
}

void test_empty_list() {
    int stones[] = {};
    int n = sizeof(stones) / sizeof(stones[0]);
    int result = lastStoneWeight(stones, n);
    assert(result == 0);
    printf("Test case 'empty_list' passed\n");
}

int main() {
    test_single_stone();
    test_two_stones();
    test_multiple_stones();
    test_same_weight_stones();
    test_empty_list();
    return 0;
}
