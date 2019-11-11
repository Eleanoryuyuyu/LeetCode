class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList1(self, head: ListNode) -> ListNode:
        new_head = None
        while head is not None:
            nex = head.next
            head.next = new_head
            new_head = head
            head = nex
        return new_head

    def reverseList2(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        else:
            #获取到反转后的新的头结点，不管具体内容，把整个从head->next看做一个整体
            new_head = self.reverseList2(head.next)
            # 将当前head指向的那个节点的下一个节点的下一个节点指向head，就把head和head.next的方向换过来了。
            head.next.next = head
            #然后把它自己本身的head.next设置为null，就好了。
            head.next = None
        return new_head



s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = None
new_head = s.reverseList2(head)
while new_head is not None:
    print(new_head.val)
    new_head = new_head.next