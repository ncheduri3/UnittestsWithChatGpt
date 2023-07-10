#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// Function declaration
bool areSentencesSimilar(char** sentence1, int sentence1Size, char** sentence2, int sentence2Size, char*** similarPairs, int similarPairsSize, int* similarPairsColSize);

// Function to check if two sentences are similar
bool areSentencesSimilar(char** sentence1, int sentence1Size, char** sentence2, int sentence2Size, char*** similarPairs, int similarPairsSize, int* similarPairsColSize) {
    if (sentence1Size != sentence2Size) {
        return false;
    }

    for (int i = 0; i < sentence1Size; i++) {
        if (strcmp(sentence1[i], sentence2[i]) != 0) {
            bool similar = false;
            for (int j = 0; j < similarPairsSize; j++) {
                if ((strcmp(similarPairs[j][0], sentence1[i]) == 0 && strcmp(similarPairs[j][1], sentence2[i]) == 0) ||
                    (strcmp(similarPairs[j][0], sentence2[i]) == 0 && strcmp(similarPairs[j][1], sentence1[i]) == 0)) {
                    similar = true;
                    break;
                }
            }
            if (!similar) {
                return false;
            }
        }
    }

    return true;
}

// Test cases
void test_equal_sentences() {
    char* sentence1[] = {"Hello", "World"};
    int sentence1Size = sizeof(sentence1) / sizeof(sentence1[0]);

    char* sentence2[] = {"Hello", "World"};
    int sentence2Size = sizeof(sentence2) / sizeof(sentence2[0]);

    char** similarPairs = NULL;
    int similarPairsSize = 0;
    int similarPairsColSize = 0;

    bool result = areSentencesSimilar(sentence1, sentence1Size, sentence2, sentence2Size, (char***)similarPairs, similarPairsSize, &similarPairsColSize);

    printf("Test equal_sentences: ");
    if (result) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_similar_pairs() {
    char* sentence1[] = {"Hello", "World"};
    int sentence1Size = sizeof(sentence1) / sizeof(sentence1[0]);

    char* sentence2[] = {"Hola", "Mundo"};
    int sentence2Size = sizeof(sentence2) / sizeof(sentence2[0]);

    char* similarPairs[][2] = {{"Hello", "Hola"}, {"World", "Mundo"}};
    int similarPairsSize = sizeof(similarPairs) / sizeof(similarPairs[0]);
    int similarPairsColSize = 2;

    bool result = areSentencesSimilar(sentence1, sentence1Size, sentence2, sentence2Size, (char***)similarPairs, similarPairsSize, &similarPairsColSize);

    printf("Test similar_pairs: ");
    if (result) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_no_similar_pairs() {
    char* sentence1[] = {"Hello", "World"};
    int sentence1Size = sizeof(sentence1) / sizeof(sentence1[0]);

    char* sentence2[] = {"Hola", "Mundo"};
    int sentence2Size = sizeof(sentence2) / sizeof(sentence2[0]);

    char*** similarPairs = NULL;
    int similarPairsSize = 0;
    int similarPairsColSize = 0;

    bool result = areSentencesSimilar(sentence1, sentence1Size, sentence2, sentence2Size, similarPairs, similarPairsSize, &similarPairsColSize);

    printf("Test no_similar_pairs: ");
    if (!result) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_mismatched_lengths() {
    char* sentence1[] = {"Hello", "World"};
    int sentence1Size = sizeof(sentence1) / sizeof(sentence1[0]);

    char* sentence2[] = {"Hello"};
    int sentence2Size = sizeof(sentence2) / sizeof(sentence2[0]);

    char*** similarPairs = NULL;
    int similarPairsSize = 0;
    int similarPairsColSize = 0;

    bool result = areSentencesSimilar(sentence1, sentence1Size, sentence2, sentence2Size, similarPairs, similarPairsSize, &similarPairsColSize);

    printf("Test mismatched_lengths: ");
    if (!result) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_empty_sentences() {
    char** sentence1 = NULL;
    int sentence1Size = 0;

    char** sentence2 = NULL;
    int sentence2Size = 0;

    char*** similarPairs = NULL;
    int similarPairsSize = 0;
    int similarPairsColSize = 0;

    bool result = areSentencesSimilar(sentence1, sentence1Size, sentence2, sentence2Size, similarPairs, similarPairsSize, &similarPairsColSize);

    printf("Test empty_sentences: ");
    if (result) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

int main() {
    test_equal_sentences();
    test_no_similar_pairs();
    test_mismatched_lengths();
    test_empty_sentences();

}