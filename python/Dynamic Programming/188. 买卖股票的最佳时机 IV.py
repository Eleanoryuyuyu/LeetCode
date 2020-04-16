from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        if k >= len(prices)//2:
            return self._maxProfit(prices)
        dp = [[[0]*2 for _ in range(k+1)] for _ in range(len(prices))]
        dp[0][0][0], dp[0][0][1] = 0, -prices[0]
        for t in range(1, k+1):
            dp[0][t][0], dp[0][t][1] = float('-inf'), float('-inf')
        for i in range(1, len(prices)):
            for j in range(1, k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
        return dp[len(prices)-1][k][0]
    def _maxProfit(self, prices):
        res = 0
        for i in range(1, len(prices)):
            if prices[i]-prices[i-1] > 0:
                res += prices[i]-prices[i-1]
        return res

prices = [3,2,6,5,0,3]
print(Solution().maxProfit(2, prices))