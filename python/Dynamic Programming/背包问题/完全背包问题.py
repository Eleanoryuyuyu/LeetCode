def CompletePack1(n,m,w,v):
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j]
            if j >= w[i]:
                dp[i][j] = max(dp[i][j], dp[i][j-w[i]] + v[i])
    return max(dp[n])

def CompletePack2(n,m,w,v):
    dp = [0]*(m+1) # 表示体积小于等于j的情况下背包的最大价值，
                   # 如果只有dp[0]=0,其余初始化为负无穷，则表示体积为j的背包的最大价值
    for i in range(1, n+1):
        for j in range(w[i],m+1):
            dp[j] = max(dp[j], dp[j-w[i]]+v[i])
    return dp


n, m = map(int, input().split())
w, v = [0] * (n + 1), [0] * (n + 1)
for i in range(1, n + 1):
    w[i], v[i] = map(int, input().split())
print(CompletePack2(n,m,w,v))