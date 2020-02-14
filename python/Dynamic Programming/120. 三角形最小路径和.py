from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) < 1 or len(triangle[0]) < 1:
            return 0
        rows = len(triangle)
        dp = []
        for i in range(rows):
            dp.append([0] * len(triangle[i]))
        dp[0][0] = triangle[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            cols = len(triangle[i])
            for j in range(1, cols-1):
                dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j])
            dp[i][cols - 1] = triangle[i][cols - 1] + dp[i-1][cols-2]

        return min(dp[rows - 1])
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        if len(triangle) < 1 or len(triangle[0]) < 1:
            return 0
        rows = len(triangle)
        dp = []
        for i in range(rows):
            dp.append([0]*len(triangle[i]))
        for j in range(len(triangle[rows - 1])):
            dp[rows - 1][j] = triangle[rows - 1][j]
        for i in range(rows - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]




tri = [[-1],
       [2,3],
       [1,-1,-3]]
print(Solution().minimumTotal2(tri))
