# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        target = ListNode(0)
        pre = target
        target.next = head
        cur = head
        while cur.next:
            if n > 1:
                n -= 1
            else:
                target = target.next
            cur = cur.next
        target.next = target.next.next
        return pre.next


s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = None
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = None
new_head = s.removeNthFromEnd(head,2)
while head is not None:
    print(head.val)
    head = head.next
