class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

head = ListNode(3)
head.next = tmp = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(4)
head.next.next.next.next = tmp
res = Solution().detectCycle(head)
print(res.val)