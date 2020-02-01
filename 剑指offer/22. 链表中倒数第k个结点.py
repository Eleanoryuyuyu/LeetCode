# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if not head or k == 0:
            return None
        slow = head
        fast = head
        for i in range(k-1):
            if fast.next:
                fast = fast.next
            else:
                return None
        while fast.next:
            slow = slow.next
            fast = fast.next
        return slow

pHead = ListNode(1)
pHead.next = ListNode(2)
pHead.next.next = ListNode(3)
pHead.next.next.next = ListNode(4)
pHead.next.next.next.next = ListNode(5)
pHead.next.next.next.next.next = ListNode(6)
pHead.next.next.next.next.next.next = None

p = Solution().FindKthToTail(pHead, 3)
print(p.val)