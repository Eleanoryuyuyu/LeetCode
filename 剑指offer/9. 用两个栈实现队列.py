# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if self.stack1 and not self.stack2:
            while self.stack1:
                x = self.stack1.pop()
                self.stack2.append(x)
        if self.stack2:
            xx = self.stack2.pop()
            return xx
