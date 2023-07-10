#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int maxProfit(int* prices, int pricesSize) {
    int left = 0;  // Buy
    int right = 1; // Sell
    int maxProfit = 0;

    while (right < pricesSize) {
        int currentProfit = prices[right] - prices[left]; // Current profit

        if (prices[left] < prices[right]) {
            maxProfit = (currentProfit > maxProfit) ? currentProfit : maxProfit;
        } else {
            left = right;
        }

        right++;
    }

    return maxProfit;
}

bool testProfitPossible() {
    int prices[] = {7, 1, 5, 3, 6, 4};
    int pricesSize = sizeof(prices) / sizeof(prices[0]);
    int expectedOutput = 5;
    int result = maxProfit(prices, pricesSize);
    if (result == expectedOutput) {
        printf("Profit Possible Case: Passed\n");
        return true;
    } else {
        printf("Profit Possible Case: Failed\n");
        return false;
    }
}

bool testNoProfitPossible() {
    int prices[] = {7, 6, 4, 3, 1};
    int pricesSize = sizeof(prices) / sizeof(prices[0]);
    int expectedOutput = 0;
    int result = maxProfit(prices, pricesSize);
    if (result == expectedOutput) {
        printf("No Profit Possible Case: Passed\n");
        return true;
    } else {
        printf("No Profit Possible Case: Failed\n");
        return false;
    }
}

bool testEmptyArray() {
    int prices[] = {};
    int pricesSize = 0;
    int expectedOutput = 0;
    int result = maxProfit(prices, pricesSize);
    if (result == expectedOutput) {
        printf("Empty Array Case: Passed\n");
        return true;
    } else {
        printf("Empty Array Case: Failed\n");
        return false;
    }
}

bool testSingleElementArray() {
    int prices[] = {5};
    int pricesSize = sizeof(prices) / sizeof(prices[0]);
    int expectedOutput = 0;
    int result = maxProfit(prices, pricesSize);
    if (result == expectedOutput) {
        printf("Single Element Array Case: Passed\n");
        return true;
    } else {
        printf("Single Element Array Case: Failed\n");
        return false;
    }
}

bool testConstantPrice() {
    int prices[] = {3, 3, 3, 3, 3};
    int pricesSize = sizeof(prices) / sizeof(prices[0]);
    int expectedOutput = 0;
    int result = maxProfit(prices, pricesSize);
    if (result == expectedOutput) {
        printf("Constant Price Case: Passed\n");
        return true;
    } else {
        printf("Constant Price Case: Failed\n");
        return false;
    }
}


int main() {
    bool success = true;
    success &= testProfitPossible();
    success &= testNoProfitPossible();
    success &= testEmptyArray();
    success &= testSingleElementArray();
    success &= testConstantPrice();

    if (success) {
        printf("All test cases passed!\n");
    } else {
        printf("Some test cases failed!\n");
    }

    return 0;
}
