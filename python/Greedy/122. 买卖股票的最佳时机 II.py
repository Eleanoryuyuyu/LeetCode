from typing import List


class Solution:
    # 1. 贪心法， 时间复杂度O(n)
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        sum = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                sum += prices[i + 1] - prices[i]
        return sum


prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [1, 2, 3, 4, 5]
prices3 = [7, 6, 3, 2]
print(Solution().maxProfit(prices2))
