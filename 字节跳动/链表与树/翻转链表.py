# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        resHead = None
        while head:
            p = head.next
            head.next = resHead
            resHead = head
            head = p
        return resHead


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = None

res = Solution().reverseList(head)
while res:
    print(res.val)
    res = res.next
