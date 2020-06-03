from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        loc = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    loc.append((i, j))
        while loc:
            row, col = loc.pop(0)
            for i in range(m):
                matrix[i][col] = 0
            for j in range(n):
                matrix[row][j] = 0
        print(matrix)
matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Solution().setZeroes(matrix)
