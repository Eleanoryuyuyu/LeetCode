# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) < 5:
            return False
        numbers.sort()
        num_0, num_gap = 0, 0
        for i in numbers:
            if i == 0:
                num_0 += 1
        small = num_0
        big = small + 1
        while big < len(numbers):
            if numbers[small] == numbers[big]:
                return False
            num_gap += numbers[big] - numbers[small] - 1
            small = big
            big += 1
        if num_gap > num_0:
            return False
        else:
            return True

number = [0, 1, 3, 4, 5]
print(Solution().IsContinuous(number))