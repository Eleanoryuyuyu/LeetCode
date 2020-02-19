from typing import List
import sys
maxint = sys.maxsize

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1:
            return 0
        # dp[i][k][j] i表示第几天， k表示可以交易几次, j表示当前是否拥有股票
        dp = [[[0]*2 for _ in range(3)] for _ in range(len(prices))]
        dp[0][0][0], dp[0][0][1] = 0, -prices[0]
        dp[0][1][0], dp[0][1][1] = -maxint, -maxint
        dp[0][2][0], dp[0][2][1] = -maxint, -maxint

        for i in range(1,len(prices)):
            dp[i][0][0] = dp[i-1][0][0]
            dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][0][0]-prices[i])

            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][1]+prices[i])
            dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][1][0]-prices[i])

            dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][1][1] + prices[i])
        end = len(prices)-1
        return max(dp[end][0][0], dp[end][1][0], dp[end][2][0])

prices = [1,2,3,4,5]
print(Solution().maxProfit(prices))