# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 2:
            return number
        f1, f2, f3 = 1, 2, 3
        for _ in range(3, number+1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3