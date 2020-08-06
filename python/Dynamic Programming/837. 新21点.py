class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0 or N >= K + W - 1:
            return 1.0
        dp = [0.0] * (K + W)
        for i in range(K, N+1):
            dp[i] = 1.0
        S = N - K + 1
        for i in range(K-1, -1, -1):
            dp[i] = S / float(W)
            S += dp[i] - dp[i + W]
        return dp[0]

print(Solution().new21Game(21, 17, 10))