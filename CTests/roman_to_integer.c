#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// Function declaration
int romanToInt(char* s);

// Function implementation
int romanToInt(char* s) {
    int length = strlen(s);
    int number = 0;
    
    for (int i = 0; i < length - 1; i++) {
        if (s[i] == 'I' && (s[i + 1] == 'V' || s[i + 1] == 'X')) {
            number -= 1;
        } else if (s[i] == 'X' && (s[i + 1] == 'L' || s[i + 1] == 'C')) {
            number -= 10;
        } else if (s[i] == 'C' && (s[i + 1] == 'D' || s[i + 1] == 'M')) {
            number -= 100;
        } else {
            switch (s[i]) {
                case 'I':
                    number += 1;
                    break;
                case 'V':
                    number += 5;
                    break;
                case 'X':
                    number += 10;
                    break;
                case 'L':
                    number += 50;
                    break;
                case 'C':
                    number += 100;
                    break;
                case 'D':
                    number += 500;
                    break;
                case 'M':
                    number += 1000;
                    break;
            }
        }
    }
    
    switch (s[length - 1]) {
        case 'I':
            number += 1;
            break;
        case 'V':
            number += 5;
            break;
        case 'X':
            number += 10;
            break;
        case 'L':
            number += 50;
            break;
        case 'C':
            number += 100;
            break;
        case 'D':
            number += 500;
            break;
        case 'M':
            number += 1000;
            break;
    }
    
    return number;
}

// Test cases
void test_single_roman_symbol() {
    char s[] = "X";
    int expected_output = 10;

    int result = romanToInt(s);

    printf("Test single_roman_symbol: ");
    if (result == expected_output) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_roman_symbols_in_ascending_order() {
    char s[] = "VII";
    int expected_output = 7;

    int result = romanToInt(s);

    printf("Test roman_symbols_in_ascending_order: ");
    if (result == expected_output) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_roman_symbols_in_descending_order() {
    char s[] = "IX";
    int expected_output = 9;

    int result = romanToInt(s);

    printf("Test roman_symbols_in_descending_order: ");
    if (result == expected_output) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

void test_roman_symbols_mixed_order() {
    char s[] = "MCMXCIV";
    int expected_output = 1994;

    int result = romanToInt(s);

    printf("Test roman_symbols_mixed_order: ");
    if (result == expected_output) {
        printf("PASSED\n");
    } else {
        printf("FAILED\n");
    }
}

int main() {
    test_single_roman_symbol();
    test_roman_symbols_in_ascending_order();
    test_roman_symbols_in_descending_order();
    test_roman_symbols_mixed_order();

    return 0;
}
