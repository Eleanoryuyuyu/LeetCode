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

    def mergeKLists3(self, lists):
        def mergeHelper(lists,left,right):
            if not lists:
                return None
            if len(lists) == 1:
                return lists[0]
            if len(lists) == 2:
                return merge(lists[0],lists[1])
            mid = (left + right) // 2
            leftLists = mergeHelper(lists[:mid],left, mid)
            rightLists = mergeHelper(lists[mid:], mid+1, right)
            return merge(leftLists,rightLists)
        def merge(left,right):
            if not left:
                return right
            if not right:
                return left
            result = ListNode(0)
            tmp = result
            while left and right:
                if left.val<right.val:
                    tmp.next = left
                    left = left.next
                else:
                    tmp.next = right
                    right = right.next
                tmp = tmp.next
            if left:
                tmp.next = left
            elif right:
                tmp.next = right
            return result.next

        return mergeHelper(lists, 0, len(lists) - 1)






h1 = ListNode(1)
h2 = ListNode(2)
h3 = ListNode(3)
h4 = ListNode(4)
h5 = ListNode(5)
h6 = ListNode(6)

l1 = h1
l1.next = h4
l1.next.next = h5
l1.next.next.next = None


l2 = h1
l2.next = h3
l2.next.next = h4
l2.next.next.next = None

l3 = h2
l3.next =h6
l3.next.next = None

lists = []
lists.append(l1)
lists.append(l2)
lists.append(l3)
s = Solution()
res = s.mergeKLists3(lists)


