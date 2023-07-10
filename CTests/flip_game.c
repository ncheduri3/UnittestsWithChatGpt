#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <assert.h>

char** generatePossibleNextMoves(const char* currentState, int* returnSize) {
    int length = strlen(currentState);
    int maxStates = length / 2;
    char** result = (char**)malloc(sizeof(char*) * maxStates);
    *returnSize = 0;

    for (int i = 0; i < length - 1; i++) {
        if (currentState[i] == '+' && currentState[i + 1] == '+') {
            char* newState = (char*)malloc(sizeof(char) * (length + 1));
            strcpy(newState, currentState);
            newState[i] = '-';
            newState[i + 1] = '-';
            result[*returnSize] = newState;
            (*returnSize)++;
        }
    }

    return result;
}

void freeResult(char** result, int returnSize) {
    for (int i = 0; i < returnSize; i++) {
        free(result[i]);
    }
    free(result);
}

void test_no_moves() {
    const char* currentState = "--";
    int returnSize = 0;
    char** result = generatePossibleNextMoves(currentState, &returnSize);
    assert(returnSize == 0);
    freeResult(result, returnSize);
    printf("Test case 'no_moves' passed\n");
}

void test_single_move() {
    const char* currentState = "++-+";
    int returnSize = 0;
    char** result = generatePossibleNextMoves(currentState, &returnSize);
    assert(returnSize == 1);
    // assert(strcmp(result[0], "--+") == 0);
    assert(strcmp(result[0], "---+") == 0);
    freeResult(result, returnSize);
    printf("Test case 'single_move' passed\n");
}


void test_no_plus_signs() {
    const char* currentState = "--";
    int returnSize = 0;
    char** result = generatePossibleNextMoves(currentState, &returnSize);
    assert(returnSize == 0);
    freeResult(result, returnSize);
    printf("Test case 'no_plus_signs' passed\n");
}

int main() {
    test_no_moves();
    test_single_move();
    test_no_plus_signs();

    return 0;
}
