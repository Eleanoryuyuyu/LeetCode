# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row = len(array)
        col = len(array[0])
        if row == 0:
            return False
        i = row-1
        j = 0
        while i >= 0 and j < col:
            if array[i][j] < target:
                j += 1
            elif array[i][j] > target:
                i -= 1
            else:
                return True
        return False


array = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]
target = 7
print(Solution().Find(target,array))