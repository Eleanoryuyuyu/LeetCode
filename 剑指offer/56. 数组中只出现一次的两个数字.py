# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if len(array) < 1:
            return []
        flag = 0
        for i in array:
            flag ^= i
        flag = self.findIndexOf1(flag)
        num1, num2 = 0, 0
        for i in array:
            if self.findIndexOf1(i) == flag:
                num1 ^= i
            else:
                num2 ^= i
        return [num1, num2]
    def findIndexOf1(self, num):
        index = 0
        while num & 1 == 0:
            num = num >> 1
            index += 1
        return index



array = [2,4,3,6,3,2,5,5]
print(Solution().FindNumsAppearOnce(array))