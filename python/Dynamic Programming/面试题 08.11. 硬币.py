class Solution:
    def waysToChange(self, n: int) -> int:
        coins = [1, 5, 10, 25]
        dp = [1] + [0] * (n)
        for coin in coins:
            for i in range(coin, n+1):
                dp[i] += dp[i-coin]
        return int(dp[n] % (1e9 + 7))
print(Solution().waysToChange(5))