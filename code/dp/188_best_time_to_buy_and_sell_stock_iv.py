"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        length = len(prices)
        if length < 2:
            return 0
        max_profit = 0
        # if k>= n/2, then it can't complete k transactions. The problem becomes buy-and-sell problem 2
        if k >= length / 2:
            for i in range(1, length):
                max_profit += max(prices[i] - prices[i - 1], 0)
            return max_profit

        # max_global[i][j] is to store the maximum profit, at day j, and having i transactions already
        # max_local[i][j] is to store the maximum profit at day j, having i transactions already, and having transaction at day j
        max_global = [[0] * length for _ in range(k + 1)]
        max_local = [[0] * length for _ in range(k + 1)]

        # i indicates the transaction times, j indicates the times
        for j in range(1, length):
            cur_profit = prices[j] - prices[j - 1]  # variable introduced by the current day transaction
            for i in range(1, k + 1):
                max_local[i][j] = max(max_global[i - 1][j - 1] + max(cur_profit, 0), max_local[i][j - 1] + cur_profit)
                max_global[i][j] = max(max_global[i][j - 1], max_local[i][j])

        return max_global[k][-1]  # the last day, the last transaction