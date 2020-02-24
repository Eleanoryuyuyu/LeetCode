def changeCoins2(n, coins, target):
    if n < 1 or len(coins)<1 or target < 0:
        return 0
    mod = 1e9 + 7
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(coins[i], target + 1):
            dp[j] = (dp[j] + dp[j - coins[i]]) % mod
    return dp[target]


n, target = map(int, input().split())
coins = list(map(int, input().split()))
print(changeCoins2(n,coins, target))