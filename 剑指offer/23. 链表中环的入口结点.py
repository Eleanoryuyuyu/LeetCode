# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead:
            return None
        slow = pHead
        fast = pHead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                fast = pHead
                while fast != slow:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

pHead = ListNode(1)
pHead.next = ListNode(2)
tmp = ListNode(3)
pHead.next.next = tmp
tmp.next = ListNode(4)
pHead.next.next.next.next = ListNode(5)
pHead.next.next.next.next.next = ListNode(6)
pHead.next.next.next.next.next.next = tmp

e = Solution().EntryNodeOfLoop(pHead)
print(e.val)