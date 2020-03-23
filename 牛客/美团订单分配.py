"""
打车派单场景, 假定有N个订单， 待分配给N个司机。每个订单在匹配司机前，会对候选司机进行打分，打分的结果保存在N*N的矩阵A， 其中Aij 代表订单i司机j匹配的分值。

假定每个订单只能派给一位司机，司机只能分配到一个订单。求最终的派单结果，使得匹配的订单和司机的分值累加起来最大，并且所有订单得到分配。
"""

n = int(input())
order = []
for i in range(n):
    line = list(map(float, input().split()))
    order.append(line)
value = 0
def assign_order(order):
    res = []
    visited = [[0] * n] * n
    def dfs(cur, t, path):
        global value
        if cur > n-1:
            tmp = sum(t)
            if tmp > value:
                value = tmp
                res.append(path)
            return

        for i in range(n):
            if not visited[cur][i]:
                visited[cur][i] = 1
                dfs(cur + 1, t + [order[cur][i]], path+[i + 1])
                visited[cur][i] = 0
    dfs(0, [], [])
    print('{:.2f}'.format(value))
    for i in range(n):
        print('{} {}'.format(i+1, res[-1][i]))

assign_order(order)

