
import sys
n = int(input())
grid = []
for i in range(3):
    line = list(map(int, input().split()))
    grid.append(line)

dp = [[sys.maxsize]*n for _ in range(3)]
dp[0][0], dp[1][0], dp[2][0] = 0, 0, 0
for i in range(1,n):
    for k in range(3):
        for j in range(3):
            dp[k][i] = min(dp[k][i], dp[j][i-1] + abs(grid[j][i-1]-grid[k][i]))
res = min(dp[0][n-1], min(dp[1][n-1], dp[2][n-1]))
print(res)