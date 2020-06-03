from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        m, n = len(matrix), len(matrix[0])
        layer = (min(m, n) + 1)//2
        for l in range(layer):
            start = l
            last_row = m - l - 1
            last_col = n - l - 1
            for j in range(start, last_col+1):
                res.append(matrix[start][j])
            for i in range(start+1, last_row + 1):
                res.append(matrix[i][last_col])
            if last_row != start and last_col != start:
                for j in range(last_col-1, start-1, -1):
                    res.append(matrix[last_row][j])
                for i in range(last_row-1, start, -1):
                    res.append(matrix[i][start])
        return res

matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

print(Solution().spiralOrder(matrix))
