# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 1. 使用栈，相当于从尾部开始遍历链表
    # 时间复杂度O(m+n)， 空间复杂度O(m+n)
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        stack1, stack2 = [], []
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next
        tmp = None
        while stack1 or stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if node1.val == node2.val:
                tmp = node1
            else:
                return tmp
        return None

    # 2. 先得到两链表的长度差，再比较结点
    # 时间复杂度O(m+n)， 空间复杂度O(1)
    def FindFirstCommonNode2(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        n = 0
        m = 0
        p1 = pHead1
        p2 = pHead2
        while p1:
            n += 1
            p1 = p1.next
        while p2:
            m += 1
            p2 = p2.next
        if n > m:
            b = n - m
            while b:
                pHead1 = pHead1.next
                b -= 1
        elif n < m:
            b = m - n
            while b:
                pHead2 = pHead2.next
                b -= 1
        while pHead1 and pHead2:
            if pHead1.val == pHead2.val:
                return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next
        return None

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(6)
head1.next.next.next.next = ListNode(7)
head1.next.next.next.next.next = None
head2 = ListNode(4)
head2.next = ListNode(5)
head2.next.next = ListNode(6)
head2.next.next.next = ListNode(7)
head2.next.next.next.next = None

print(Solution().FindFirstCommonNode2(head1, head2).val)