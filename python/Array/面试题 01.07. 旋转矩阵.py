from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) < 1 or len(matrix[0])<1:
            return
        n = len(matrix)
        for i in range(n//2):
            for j in range(i,n-i-1):
                matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1], matrix[n-j-1][i] = \
                    matrix[n-j-1][i], matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1]
        print(matrix)


matrix = [[ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]]
Solution().rotate(matrix)
