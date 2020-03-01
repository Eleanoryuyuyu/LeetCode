def ZeroOnePack1(n, m, w, v):
    """
    dp[i][j]表示前i个物品的总体积为j的情况下的最大价值
    result = max(dp[n][0-V])
    dp[i][j]:
    1. 不选第i个物品，dp[i][j] = dp[i-1][j];
    2. 选第i个物品， dp[i][j] = dp[i-1][j-V[i]];
    dp[i][j] = max(1,2)
    dp[0][0] = 0
    """
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= w[i]:  # 如果当前物品的体积大于当前总体积j，则不可选
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w[i]] + v[i])
    result = max(dp[n])
    print(result)

def ZeroOnePack2(n, m, w, v):
    """
    :param n: n个物品
    :param m: 背包能承受的最大重量
    :param w: 物品的重量列表
    :param v: 物品的价值列表
    :return: 背包装的最大价值
    """
    """
    dp[j]：表示体积是j的情况下的最大价值
    """
    dp = [0]*(m+1)
    for i in range(1, n+1):
        for j in range(m, w[i]-1, -1):
            dp[j] = max(dp[j], dp[j-w[i]]+v[i])
    print(dp[m])

n, m = map(int, input().split())
w, v = [0] * (n + 1), [0] * (n + 1)
for i in range(1, n + 1):
    w[i], v[i] = map(int, input().split())
ZeroOnePack2(n,m,w,v)