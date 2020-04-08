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
        tmp = res
        flag = 0
        while l1 and l2:
            s = l1.val + l2.val + flag
            flag = s//10
            s = s%10
            tmp.next = ListNode(s)
            tmp = tmp.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            s = l1.val + flag
            flag = s//10
            s = s%10
            tmp.next = ListNode(s)
            tmp = tmp.next
            l1 = l1.next
        while l2:
            s = l2.val + flag
            flag = s // 10
            s = s % 10
            tmp.next = ListNode(s)
            tmp = tmp.next
            l2 = l2.next
        if flag != 0:
            tmp.next = ListNode(flag)
        return res.next

l1 = ListNode(4)
l1.next = ListNode(3)
l1.next.next = ListNode(2)
l1.next.next.next = ListNode(1)
l1.next.next.next.next = None
l2 = ListNode(9)
l2.next = ListNode(8)
l2.next.next = ListNode(7)
l2.next.next.next = None

res = Solution().addTwoNumbers(l1, l2)
while res:
    print(res.val)
    res = res.next


