# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n <= 1:
            return n
        f0, f1, f2 = 0, 1, 1
        for _ in range(2, n+1):
            f2 = f0 + f1
            f0 = f1
            f1 = f2
        return f2

print(Solution().Fibonacci(3))