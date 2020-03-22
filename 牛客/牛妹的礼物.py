class Solution:
    def selectPresent(self , presentVolumn ):
        if len(presentVolumn) < 1 or len(presentVolumn[0]) < 1:
            return 0
        n, m = len(presentVolumn), len(presentVolumn[0])
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = presentVolumn[0][0]
        for i in range(1, n):
            dp[i][0] = presentVolumn[i][0] + dp[i-1][0]
        for j in range(1, m):
            dp[0][j] = presentVolumn[0][j] + dp[0][j-1]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + presentVolumn[i][j]
        return dp[n-1][m-1]

print(Solution().selectPresent([[1,2,3],[2,3,4]]))