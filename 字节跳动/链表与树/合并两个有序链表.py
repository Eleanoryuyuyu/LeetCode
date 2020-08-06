class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        head = ListNode(0)
        l3 = head
        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        if l1:
            l3.next = l1
        elif l2:
            l3.next = l2
        return head.next
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = None
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l2.next.next.next = None

l3 = Solution().mergeTwoLists(l1, l2)
while l3:
    print(l3.val)
    l3 = l3.next

