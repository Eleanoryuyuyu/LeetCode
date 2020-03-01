def MultiplePack(n,m,w,v,num):
    dp = [0]*(m+1)
    for i in range(1, n+1):
        for j in range(m, 0, -1):
            for k in range(1,num[i]+1):
                if k * w[i] <= j:
                    dp[j] = max(dp[j], dp[j-k*w[i]] + k*v[i])
    return dp[m]


n, m = map(int, input().split())
w, v, num = [0] * (n + 1), [0] * (n + 1), [0]*(n+1)
for i in range(1, n + 1):
    w[i], v[i], num[i] = map(int, input().split())
print(MultiplePack(n,m,w,v,num))
