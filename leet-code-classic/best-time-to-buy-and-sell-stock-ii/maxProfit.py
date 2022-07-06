from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        res = 0
        for i in range(0, length - 1):
            profit = prices[i + 1] - prices[i]
            if profit > 0:
                res += profit
        return res
