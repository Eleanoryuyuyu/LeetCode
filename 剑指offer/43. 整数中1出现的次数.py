# -*- coding:utf-8 -*-
class Solution:
    # 递推式： sum += (n // i*10) * i + i if (n % i *10) > (i*2 -1) elif (n % i * 10) < i ? 0 else (n % i * 10) -i + 1
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n < 1:
            return 0
        sum = 0
        i = 1
        while i <= n:
            driver = i * 10
            k = n % driver
            if k > i * 2 - 1:
                add_num = i
            elif k < i:
                add_num = 0
            else:
                add_num = k - i + 1
            sum += n // driver * i + add_num
            i *= 10
        return sum
print(Solution().NumberOf1Between1AndN_Solution(22))