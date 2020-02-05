class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return 0
        self.cols, self.pie, self.na = [], [], []
        self.result = 0
        self.DFS(n, 0, [])
        return self.result
    def DFS(self, n, row, cur_state):
        if row >= n:
            self.result += 1
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


print(Solution().totalNQueens(4))