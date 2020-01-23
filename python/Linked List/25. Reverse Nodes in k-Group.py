# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        new_head = ListNode(0)
        new_head.next = head
        pre, end = new_head, new_head

        while end.next:
            i = 0
            while i < k and end != None:
                end = end.next
                i += 1
            if end == None:
                break
            start = pre.next
            nxt = end.next
            end.next = None
            pre.next = self.reverse(start)
            start.next = nxt
            pre = start
            end = pre
        return new_head.next

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def reverseKGroup2(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        new_head = ListNode(0)
        pre = new_head
        while True:
            count = k
            stack = []
            tmp = head
            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
            if count:
                pre.next = head
                break
            while stack:
                pre.next = stack.pop()
                pre = pre.next
            pre.next = tmp
            head = tmp
        return new_head.next



head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = None

new_head = Solution().reverseKGroup2(head, 3)
while new_head:
    print(new_head.val)
    new_head = new_head.next
