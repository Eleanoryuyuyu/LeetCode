# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        elif not pHead2:
            return pHead1
        else:
            newHead  = ListNode(0)
            pHead3 = newHead
            while pHead1 and pHead2:
                if pHead1.val < pHead2.val:
                    pHead3.next = pHead1
                    pHead1 = pHead1.next
                else:
                    pHead3.next = pHead2
                    pHead2 = pHead2.next
                pHead3 = pHead3.next
            if pHead1:
                pHead3.next = pHead1
            elif pHead2:
                pHead3.next = pHead2
            return newHead.next

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = None

head2 = ListNode(2)
head2.next = ListNode(3)
head2.next.next = ListNode(4)
head2.next.next.next = None

newHead = Solution().Merge(head1, head2)
while newHead:
    print(newHead.val)
    newHead = newHead.next
