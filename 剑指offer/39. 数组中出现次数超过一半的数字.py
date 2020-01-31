# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if len(numbers) < 1:
            return 0
        left = 0
        right = len(numbers) - 1
        res = self.Helper(numbers, left, right)
        times = 0
        for i in range(len(numbers)):
            if numbers[i] == res:
                times += 1
        if times*2 < len(numbers):
            return 0
        return res

    def Helper(self, numbers, left, right):
        # write code here
        def Partition(left, right):
            pivot = numbers[left]
            while left < right:
                while left < right and numbers[right] >= pivot:
                    right -= 1
                numbers[left] = numbers[right]
                while left < right and numbers[left] <= pivot:
                    left += 1
                numbers[right] = numbers[left]
            numbers[left] = pivot
            return left

        index = Partition(left, right)
        if index == len(numbers) // 2:
            return numbers[index]
        elif index > len(numbers) // 2:
            return self.Helper(numbers, left, index-1)
        else:
            return self.Helper(numbers, index+1, right)

    def MoreThanHalfNum_Solution2(self, numbers):
        if len(numbers) < 1:
            return 0
        res = numbers[0]
        times = 1
        for i in range(1, len(numbers)):
            if times == 0:
                res = numbers[i]
                times = 1
            elif numbers[i] == res:
                times += 1
            else:
                times -= 1
        count = 0
        for n in numbers:
            if n == res:
                count += 1
        if count*2 < len(numbers):
            return 0
        return res



numbers = [1, 2, 3, 2, 2, 2, 5, 4, 2]
print(Solution().MoreThanHalfNum_Solution2(numbers))
