# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 7:
            return index
        res = [0] * index
        res[0] = 1
        t2, t3, t5 = 0, 0, 0
        for i in range(1, index):
            res[i] = min(res[t2]*2, res[t3]*3, res[t5]*5)
            if res[i] == res[t2]*2:
                t2 += 1
            if res[i] == res[t3]*3:
                t3 += 1
            if res[i] == res[t5]*5:
                t5 += 1
        return res[index -1]
print(Solution().GetUglyNumber_Solution(7))