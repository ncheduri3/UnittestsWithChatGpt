#include <stdio.h>
#include <stdbool.h>
#include <assert.h>
#include <math.h>

float largestTriangleArea(int points[][2], int n) {
    float area = 0;
    for (int i = 0; i < n; i++) {
        int x1 = points[i][0];
        int y1 = points[i][1];
        for (int j = i + 1; j < n; j++) {
            int x2 = points[j][0];
            int y2 = points[j][1];
            for (int k = j + 1; k < n; k++) {
                int x3 = points[k][0];
                int y3 = points[k][1];
                float curr = fabs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)));
                if (curr > area) {
                    area = curr;
                }
            }
        }
    }
    return area;
}

void test_valid_triangle_area() {
    int points[][2] = {{0, 0}, {0, 1}, {1, 0}};
    int n = sizeof(points) / sizeof(points[0]);
    float result = largestTriangleArea(points, n);
    assert(fabs(result - 0.5) < 0.000001);
    printf("Test case 'valid_triangle_area' passed\n");
}

void test_zero_area() {
    int points[][2] = {{0, 0}, {0, 0}, {0, 0}};
    int n = sizeof(points) / sizeof(points[0]);
    float result = largestTriangleArea(points, n);
    assert(fabs(result) < 0.000001);
    printf("Test case 'zero_area' passed\n");
}

void test_large_triangle_area() {
    int points[][2] = {{-50, -50}, {0, 0}, {50, -50}, {0, 25}};
    int n = sizeof(points) / sizeof(points[0]);
    float result = largestTriangleArea(points, n);
    assert(fabs(result - 3750) < 0.000001);
    printf("Test case 'large_triangle_area' passed\n");
}

void test_single_point() {
    int points[][2] = {{0, 0}};
    int n = sizeof(points) / sizeof(points[0]);
    float result = largestTriangleArea(points, n);
    assert(fabs(result) < 0.000001);
    printf("Test case 'single_point' passed\n");
}

void test_minimum_points() {
    int points[][2] = {{0, 0}, {1, 1}, {2, 2}};
    int n = sizeof(points) / sizeof(points[0]);
    float result = largestTriangleArea(points, n);
    assert(fabs(result) < 0.000001);
    printf("Test case 'minimum_points' passed\n");
}

int main() {
    test_valid_triangle_area();
    test_zero_area();
    test_large_triangle_area();
    test_single_point();
    test_minimum_points();
    return 0;
}
