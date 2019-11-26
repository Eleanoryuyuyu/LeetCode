# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def mergeTwoList(L1, L2):
            if not L1:
                return L2
            if not L2:
                return L1
            newHead = ListNode(0)
            L3 = newHead
            while L1 and L2:
                if L1.val < L2.val:
                    L3.next = L1
                    L1 = L1.next
                else:
                    L3.next = L2
                    L2 = L2.next
                L3 = L3.next
            if L1:
                L3.next = L1
            else:
                L3.next = L2
            return newHead.next

        if not head or not head.next:
            return head
        slow = head
        quick = head
        while quick.next and quick.next.next:
            slow = slow.next
            quick = quick.next.next
        right = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(right)
        return mergeTwoList(left, right)

s = Solution()
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
head.next.next.next.next = None
new_head = s.sortList(head)
while new_head is not None:
    print(new_head.val)
    new_head = new_head.next
