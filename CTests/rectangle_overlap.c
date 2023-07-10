#include <stdio.h>
#include <stdbool.h>

// Function declaration
bool isRectangleOverlap(int* rec1, int* rec2);

bool overlap(int a1, int a2, int b1, int b2) {
    if (a1 > b1) {
        int temp = a1;
        a1 = b1;
        b1 = temp;
        temp = a2;
        a2 = b2;
        b2 = temp;
    }

    if (a2 <= b1) {
        return false;
    } else {
        return true;
    }
}
// Function implementation
bool isRectangleOverlap(int* rec1, int* rec2) {
    int ax1 = rec1[0], ay1 = rec1[1], ax2 = rec1[2], ay2 = rec1[3];
    int bx1 = rec2[0], by1 = rec2[1], bx2 = rec2[2], by2 = rec2[3];



    if (!overlap(ax1, ax2, bx1, bx2) || !overlap(ay1, ay2, by1, by2)) {
        return false;
    } else {
        return true;
    }
}

// Test cases
void test_overlap() {
    int rec1[] = {0, 0, 2, 2};
    int rec2[] = {1, 1, 3, 3};

    bool result = isRectangleOverlap(rec1, rec2);

    printf("Test overlap: ");
    if (result) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_no_overlap() {
    int rec1[] = {0, 0, 1, 1};
    int rec2[] = {2, 2, 3, 3};

    bool result = isRectangleOverlap(rec1, rec2);

    printf("Test no_overlap: ");
    if (!result) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_partial_overlap() {
    int rec1[] = {0, 0, 2, 2};
    int rec2[] = {1, 1, 2, 3};

    bool result = isRectangleOverlap(rec1, rec2);

    printf("Test partial_overlap: ");
    if (result) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_same_rectangle() {
    int rec1[] = {0, 0, 2, 2};
    int rec2[] = {0, 0, 2, 2};

    bool result = isRectangleOverlap(rec1, rec2);

    printf("Test same_rectangle: ");
    if (result) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_single_point_overlap() {
    int rec1[] = {0, 0, 1, 1};
    int rec2[] = {1, 1, 2, 2};

    bool result = isRectangleOverlap(rec1, rec2);

    printf("Test single_point_overlap: ");
    if (!result) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_minimum_area_rectangle() {
    int rec1[] = {0, 0, 0, 0};
    int rec2[] = {0, 0, 0, 0};

    bool result = isRectangleOverlap(rec1, rec2);

    printf("Test minimum_area_rectangle: ");
    if (!result) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

int main() {
    test_overlap();
    test_no_overlap();
    test_partial_overlap();
    test_same_rectangle();
    test_single_point_overlap();
    test_minimum_area_rectangle();

    return 0;
}
