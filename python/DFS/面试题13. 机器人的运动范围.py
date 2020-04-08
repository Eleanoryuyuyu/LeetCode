class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if k == 0 and m > 1 and n > 1:
            return 1
        visited = [[False] * n for _ in range(m) ]
        self.res = 0
        self.dfs(0, 0, m, n, visited, k)
        print(visited)
        return self.res
    def dfs(self, i, j, m, n, visited, k):
        if i >= 0 and i < m and j >= 0 and j < n and not visited[i][j] and self.check(i, j, k):
            visited[i][j] = True
            self.res += 1
        else:
            return
        self.dfs(i-1, j, m, n, visited, k)
        self.dfs(i+1, j, m, n, visited, k)
        self.dfs(i, j-1, m, n, visited, k)
        self.dfs(i, j+1, m, n, visited, k)
    def check(self, i, j, k):
        s = 0
        while i:
            s += i %10
            i = i //10
        while j:
            s += j % 10
            j = j // 10
        return s <= k

print(Solution().movingCount(3, 1, 0))