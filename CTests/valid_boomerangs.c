#include <stdio.h>
#include <stdbool.h>
#include <assert.h>

bool isBoomerang(int points[3][2]);

// Function to check if the given points form a boomerang
bool isBoomerang(int points[3][2]) {
    int x1 = points[0][0], y1 = points[0][1];
    int x2 = points[1][0], y2 = points[1][1];
    int x3 = points[2][0], y3 = points[2][1];

    return (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1);
}

// Test case 1
void test_is_boomerang_1() {
    int points[3][2] = {{1, 1}, {2, 3}, {3, 2}};
    bool result = isBoomerang(points);
    assert(result);
    printf("Test Case 1 Passed\n");
}

// Test case 2
void test_is_boomerang_2() {
    int points[3][2] = {{1, 1}, {2, 2}, {3, 3}};
    bool result = isBoomerang(points);
    assert(!result);
    printf("Test Case 2 Passed\n");
}

// Test case 3
void test_is_boomerang_3() {
    int points[3][2] = {{1, 1}, {2, 1}, {3, 1}};
    bool result = isBoomerang(points);
    assert(!result);
    printf("Test Case 3 Passed\n");
}

// Test case 4
void test_is_boomerang_4() {
    int points[3][2] = {{1, 1}, {1, 2}, {1, 3}};
    bool result = isBoomerang(points);
    assert(!result);
    printf("Test Case 4 Passed\n");
}

// Test case 5
void test_is_boomerang_5() {
    int points[3][2] = {{1, 1}, {1, 1}, {1, 1}};
    bool result = isBoomerang(points);
    assert(!result);
    printf("Test Case 5 Passed\n");
}

int main() {
    test_is_boomerang_1();
    test_is_boomerang_2();
    test_is_boomerang_3();
    test_is_boomerang_4();
    test_is_boomerang_5();

    return 0;
}
