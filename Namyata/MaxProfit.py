# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



import unittest

def maxProfit(prices):
    left = 0  # Buy
    right = 1  # Sell
    max_profit = 0
    while right < len(prices):
        current_profit = prices[right] - prices[left]  # our current Profit
        if prices[left] < prices[right]:
            max_profit = max(current_profit, max_profit)
        else:
            left = right
        right += 1
    return max_profit

class MaxProfitTestCase(unittest.TestCase):
    def test_profit_possible(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected_output = 5
        self.assertEqual(maxProfit(prices), expected_output)

    def test_no_profit_possible(self):
        prices = [7, 6, 4, 3, 1]
        expected_output = 0
        self.assertEqual(maxProfit(prices), expected_output)

    def test_empty_array(self):
        prices = []
        expected_output = 0
        self.assertEqual(maxProfit(prices), expected_output)

    def test_single_element_array(self):
        prices = [5]
        expected_output = 0
        self.assertEqual(maxProfit(prices), expected_output)

    def test_constant_price(self):
        prices = [3, 3, 3, 3, 3]
        expected_output = 0
        self.assertEqual(maxProfit(prices), expected_output)

if __name__ == '__main__':
    unittest.main()
