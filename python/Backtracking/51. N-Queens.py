from typing import List


class Solution:
    # 时间复杂度O(n!)
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1:
            return []
        self.cols, self.pie, self.na = [], [], []
        self.result = []
        self.DFS(n, 0, [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in self.result]

    def DFS(self, n, row, cur_state):
        if row >= n:
            self.result.append(cur_state)
            return
        for col in range(n):
            if col in self.cols or row + col in self.pie or row - col in self.na:
                continue
            self.cols.append(col)
            self.pie.append(row + col)
            self.na.append(row - col)

            self.DFS(n, row + 1, cur_state + [col])

            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)


print(Solution().solveNQueens(8))
