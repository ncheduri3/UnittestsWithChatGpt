#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

char* longestCommonPrefix(char** strs, int strsSize) {
    if (strsSize == 0)
        return "";

    int minLen = strlen(strs[0]);
    for (int i = 1; i < strsSize; i++) {
        int currLen = strlen(strs[i]);
        if (currLen < minLen)
            minLen = currLen;
    }

    char* result = (char*)malloc((minLen + 1) * sizeof(char));
    strncpy(result, strs[0], minLen);
    result[minLen] = '\0';

    for (int i = 1; i < strsSize; i++) {
        for (int j = 0; j < minLen; j++) {
            if (result[j] != strs[i][j]) {
                result[j] = '\0';
                minLen = j;
                break;
            }
        }
    }

    return result;
}

bool testLongestCommonPrefix(char** strs, int strsSize, const char* expected) {
    char* result = longestCommonPrefix(strs, strsSize);
    bool success = strcmp(result, expected) == 0;
    printf("Test Case: ");
    for (int i = 0; i < strsSize; i++) {
        printf("%s ", strs[i]);
    }
    printf("=> Expected: %s, Result: %s - %s\n", expected, result, success ? "Passed" : "Failed");
    free(result);
    return success;
}

void runTestCases() {
    // Test Case 1
    char* strs1[] = {"flower", "flow", "flight"};
    int strsSize1 = sizeof(strs1) / sizeof(strs1[0]);
    testLongestCommonPrefix(strs1, strsSize1, "fl");

    // Test Case 2
    char* strs2[] = {"dog", "racecar", "car"};
    int strsSize2 = sizeof(strs2) / sizeof(strs2[0]);
    testLongestCommonPrefix(strs2, strsSize2, "");

    // Test Case 3
    char* strs3[] = {"apple", "app", "application"};
    int strsSize3 = sizeof(strs3) / sizeof(strs3[0]);
    testLongestCommonPrefix(strs3, strsSize3, "app");

    // Add more test cases here
}

int main() {
    runTestCases();

    return 0;
}
