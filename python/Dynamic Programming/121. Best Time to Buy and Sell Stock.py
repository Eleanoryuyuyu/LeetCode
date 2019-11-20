from typing import List


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j] - prices[i] > 0:
                    profit = max(profit, prices[j] - prices[i])
        return profit

    def maxProfit2(self, prices: List[int]) -> int:
        if len(prices) < 1:
            return 0

        small = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] - small > profit:
                profit = prices[i] - small
            if prices[i] < small:
                small = prices[i]
        return profit



s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit2(prices))
