class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome1(self, head: ListNode) -> bool:
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

    def isPalindrome2(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        slow = head
        fast = head
        new_head = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        while head != slow:
            nxt = head.next
            head.next = new_head
            new_head = head
            head = nxt
        # 如果是奇数个结点，去掉后半部分第一个结点
        if fast is not None:
            slow = slow.next
        while slow:
            if slow.val != new_head.val:
                return False
            slow = slow.next
            new_head = new_head.next
        return True



s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
head.next.next.next.next = None
print(s.isPalindrome2(head))