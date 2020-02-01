class Solution:
    def getMaxValue(self, values):
        rows = len(values)
        cols = len(values[0])
        if rows < 1:
            return 0
        dp = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                up = dp[i-1][j] if i > 0 else 0
                left = dp[i][j - 1] if j > 0 else 0
                dp[i][j] = values[i][j] + max(up, left)
        return dp[rows - 1][cols - 1]

values = [[1, 10, 3, 8],
          [12, 2, 9, 6],
          [5, 7, 4, 11],
          [3, 7, 16, 5]]
print(Solution().getMaxValue(values))