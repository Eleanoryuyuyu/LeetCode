import heapq
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists) :
        lists = [node for node in lists if node]
        lists = sorted(lists, key=lambda x: x.val)
        head = ListNode(0)
        tmp = head

        for node in lists:
            tmp.next = node
            tmp = node

        return head.next

    def mergeKLists2(self,lists):
        h = []
        for head in lists:
            node = head
            while node:
                h.append(node.val)
                node = node.next
        if not h:
            return None
        heapq.heapify(h)
        root = ListNode(heapq.heappop(h))
        curNode = root
        while h :
            nextNode = ListNode(heapq.heappop(h))
            curNode.next = nextNode
            curNode = nextNode
        return root

h1 = ListNode(1)
h2 = ListNode(2)
h3 = ListNode(3)
h4 = ListNode(4)
h5 = ListNode(5)
h6 = ListNode(6)
l1 = h1
l1.next = h4
h4.next = h5


l2 = h1
l2.next = h3
h3.next = h4

l3 = h2
h2.next =h6
lists = []
lists.append(l1)
lists.append(l2)
lists.append(l3)
s = Solution()
res = s.mergeKLists(lists)


