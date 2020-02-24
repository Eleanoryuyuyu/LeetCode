
def changeCoin(coins, target):
    if len(coins)<1:
        return -1
    if target == 0:
        return 0
    dp = [target+1]*(target+1)
    dp[0] = 0
    for i in range(1,target+1):
        for j in range(len(coins)):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i-coins[j]]+1)
    return -1 if dp[target] > target else dp[target]

n, target = map(int, input().split())
coins = list(map(int, input().split()))
print(changeCoin(coins, target))
