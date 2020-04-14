class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or l1.val == 0:
            return l2
        if not l2 or l2.val == 0:
            return l1
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        l3 = None
        flag = 0
        while stack1 and stack2:
            tmp = stack1.pop() + stack2.pop() + flag
            s = tmp % 10
            flag = tmp // 10
            node = ListNode(s)
            node.next = l3
            l3 = node
        while stack1:
            tmp = stack1.pop() + flag
            s = tmp % 10
            flag = tmp //10
            node = ListNode(s)
            node.next = l3
            l3 = node
        while stack2:
            tmp = stack2.pop() + flag
            s = tmp % 10
            flag = tmp //10
            node = ListNode(s)
            node.next = l3
            l3 = node
        if flag == 1:
            node = ListNode(flag)
            node.next = l3
            l3 = node
        return l3

l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)
l1.next.next.next.next = None
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = None
l3 = Solution().addTwoNumbers(l1, l2)
while l3:
    print(l3.val)
    l3 = l3.next

