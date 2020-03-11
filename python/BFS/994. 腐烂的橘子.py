from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))

        def get_neighbor(r, c):
            for nr, nc in [((r - 1), c), ((r + 1), c), (r, (c - 1)), (r, (c + 1))]:
                if 0 <= nr <= rows - 1 and 0 <= nc <= cols - 1:
                    yield nr, nc

        d = 0
        while queue:
            r, c, d = queue.pop(0)
            for nr, nc in get_neighbor(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d + 1))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return d

    def orangesRotting2(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        queue = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
        level = 0
        while queue and count > 0:
            level += 1
            n = len(queue)
            for _ in range(n):
                r, c = queue.pop(0)
                if r > 0 and grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    count -= 1
                    queue.append((r-1, c))
                if r < rows-1 and grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                    count -= 1
                    queue.append((r+1, c))
                if c > 0 and grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    count -= 1
                    queue.append((r, c-1))
                if c < cols-1 and grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    count -= 1
                    queue.append((r, c+1))
        if count > 0:
            return -1
        return level
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting2(grid))