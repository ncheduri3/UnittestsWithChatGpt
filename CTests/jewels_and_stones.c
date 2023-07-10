#include <stdio.h>
#include <stdbool.h>
#include <assert.h>
#include <string.h>

int numJewelsInStones(const char* jewels, const char* stones) {
    int counter = 0;
    int jewelsLen = strlen(jewels);
    int stonesLen = strlen(stones);

    for (int i = 0; i < stonesLen; i++) {
        for (int j = 0; j < jewelsLen; j++) {
            if (stones[i] == jewels[j]) {
                counter++;
                break;
            }
        }
    }

    return counter;
}

void test_all_jewels_in_stones() {
    const char* jewels = "abc";
    const char* stones = "aaaabbbccc";
    int result = numJewelsInStones(jewels, stones);
    int expected = 10;
    assert(result == expected);
    printf("Test case 'all_jewels_in_stones' passed\n");
}

void test_no_jewels_in_stones() {
    const char* jewels = "abc";
    const char* stones = "def";
    int result = numJewelsInStones(jewels, stones);
    int expected = 0;
    assert(result == expected);
    printf("Test case 'no_jewels_in_stones' passed\n");
}

void test_some_jewels_in_stones() {
    const char* jewels = "abc";
    const char* stones = "aadefbcc";
    int result = numJewelsInStones(jewels, stones);
    int expected = 5;
    assert(result == expected);
    printf("Test case 'some_jewels_in_stones' passed\n");
}

void test_empty_stones() {
    const char* jewels = "abc";
    const char* stones = "";
    int result = numJewelsInStones(jewels, stones);
    int expected = 0;
    assert(result == expected);
    printf("Test case 'empty_stones' passed\n");
}

void test_empty_jewels() {
    const char* jewels = "";
    const char* stones = "abcdef";
    int result = numJewelsInStones(jewels, stones);
    int expected = 0;
    assert(result == expected);
    printf("Test case 'empty_jewels' passed\n");
}

int main() {
    test_all_jewels_in_stones();
    test_no_jewels_in_stones();
    test_some_jewels_in_stones();
    test_empty_stones();
    test_empty_jewels();

    return 0;
}
