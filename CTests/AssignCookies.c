#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>

int findContentChildren(int g[], int g_length, int s[], int s_length) {
    // Sort the arrays
    for (int i = 0; i < g_length - 1; i++) {
        for (int j = 0; j < g_length - i - 1; j++) {
            if (g[j] > g[j + 1]) {
                int temp = g[j];
                g[j] = g[j + 1];
                g[j + 1] = temp;
            }
        }
    }

    for (int i = 0; i < s_length - 1; i++) {
        for (int j = 0; j < s_length - i - 1; j++) {
            if (s[j] > s[j + 1]) {
                int temp = s[j];
                s[j] = s[j + 1];
                s[j + 1] = temp;
            }
        }
    }

    int g_index = g_length - 1;
    int s_index = s_length - 1;
    int res = 0;

    while (g_index >= 0 && s_index >= 0) {
        if (s[s_index] >= g[g_index]) {
            res++;
            s_index--;
        }
        g_index--;
    }

    return res;
}

void test_equal_sizes() {
    int g[] = {1, 2, 3};
    int s[] = {1, 2, 3};
    int g_length = sizeof(g) / sizeof(g[0]);
    int s_length = sizeof(s) / sizeof(s[0]);
    int expected = 3;
    int result = findContentChildren(g, g_length, s, s_length);
    assert(result == expected);
    printf("Test case 'equal_sizes' passed\n");
}

void test_more_cookies_than_children() {
    int g[] = {1, 2, 3};
    int s[] = {1, 2, 3, 4, 5};
    int g_length = sizeof(g) / sizeof(g[0]);
    int s_length = sizeof(s) / sizeof(s[0]);
    int expected = 3;
    int result = findContentChildren(g, g_length, s, s_length);
    assert(result == expected);
    printf("Test case 'more_cookies_than_children' passed\n");
}

void test_more_children_than_cookies() {
    int g[] = {1, 2, 3, 4, 5};
    int s[] = {1, 2, 3};
    int g_length = sizeof(g) / sizeof(g[0]);
    int s_length = sizeof(s) / sizeof(s[0]);
    int expected = 3;
    int result = findContentChildren(g, g_length, s, s_length);
    assert(result == expected);
    printf("Test case 'more_children_than_cookies' passed\n");
}

void test_no_cookies() {
    int g[] = {1, 2, 3};
    int s[] = {};
    int g_length = sizeof(g) / sizeof(g[0]);
    int s_length = sizeof(s) / sizeof(s[0]);
    int expected = 0;
    int result = findContentChildren(g, g_length, s, s_length);
    assert(result == expected);
    printf("Test case 'no_cookies' passed\n");
}

void test_no_children() {
    int g[] = {};
    int s[] = {1, 2, 3};
    int g_length = sizeof(g) / sizeof(g[0]);
    int s_length = sizeof(s) / sizeof(s[0]);
    int expected = 0;
    int result = findContentChildren(g, g_length, s, s_length);
    assert(result == expected);
    printf("Test case 'no_children' passed\n");
}

void test_empty_lists() {
    int g[] = {};
    int s[] = {};
    int g_length = sizeof(g) / sizeof(g[0]);
    int s_length = sizeof(s) / sizeof(s[0]);
    int expected = 0;
    int result = findContentChildren(g, g_length, s, s_length);
    assert(result == expected);
    printf("Test case 'empty_lists' passed\n");
}

int main() {
    test_equal_sizes();
    test_more_cookies_than_children();
    test_more_children_than_cookies();
    test_no_cookies();
    test_no_children();
    test_empty_lists();

    return 0;
}
