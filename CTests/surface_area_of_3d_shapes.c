#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

int surfaceArea(int** grid, int gridSize, int* gridColSize);

// Function to calculate the surface area of the resulting shapes
int surfaceArea(int** grid, int gridSize, int* gridColSize) {
    int area = 0;
    for (int row = 0; row < gridSize; row++) {
        for (int col = 0; col < gridColSize[row]; col++) {
            if (grid[row][col]) {
                area += (grid[row][col] * 4) + 2;  // Surface area of each block if blocks weren't connected
                if (row > 0) {
                    area -= (grid[row][col] < grid[row - 1][col] ? grid[row][col] : grid[row - 1][col]) * 2;
                    // Subtracting shared area between adjacent blocks in the same column
                }
                if (col > 0) {
                    area -= (grid[row][col] < grid[row][col - 1] ? grid[row][col] : grid[row][col - 1]) * 2;
                    // Subtracting shared area between adjacent blocks in the same row
                }
            }
        }
    }
    return area;
}

// Test case 1
void test_surface_area_1() {
    int gridSize = 0;
    int* gridColSize = NULL;
    int** grid = NULL;
    int result = surfaceArea(grid, gridSize, gridColSize);
    assert(result == 0);
    printf("Test Case 1 Passed\n");
}

// Test case 2
void test_surface_area_2() {
    int gridSize = 1;
    int gridColSize[] = {1};
    int** grid = (int**)malloc(sizeof(int*) * gridSize);
    grid[0] = (int*)malloc(sizeof(int) * gridColSize[0]);
    grid[0][0] = 1;
    int result = surfaceArea(grid, gridSize, gridColSize);
    assert(result == 6);
    printf("Test Case 2 Passed\n");
}

// Test case 3
void test_surface_area_3() {
    int gridSize = 3;
    int gridColSize[] = {3, 3, 3};
    int** grid = (int**)malloc(sizeof(int*) * gridSize);
    for (int i = 0; i < gridSize; i++) {
        grid[i] = (int*)malloc(sizeof(int) * gridColSize[i]);
    }
    int values[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridColSize[i]; j++) {
            grid[i][j] = values[i][j];
        }
    }
    int result = surfaceArea(grid, gridSize, gridColSize);
    assert(result == 102);
    printf("Test Case 3 Passed\n");
}

// Test case 4
void test_surface_area_4() {
    int gridSize = 2;
    int gridColSize[] = {2, 2};
    int** grid = (int**)malloc(sizeof(int*) * gridSize);
    for (int i = 0; i < gridSize; i++) {
        grid[i] = (int*)malloc(sizeof(int) * gridColSize[i]);
    }
    int values[2][2] = {{0, 0}, {0, 0}};
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridColSize[i]; j++) {
            grid[i][j] = values[i][j];
        }
    }
    int result = surfaceArea(grid, gridSize, gridColSize);
    assert(result == 0);
    printf("Test Case 4 Passed\n");
}

// Test case 5
void test_surface_area_5() {
    int gridSize = 5;
    int gridColSize[] = {5, 5, 5, 5, 5};
    int** grid = (int**)malloc(sizeof(int*) * gridSize);
    for (int i = 0; i < gridSize; i++) {
        grid[i] = (int*)malloc(sizeof(int) * gridColSize[i]);
    }
    int values[5][5] = {{3, 2, 1, 0, 4}, {2, 5, 6, 7, 3}, {1, 0, 3, 4, 2}, {2, 1, 0, 3, 2}, {4, 3, 2, 1, 0}};
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridColSize[i]; j++) {
            grid[i][j] = values[i][j];
        }
    }
    int result = surfaceArea(grid, gridSize, gridColSize);
    assert(result == 164);
    printf("Test Case 5 Passed\n");
}

int main() {
    test_surface_area_1();
    test_surface_area_2();
    test_surface_area_3();
    test_surface_area_4();
    test_surface_area_5();

    return 0;
}