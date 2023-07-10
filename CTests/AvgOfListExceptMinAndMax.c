#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>
#include <math.h>

float some_function(int salary[], int length) {
    int min_salary = salary[0];
    int max_salary = salary[0];
    int sum = 0;
    for (int i = 0; i < length; i++) {
        if (salary[i] < min_salary) {
            min_salary = salary[i];
        }
        if (salary[i] > max_salary) {
            max_salary = salary[i];
        }
        sum += salary[i];
    }
    return (float)(sum - min_salary - max_salary) / (length - 2);
}

void test_case_1() {
    int salary[] = {1000, 2000, 3000, 4000, 5000};
    float result = some_function(salary, 5);
    assert(result == 3000.0);
    printf("Test case 1 passed\n");
}

void test_case_2() {
    int salary[] = {500, 800, 1200, 1500};
    float result = some_function(salary, 4);
    assert(result == 1000.0);
    printf("Test case 2 passed\n");
}

void test_case_3() {
    int salary[] = {2500, 3500, 2000, 4500};
    float result = some_function(salary, 4);
    assert(result == 3000.0);
    printf("Test case 3 passed\n");
}

void test_case_4() {
    int salary[] = {10000, 15000, 12000, 9000, 18000};
    float result = some_function(salary, 5);
    float expected = 12333.333333333334;
    float tolerance = 1e-5;
    assert(fabs(result - expected) < tolerance);
    printf("Test case 4 passed\n");
}

void test_case_5() {
    int salary[] = {5000, 3000, 2000, 4000, 6000, 1000};
    float result = some_function(salary, 6);
    assert(result == 3500.0);
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
