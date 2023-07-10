#include <stdio.h>
#include <stdbool.h>
#include <assert.h>

bool checkStraightLine(int coordinates[][2], int size) {
    int x0 = coordinates[0][0];
    int y0 = coordinates[0][1];
    int x1 = coordinates[1][0];
    int y1 = coordinates[1][1];

    for (int i = 2; i < size; i++) {
        int x = coordinates[i][0];
        int y = coordinates[i][1];
        if ((x - x0) * (y1 - y0) != (y - y0) * (x1 - x0)) {
            return false;
        }
    }

    return true;
}

void test_straight_line() {
    int coordinates[][2] = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}};
    int size = sizeof(coordinates) / sizeof(coordinates[0]);
    bool result = checkStraightLine(coordinates, size);
    bool expected = true;
    assert(result == expected);
    printf("Test case 'straight_line' passed\n");
}

void test_not_straight_line() {
    int coordinates[][2] = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 7}};
    int size = sizeof(coordinates) / sizeof(coordinates[0]);
    bool result = checkStraightLine(coordinates, size);
    bool expected = false;
    assert(result == expected);
    printf("Test case 'not_straight_line' passed\n");
}

void test_collinear_points() {
    int coordinates[][2] = {{0, 0}, {1, 1}, {2, 2}, {3, 3}, {4, 4}};
    int size = sizeof(coordinates) / sizeof(coordinates[0]);
    bool result = checkStraightLine(coordinates, size);
    bool expected = true;
    assert(result == expected);
    printf("Test case 'collinear_points' passed\n");
}

void test_vertical_line() {
    int coordinates[][2] = {{1, 2}, {1, 3}, {1, 4}, {1, 5}, {1, 6}};
    int size = sizeof(coordinates) / sizeof(coordinates[0]);
    bool result = checkStraightLine(coordinates, size);
    bool expected = true;
    assert(result == expected);
    printf("Test case 'vertical_line' passed\n");
}

void test_horizontal_line() {
    int coordinates[][2] = {{1, 1}, {2, 1}, {3, 1}, {4, 1}, {5, 1}};
    int size = sizeof(coordinates) / sizeof(coordinates[0]);
    bool result = checkStraightLine(coordinates, size);
    bool expected = true;
    assert(result == expected);
    printf("Test case 'horizontal_line' passed\n");
}

int main() {
    test_straight_line();
    test_not_straight_line();
    test_collinear_points();
    test_vertical_line();
    test_horizontal_line();

    return 0;
}
