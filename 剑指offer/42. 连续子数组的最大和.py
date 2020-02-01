# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return
        dp = [0]*len(array)
        sum = array[0]
        dp[0] = array[0]
        for i in range(1, len(array)):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + array[i]
            else:
                dp[i] = array[i]
            if dp[i] > sum:
                sum = dp[i]
        print(dp)
        return sum

array = [6, -3, -2, 7, -15, 1, 2, 2]
print(Solution().FindGreatestSumOfSubArray(array))