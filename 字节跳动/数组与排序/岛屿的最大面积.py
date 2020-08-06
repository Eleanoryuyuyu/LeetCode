from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.area = 0
                    self.dfs(grid, i, j, m, n)
                    if self.area > res:
                        res = self.area
        return res

    def dfs(self, grid, i, j, m, n):
        if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
            self.area += 1
            grid[i][j] = 0
            self.dfs(grid, i - 1, j, m, n)
            self.dfs(grid, i + 1, j, m, n)
            self.dfs(grid, i, j - 1, m, n)
            self.dfs(grid, i, j + 1, m, n)
        else:
            return


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(Solution().maxAreaOfIsland(grid))
