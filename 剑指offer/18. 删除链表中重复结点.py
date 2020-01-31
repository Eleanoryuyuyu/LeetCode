# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return pHead
        newHead = ListNode(0)
        newHead.next = pHead
        pre = newHead
        cur = newHead.next
        while cur.next:
            tmp = cur.next
            if tmp.val == cur.val:
                while tmp and tmp.val == cur.val:
                    tmp = tmp.next
                cur = tmp
                pre.next = cur
                if cur == None:
                    break
            else:
                pre = pre.next
                cur = cur.next
        return newHead.next

pHead = ListNode(3)
pHead.next = ListNode(3)
pHead.next.next = ListNode(3)
pHead.next.next.next = ListNode(3)
pHead.next.next.next.next = None
# pHead.next.next.next.next = ListNode(4)
# pHead.next.next.next.next.next = ListNode(4)
# pHead.next.next.next.next.next.next = ListNode(5)
# pHead.next.next.next.next.next.next.next = None

s = Solution()
new_head = s.deleteDuplication(pHead)
while new_head:
    print(new_head.val)
    new_head = new_head.next