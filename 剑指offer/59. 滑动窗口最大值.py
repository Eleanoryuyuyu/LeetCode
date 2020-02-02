class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if len(num) < 1 or size <1:
            return []
        queue = []
        result = []
        for i in range(len(num)):
            while queue and num[i] > num[queue[-1]]:
                queue.pop()
            queue.append(i)
            if i >= size-1:
                result.append(num[queue[0]])
            if i - size + 1 == queue[0]:
                queue.pop(0)
        return result

num = [2, 3, 4, 2, 6, 2, 5, 1]
print(Solution().maxInWindows(num, 3))

