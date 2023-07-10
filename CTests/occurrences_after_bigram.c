#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// Function declaration
char** findOcurrences(const char* text, const char* first, const char* second, int* returnSize);

// Function implementation
char** findOcurrences(const char* text, const char* first, const char* second, int* returnSize) {
    const char* delimiter = " ";
    char* copy = strdup(text); // Make a copy of the text
    char* token = strtok(copy, delimiter);
    char** thirds = NULL;
    *returnSize = 0;

    while (token != NULL) {
        if (strcmp(token, first) == 0) {
            char* next = strtok(NULL, delimiter);
            if (next != NULL && strcmp(next, second) == 0) {
                char* third = strtok(NULL, delimiter);
                if (third != NULL) {
                    thirds = (char**)realloc(thirds, (*returnSize + 1) * sizeof(char*));
                    thirds[*returnSize] = strdup(third);
                    (*returnSize)++;
                }
            }
        }
        token = strtok(NULL, delimiter);
    }

    free(copy);
    return thirds;
}

// Test cases
void test_empty_text() {
    const char* text = "There";
    const char* first = "hello";
    const char* second = "world";
    int expectedSize = 0;
    char** expected = NULL;

    int returnSize;
    char** result = findOcurrences(text, first, second, &returnSize);

    printf("Test empty_text: ");
    if (returnSize == expectedSize) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }

    // Free memory
    for (int i = 0; i < returnSize; i++) {
        free(result[i]);
    }
    free(result);
}

void test_no_occurrences() {
    const char* text = "This is a sample sentence.";
    const char* first = "hello";
    const char* second = "world";
    int expectedSize = 0;
    char** expected = NULL;

    int returnSize;
    char** result = findOcurrences(text, first, second, &returnSize);

    printf("Test no_occurrences: ");
    if (returnSize == expectedSize) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }

    // Free memory
    for (int i = 0; i < returnSize; i++) {
        free(result[i]);
    }
    free(result);
}

void test_single_occurrence() {
    const char* text = "hello world hello there world";
    const char* first = "hello";
    const char* second = "world";
    int expectedSize = 1;
    char** expected = (char**)malloc(sizeof(char*) * expectedSize);
    expected[0] = strdup("hello");

    int returnSize;
    char** result = findOcurrences(text, first, second, &returnSize);

    printf("Test single_occurrence: ");
    if (returnSize == expectedSize) {
        int i;
        for (i = 0; i < returnSize; i++) {
            if (strcmp(result[i], expected[i]) != 0) {
                printf("FAILED\n");
                break;
            }
        }
        if (i == returnSize) {
            printf("PASSED\n");
        }
    } else {
        printf("FAILED\n");
    }

    // Free memory
    for (int i = 0; i < returnSize; i++) {
        free(result[i]);
    }
    free(result);
    for (int i = 0; i < expectedSize; i++) {
        free(expected[i]);
    }
    free(expected);
}

void test_multiple_occurrences() {
    const char* text = "hello world hello there world hello";
    const char* first = "hello";
    const char* second = "world";
    int expectedSize = 1;
    char** expected = (char**)malloc(sizeof(char*) * expectedSize);
    expected[0] = strdup("hello");

    int returnSize;
    char** result = findOcurrences(text, first, second, &returnSize);

    printf("Test multiple_occurrences: ");
    if (returnSize == expectedSize) {
        int i;
        for (i = 0; i < returnSize; i++) {
            if (strcmp(result[i], expected[i]) != 0) {
                printf("FAILED\n");
                break;
            }
        }
        if (i == returnSize) {
            printf("PASSED\n");
        }
    } else {
        printf("FAILED\n");
    }

    // Free memory
    for (int i = 0; i < returnSize; i++) {
        free(result[i]);
    }
    free(result);
    for (int i = 0; i < expectedSize; i++) {
        free(expected[i]);
    }
    free(expected);
}


int main() {
    test_consecutive_occurrences();
    test_multiple_occurrences();
    test_single_occurrence();
    test_no_occurrences();
    test_empty_text();
}
       
