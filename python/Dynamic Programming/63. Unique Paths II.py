class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
                break
            else:
                dp[i][0] = 1
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                dp[0][i] = 0
                break
            else:
                dp[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] if obstacleGrid[i][j] == 0 else 0
        print(dp)
        return dp[m - 1][n - 1]


s = Solution()
# grid = [
#     [0, 0, 0],
#     [0, 1, 0],
#     [0, 0, 0]
# ]

grid = [[1,0]]
print(s.uniquePathsWithObstacles(grid))
