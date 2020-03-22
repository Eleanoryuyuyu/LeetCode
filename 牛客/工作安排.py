"""
美团
小美是团队的负责人，需要为团队制定工作的计划，以帮助团队产出最大的价值。

每周团队都会有两项候选的任务，其中一项为简单任务，一项为复杂任务，两项任务都能在一周内完成。第i周，团队完成简单任务的价值为li，完成复杂任务的价值为hi。由于复杂任务本身的技术难度较高，团队如果在第i周选择执行复杂任务的话，需要在i-1周不做任何任务专心准备。如果团队在第i周选择执行简单任务的话，不需要提前做任何准备。

现在小美的团队收到了未来N周的候选任务列表，请帮助小美确定每周的工作安排使得团队的工作价值最大。
"""


n = int(input())
works = []
for _ in range(n):
    work = list(map(int, input().split()))
    works.append(work)
dp = [[0] * 2 for _ in range(n)]
dp[0][0] = works[0][0]
dp[0][1] = works[0][1]
for i in range(1, n):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + works[i][0]
    if i == 1:
        dp[i][1] = works[i][1]
    else:
        dp[i][1] = max(dp[i-2][0], dp[i-2][1]) + works[i][1]
print(max(dp[n-1][0], dp[n-1][1]))
