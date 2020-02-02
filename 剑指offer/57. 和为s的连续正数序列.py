# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum <= 2:
            return []
        left = 1
        right = 2
        result = []
        while left < (tsum + 1)//2:
            re = [i for i in range(left, right + 1)]
            s = sum(re)
            if s == tsum:
                result.append(re)
                right += 1
            elif s > tsum:
                left += 1
            else:
                right += 1
        return result
print(Solution().FindContinuousSequence(15))