
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 数学
    def lastRemaining(self, n: int, m: int) -> int:
        if n == 1:
            return 0
        if m == 1:
            return n-1
        res = 0
        for i in range(2, n + 1):
            res = (res + m) % i
        return res

    # 链表模拟， 会超时
    def lastRemaining2(self, n: int, m: int) -> int:
        if n == 1:
            return 0
        if m == 1:
            return n-1
        head = ListNode(0)
        node = head
        for i in range(1, n):
            node.next = ListNode(i)
            node = node.next
        node.next = head
        while head.next != head:
            tmp = head
            for _ in range(m-2):
                tmp = tmp.next
            drop = tmp.next
            tmp.next = drop.next
            drop.next = None
            head = tmp.next
        return head.val
print(Solution().lastRemaining(5, 3))