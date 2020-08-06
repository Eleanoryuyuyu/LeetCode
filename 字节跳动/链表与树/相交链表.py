class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        pa, pb = headA, headB
        lena, lenb = 0, 0
        while pa:
            pa = pa.next
            lena += 1
        while pb:
            pb = pb.next
            lenb += 1
        diff = lena - lenb
        if diff > 0:
            fast, slow = headA, headB
            for _ in range(diff):
                fast = fast.next
            while fast and slow:
                if fast == slow:
                    return slow
                fast = fast.next
                slow = slow.next

        elif diff < 0:
            fast, slow = headB, headA
            for _ in range(-diff):
                fast = fast.next
            while fast and slow:
                if fast == slow:
                    return slow
                fast = fast.next
                slow = slow.next

        else:
            pa, pb = headA, headB
            while pa and pb:
                if pa == pb:
                    return pa
                pa = pa.next
                pb = pb.next
        return None




l1 = ListNode(3)
l1.next = inter1 = ListNode(2)
l1.next.next = inter2 = ListNode(4)
l1.next.next.next = None
l2 = ListNode(0)
l2.next = ListNode(9)
l2.next.next = ListNode(1)
l2.next.next.next = inter1
l2.next.next.next.next = inter2
l2.next.next.next.next.next = None
node = Solution().getIntersectionNode(l1, l2)
print(node.val)
