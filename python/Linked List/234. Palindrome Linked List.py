class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        tmp = head
        while tmp:
            stack.append(tmp.val)
            tmp = tmp.next
        while head:
            cur = stack.pop()
            if head.val != cur:
                return False
            head = head.next
        return True

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = None
print(s.isPalindrome(head))