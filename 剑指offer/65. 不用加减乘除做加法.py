# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2:
            sum = num1 ^ num2
            carray = (num1 & num2) << 1
            num1 = sum
            num2 = carray
        return num1

print(Solution().Add(5,17))
