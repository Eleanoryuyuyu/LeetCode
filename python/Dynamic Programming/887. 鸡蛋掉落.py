class Solution:
    # 超时
    def superEggDrop(self, K: int, N: int) -> int:
        self.memo = dict()
        res = self.dp(K, N)
        return res

    def dp(self, K, N):
        if N == 0 or N == 1 or K == 1:
            return N
        if self.memo.get((K, N)):
            return self.memo[(K,N)]
        res = N
        for i in range(1, N+1):
            res = min(res, max(self.dp(K-1, i-1), self.dp(K, N-i)) + 1)
        self.memo[(K, N)] = res
        return res

    def superEggDrop2(self, K: int, N: int) -> int:
        dp = [0] * (K + 1)
        m = 0
        while dp[K] < N:
            m += 1
            for k in range(K, 0, -1):
                # print(m, k)
                dp[k] = dp[k - 1] + dp[k] + 1
        return m

print(Solution().superEggDrop(3,14))