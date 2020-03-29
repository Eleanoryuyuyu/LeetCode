from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) < 1 or len(grid[0]) < 1:
            return -1
        n = len(grid)
        queue = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
        if len(queue) < 1 or len(queue) == n*n:
            return -1
        res = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        while queue:
            res += 1
            l = len(queue)
            for _ in range(l):
                x, y = queue.pop(0)
                for i in range(4):
                    newx, newy = x + dx[i], y + dy[i]
                    if newx < 0 or newx >= n or newy < 0 or newy >= n:
                        continue
                    if grid[newx][newy] == 0:
                        queue.append((newx, newy))
                        grid[newx][newy] = 2
        return res -1

grid = [[1,0,1],[0,0,0],[1,0,1]]
print(Solution().maxDistance(grid))

