# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    # 1. 栈
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        stack = []
        res = []
        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next
        while stack:
            tmp = stack.pop()
            res.append(tmp)
        return res
    # 2. 递归
    def printListFromTailToHead2(self, listNode):
        def printNodeHelper(listNode):
            if listNode.next:
                printNodeHelper(listNode.next)
            res.append(listNode.val)

        if not listNode:
            return []
        res = []
        printNodeHelper(listNode)
        return res


s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = None

res = s.printListFromTailToHead2(head)
print(res)