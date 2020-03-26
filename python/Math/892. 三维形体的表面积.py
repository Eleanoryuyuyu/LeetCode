from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) < 1 or len(grid[0]) < 1:
            return 0
        n = len(grid)
        res = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    res += 2
                for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    if 0 <= nr < n and 0 <= nc < n:
                        nvalue = grid[nr][nc]
                    else:
                        nvalue = 0
                    res += max(grid[r][c]-nvalue, 0)
        return res
grid = [[1, 0], [0, 2]]
print(Solution().surfaceArea(grid))