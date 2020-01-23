class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 1. 快慢指针，空间复杂度O(1)
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    #2. 哈希表，空间复杂度O(n)
    def hasCycle(self, head: ListNode) -> bool:
        hash_set = set()
        while head:
            if head in hash_set:
                return True
            else:
                hash_set.add(head)
            head = head.next
        return False
