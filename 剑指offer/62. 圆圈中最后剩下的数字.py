# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return
        if n == 1:
            return n
        if m == 1:
            return n-1
        head = ListNode(0)
        p = head
        for i in range(1,n):
            p.next = ListNode(i)
            p = p.next
        p.next = head
        result = []
        while head.next != head:
            p = head
            for _ in range(m-2):
                p = p.next
            item = p.next
            result.append(item.val)
            p.next = item.next
            item.next = None
            head = p.next
        print(result)
        return head.val

    def LastRemaining_Solution2(self, n, m):
        if n < 1:
            return -1
        con = list(range(n))
        start = 0
        final = -1
        while con:
            k = (start + m -1)%n
            final = con.pop(k)
            n -= 1
            start = k
        return final


print(Solution().LastRemaining_Solution2(5, 3))