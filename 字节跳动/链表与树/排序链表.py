class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid, slow.next = slow.next, None
        left, right = self.sortList(head), self.sortList(mid)
        res = p = ListNode(0)
        while left and right:
            if left.val <= right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        p.next = left if left else right
        return res.next

l2 = ListNode(5)
l2.next = ListNode(9)
l2.next.next = ListNode(1)
l2.next.next.next = ListNode(2)
l2.next.next.next.next = ListNode(4)
l2.next.next.next.next.next = None

res = Solution().sortList(l2)
while res:
    print(res.val)
    res = res.next
