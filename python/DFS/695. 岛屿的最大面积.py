from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or len(grid)<1 or len(grid[0])<1:
            return 0
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                self.area = 0
                if grid[i][j] == 1:
                    self.dfs(grid, i, j, m, n)
                max_area = max(max_area, self.area)
        return max_area


    def dfs(self, grid, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
            return
        elif grid[i][j] == 1:
            self.area += 1
        grid[i][j] = 0
        self.dfs(grid, i-1, j, m, n)
        self.dfs(grid, i+1, j, m, n)
        self.dfs(grid, i, j-1, m, n)
        self.dfs(grid, i, j+1, m, n)

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(Solution().maxAreaOfIsland(grid))