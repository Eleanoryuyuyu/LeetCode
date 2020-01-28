# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False

    # 1. 利用下标
    def duplicate(self, numbers, duplication):
        # write code here
        if len(numbers) < 1 or len(duplication) < 1:
            return False
        for i in range(len(numbers)):
            while i != numbers[i]:
                if numbers[i] != numbers[numbers[i]]:
                    tmp = numbers[i]
                    numbers[i] = numbers[numbers[i]]
                    numbers[tmp] = tmp
                else:
                    duplication[0] = numbers[i]
                    return True
        return False

    # 2. 二分查找
    def duplicate2(self, numbers, duplication):
        if len(numbers) < 1 or len(duplication) < 1:
            return False
        start = min(numbers)
        end = len(numbers) - 1
        while (start <= end):
            mid = (end - start) // 2 + start
            count = self.countRange(numbers, start, mid)
            if start == end:
                if count > 1:
                    duplication[0] = start
                    return True
                else:
                    return False
            if count > (mid - start + 1):
                end = mid
            else:
                start = mid + 1


    def countRange(self, numbers, start, end):
        if len(numbers) < 1:
            return 0
        count = 0
        for i in range(len(numbers)):
            if numbers[i] >= start and numbers[i] <= end:
                count += 1
        return count


nums = [2, 3, 1, 0, 2, 5, 3]
dup = [-1]
print(Solution().duplicate2([2,1,3,1,4], dup))
