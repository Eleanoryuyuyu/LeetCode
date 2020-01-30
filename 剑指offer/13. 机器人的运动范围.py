# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if rows < 1 or cols < 1:
            return 0
        visited = [False] * rows * cols
        count = self.countGrid(threshold, 0, 0, rows, cols, visited)
        return count

    def countGrid(self, k, i, j, rows, cols, visited):
        if i < 0 or i >= rows or j > 0 or j >= cols:
            return 0
        count = 0
        if self.check(k, i, j, rows, cols, visited):
            visited[i * cols + j] = True
            count += 1 + self.countGrid(k, i - 1, j, rows, cols, visited) + self.countGrid(k, i + 1, j, rows, cols,
                                                                                           visited) + \
                     self.countGrid(k, i, j - 1, rows, cols, visited) + self.countGrid(k, i, j + 1, rows, cols, visited)
        return count

    def check(self, k, i, j, rows, cols, visited):
        if 0 <= i < rows and 0 <= j < cols and not visited[i * cols + j] and self.getSum(i) + self.getSum(j) <= k:
            return True
        return False

    def getSum(self, num):
        sum = 0
        while num:
            sum += num % 10
            num = num // 10
        return sum

print(Solution().movingCount(35,37,18))