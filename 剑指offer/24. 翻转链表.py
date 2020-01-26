# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    # 1. 非递归
    def ReverseList(self, pHead):
        newHead = None
        cur = pHead
        while cur:
            nxt = cur.next
            cur.next = newHead
            newHead = cur
            cur = nxt
        return newHead

    # 2. 递归
    def ReverseList2(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        else:
            newHead = self.ReverseList2(pHead.next)
            pHead.next.next = pHead
            pHead.next = None
        return newHead

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = None

newHead = s.ReverseList2(head)
while newHead:
    print(newHead.val)
    newHead = newHead.next
