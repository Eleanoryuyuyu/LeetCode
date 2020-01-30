# -*- coding:utf-8 -*-
class Solution:
    # 1. 动态规划
    def cutRope(self, number):
        # write code here
        if number < 2:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2
        dp = [0] * (number + 1)
        max = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        for i in range(4, number + 1):
            for j in range(1, number // 2 + 1):
                p = dp[j] * dp[i - j]
                if p > max:
                    max = p
            dp[i] = max
        return dp[number]

    # 2. 贪婪算法，尽量剪为长度为3的绳子，如果剩下的绳子长为4，则把长为4的绳子剪为2x2
    def cutRope2(self, number):
        if number < 2:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2
        timesOf3 = number // 3
        if number - timesOf3 * 3 == 1:
            timesOf3 -= 1
        timesOf2 = (number - timesOf3 * 3) // 2
        max = int(pow(3, timesOf3)) * int(pow(2, timesOf2))
        return max


print(Solution().cutRope2(8))
