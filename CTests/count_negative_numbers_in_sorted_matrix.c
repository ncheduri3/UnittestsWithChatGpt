#include <stdio.h>
#include <stdbool.h>
#include <assert.h>

int countNegatives(int** grid, int gridSize, int* gridColSize) {
    int ROWS = gridSize;
    int COLS = *gridColSize;
    int negatives = 0;
    int col = 0;
    for (int row = ROWS - 1; row >= 0; row--) {
        while (col < COLS && grid[row][col] >= 0) {
            col++;
        }
        negatives += COLS - col;
    }
    return negatives;
}

void test_no_negatives() {
    int grid[3][3] = {
        {4, 3, 2},
        {3, 2, 1},
        {2, 1, 0}
    };
    int gridSize = 3;
    int gridColSize[3] = {3, 3, 3};
    int* gridPtr[3] = {grid[0], grid[1], grid[2]};
    int result = countNegatives(gridPtr, gridSize, gridColSize);
    int expected = 0;
    assert(result == expected);
    printf("Test case 'no_negatives' passed\n");
}

void test_all_negatives() {
    int grid[3][3] = {
        {-1, -2, -3},
        {-4, -5, -6},
        {-7, -8, -9}
    };
    int gridSize = 3;
    int gridColSize[3] = {3, 3, 3};
    int* gridPtr[3] = {grid[0], grid[1], grid[2]};
    int result = countNegatives(gridPtr, gridSize, gridColSize);
    int expected = 9;
    assert(result == expected);
    printf("Test case 'all_negatives' passed\n");
}

void test_mixed_negatives() {
    int grid[3][3] = {
        {4, 3, -2},
        {3, -5, -6},
        {-7, -8, -9}
    };
    int gridSize = 3;
    int gridColSize[3] = {3, 3, 3};
    int* gridPtr[3] = {grid[0], grid[1], grid[2]};
    int result = countNegatives(gridPtr, gridSize, gridColSize);
    int expected = 6;
    assert(result == expected);
    printf("Test case 'mixed_negatives' passed\n");
}

void test_large_grid() {
    int grid[3][5] = {
        {-1, -2, -3, -4, -5},
        {-6, -7, -8, -9, -10},
        {-11, -12, -13, -14, -15}
    };
    int gridSize = 3;
    int gridColSize[3] = {5, 5, 5};
    int* gridPtr[3] = {grid[0], grid[1], grid[2]};
    int result = countNegatives(gridPtr, gridSize, gridColSize);
    int expected = 15;
    assert(result == expected);
    printf("Test case 'large_grid' passed\n");
}

int main() {
    test_no_negatives();
    test_all_negatives();
    test_mixed_negatives();
    test_large_grid();

    return 0;
}
