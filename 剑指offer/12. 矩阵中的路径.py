# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if len(matrix) < 1 or rows < 1 or cols < 1 or len(path) < 1:
            return False
        visited = [False] * rows * cols
        pathLength = 0
        for i in range(rows):
            for j in range(cols):
                if self.hasPathHelper(matrix, i, j, rows, cols, path, pathLength, visited):
                    return True
        return False

    def hasPathHelper(self, matrix, i, j, rows, cols, path, pathLength, visited):
        if pathLength == len(path):
            return True
        hasPath = False
        if 0 <= i < rows and 0 <= j < cols and matrix[i*cols+j] == path[pathLength] and not visited[i*cols+j]:
            pathLength += 1
            visited[i*cols+j] = True
            hasPath = self.hasPathHelper(matrix, i, j - 1, rows, cols, path, pathLength, visited) or \
                      self.hasPathHelper(matrix, i, j + 1, rows, cols, path, pathLength, visited) or \
                      self.hasPathHelper(matrix, i + 1, j, rows, cols, path, pathLength, visited) or \
                      self.hasPathHelper(matrix, i - 1, j, rows, cols, path, pathLength, visited)
            if not hasPath:
                pathLength -= 1
                visited[i*cols+j] = False
        return hasPath


matrix = "ABCESFCSADEE"
path = "ABCCED"

print(Solution().hasPath(matrix,3,4,path))
