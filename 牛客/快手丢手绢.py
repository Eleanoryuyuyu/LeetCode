
def f():
    n = int(input())
    to = [int(item) - 1 for item in input().split()]
    in_degree = [0] * n
    for i in range(n):
        in_degree[to[i]] += 1
    stack = []
    for i in range(n):
        if in_degree[i] == 0:
            stack.append(i)
    while len(stack) != 0:
        top = stack[-1]
        in_degree[top] -= 1  # in_degree==-1,则代表删除了
        stack.pop(-1)
        in_degree[to[top]] -= 1
        if in_degree[to[top]] == 0:
            stack.append(to[top])
    min_num = 200000
    for i in range(n):
        if in_degree[i] == -1:
            continue
        else:
            start = i
            num = 1
            while to[i] != start:
                i = to[i]
                num += 1
                in_degree[i] = -1  # 同一个圈内的就不重复计算环了
            min_num = min(min_num, num)
    return min_num


ans = f()
print(ans)

