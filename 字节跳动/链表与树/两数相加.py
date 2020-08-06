# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        res = ListNode(0)
        l3 = res
        flag = 0
        while l1 and l2:
            cur = l1.val + l2.val + flag
            flag = cur // 10
            l3.next = ListNode(cur % 10)
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            cur = l1.val + flag
            flag = cur //10
            l3.next = ListNode(cur % 10)
            l3 = l3.next
            l1 = l1.next
        while l2:
            cur = l2.val + flag
            flag = cur //10
            l3.next = ListNode(cur % 10)
            l3 = l3.next
            l2 = l2.next
        if flag != 0:
            l3.next = ListNode(flag)
        return res.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.next.next.next = None

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = None

l3 = Solution().addTwoNumbers(l1, l2)
while l3:
    print(l3.val)
    l3 = l3.next