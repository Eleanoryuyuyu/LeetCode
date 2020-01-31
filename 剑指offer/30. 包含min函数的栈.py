# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.min_stack:
            self.min_stack.append(node)
        if node < self.min_stack[-1]:
            self.min_stack.append(node)
        else:
            tmp = self.min_stack[-1]
            self.min_stack.append(tmp)
    def pop(self):
        # write code here
        self.stack.pop()
        self.min_stack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.min_stack[-1]

s = Solution()
s.push(3)
print(s.min())
s.push(4)
print(s.min())
s.push(2)
print(s.min())
s.push(1)
print(s.min())
s.pop()
print(s.min())
s.pop()
print(s.min())
print(s.top())
s.push(0)
print(s.min())
