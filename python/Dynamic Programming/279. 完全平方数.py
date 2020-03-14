class Solution:
    # 动态规划
    # 1. 初始化数组 dp = [0,1,2,...,n] 长度为n+1，表示每个数最多由多少个1组成，比如2=1+1
    # 2. 遍历所有小于平方数小于i的数j，dp[i] = min(dp[i], dp[i-j*j]+1)
    # 时间复杂度O(n*sqrt{n})，空间复杂度O(n)
    def numSquares1(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = i
            for j in range(1, int(i**0.5)+1):
                dp[i] = min(dp[i], dp[i-j*j]+1)
        return dp[-1]
    # BFS，顺序遍历每一层，每一层的节点都根节点减去平方数的差，当节点差出现0时，此时为最短路径。
    def numSquares2(self, n: int) -> int:
        if n == 0:
            return 0
        queue = [n]
        visited = set()
        step = 0
        while queue:
            step += 1
            level_len = len(queue)
            for _ in range(level_len):
                cur = queue.pop(0)
                for j in range(1, int(cur**0.5)+1):
                    x = cur - j*j
                    if x == 0:
                        return step
                    if x not in visited:
                        queue.append(x)
                        visited.add(x)
        return step


print(Solution().numSquares2(5))