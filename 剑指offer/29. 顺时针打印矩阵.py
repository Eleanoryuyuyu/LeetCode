# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if len(matrix) < 1:
            return []
        low = 0
        high = len(matrix)
        left = 0
        right = len(matrix[0])
        res = []
        while low < high and left < right:
            for j in range(left, right):
                res.append(matrix[low][j])
            for i in range(low + 1, high):
                res.append(matrix[i][right - 1])
            if low < high - 1:
                for j in range(right - 2, left - 1, -1):
                    res.append(matrix[high - 1][j])
            if left < right - 1:
                for i in range(high - 2, low, -1):
                    res.append(matrix[i][left])
            low += 1
            high -= 1
            left += 1
            right -= 1
        return res



matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
print(Solution().printMatrix(matrix))
