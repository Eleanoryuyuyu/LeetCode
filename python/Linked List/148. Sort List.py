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

    def sortList2(self, head: ListNode) -> ListNode:
        def partition(head, end):
            if not head or not end or head == end:
                return
            l1 = head
            l2 = head.next
            pivot = head.val
            while l2 != end.next and l2:
                if l2.val < pivot:
                    l1 = l1.next
                    if l1 != l2:
                        tmp = l1.val
                        l1.val = l2.val
                        l2.val = tmp
                l2 = l2.next
            if head != l1:
                tmp = l1.val
                l1.val = head.val
                head.val = tmp
            return l1
        def sortHelper(head, end):
            if not head or not end or head == end:
                return
            node = partition(head, end)
            sortHelper(head, node)
            sortHelper(node.next, end)
            return head

        if not head or not head.next:
            return head
        end = head
        while end.next:
            end = end.next

        new_head = sortHelper(head, end)
        return new_head

s = Solution()
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
head.next.next.next.next = None
new_head = s.sortList2(head)
while new_head is not None:
    print(new_head.val)
    new_head = new_head.next
