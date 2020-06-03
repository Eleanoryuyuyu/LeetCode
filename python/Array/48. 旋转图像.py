from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2 + n%2):
            for j in range(n//2):
                tmp = [0]*4
                row, col = i, j
                for k in range(4):
                    tmp[k] = matrix[row][col]
                    row, col = col, n -1 -row
                for k in range(4):
                    matrix[row][col] = tmp[(k-1)%4]
                    row, col = col, n - 1 - row
        print(matrix)

matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
Solution().rotate(matrix)