# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s or n == 0:
            return s
        item = s[:n]
        s += item
        s = s[n:]
        return s

s = "abcXYZdef"
print(Solution().LeftRotateString(s, 3))

