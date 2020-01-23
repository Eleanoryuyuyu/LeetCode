# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 1. 非递归，时间复杂度O(n)，空间复杂度O(1)
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_head = ListNode(-1)
        new_head.next = head
        pre_node = new_head
        while head and head.next:
            first_node = head
            seconde_node = head.next

            # swap
            pre_node.next = seconde_node
            first_node.next = seconde_node.next
            seconde_node.next = first_node

            # move
            pre_node = first_node
            head = first_node.next
        return new_head.next

    # 2. 递归, 时间复杂度O(n)， 空间复杂度O(n)
    def swapPairs2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        first_node = head
        second_node = head.next

        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        return second_node


head =ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = None

s = Solution()
new_head = s.swapPairs2(head)
while new_head:
    print(new_head.val)
    new_head = new_head.next
