# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        if not array:
            return array
        i = 0
        while i < len(array):
            if array[i] & 0x1 == 0:
                j = i + 1
                while j < len(array) and array[j] & 0x1 == 0:
                    j += 1
                if j == len(array):
                    break
                tmp = array[j]
                while j > i:
                    array[j] = array[j-1]
                    j -= 1
                array[i] = tmp
            i += 1
        return array


array = [1, 2, 3, 4, 5]
print(Solution().reOrderArray(array))
