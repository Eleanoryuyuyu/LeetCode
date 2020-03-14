from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j, m, n)
                    res += 1
        return res

    def dfs(self, grid, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i - 1, j, m, n)
        self.dfs(grid, i + 1, j, m, n)
        self.dfs(grid, i, j - 1, m, n)
        self.dfs(grid, i, j + 1, m, n)


grid = [['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']]
print(Solution().numIslands(grid))
