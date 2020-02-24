
# 1. 递归
"""
解析：当前处于cur位置，还剩rest步要走；1<=cur<=N
1. cur==1,那么下一步只能往右走，也就是走到2，还剩rest-1步；
2. cur==N,那么下一步只能往左走，也就是走到N-1，还剩rest-1步；
3. cur在中间位置，可以往左(cur-1)或者右走(cur+1),还剩rest-1步，
4.终止条件：rest==0,若定在p处，返回1表示能走到，返回0表示未走到；
"""
def robotWalk1(n, m, k, p):
    """
    :param n: 一共n个位置
    :param m: 开始位置
    :param k: 只能走的步数
    :param p: 最终到达的位置
    :return: 方案数
    """
    mod = 1e9 + 7
    if k == 0:
        return 1 if m == p else 0
    if m == 1:
        return int(robotWalk1(n, 2, k - 1, p) % mod)
    if m == n:
        return int(robotWalk1(n, n - 1, k - 1, p) % mod)
    return int(robotWalk1(n, m-1, k-1, p) % mod + robotWalk1(n, m+1, k-1, p) % mod)

# 2. 动态规划
def robotWalk2(n,m,k,p):
    mod = 1e9 + 7
    dp = [[0]*(n+1) for _ in range(k+1)]
    dp[0][p] = 1
    for step in range(1, k+1):
        for location in range(1, n+1):
            if location == 1:
                dp[step][location] = int(dp[step-1][2] % mod)
            elif location == n:
                dp[step][location] = int(dp[step-1][n-1] % mod)
            else:
                dp[step][location] = int((dp[step-1][location-1] + dp[step-1][location+1]) % mod)
    return int(dp[k][m] % mod)

def robotWalk3(n,m,k,p):
    mod = 1e9 + 7
    dp = [0]*(n+1)
    dp[p] = 1
    for i in range(1, k+1):
        leftUp = dp[1]
        for j in range(1, n+1):
            tmp = dp[j]
            if j == 1:
                dp[j] = int(dp[2] % mod)
            elif j == n:
                dp[j] = int(leftUp % mod)
            else:
                dp[j] = int(leftUp % mod + dp[j+1] % mod)
            leftUp = tmp
    return int(dp[m] % mod)

n,m,k,p = map(int, input().split())
print(robotWalk3(n,m,k,p))