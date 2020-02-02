# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return ""
        stack = []
        item = ""
        for i in s:
            if i == " ":
                stack.append(item)
                stack.append(" ")
                item = ""
            else:
                item += i
        stack.append(item)
        res = ""
        while stack:
            res += stack.pop()
        return res

print(Solution().ReverseSentence("student a am I"))
