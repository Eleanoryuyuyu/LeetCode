# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        sum = 1
        if exponent < 0:
            base = 1/base
        for _ in range(abs(exponent)):
            sum = sum * base
        return sum

    def Power2(self, base, exponent):
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        if exponent == -1:
            return 1.0/base
        result = self.Power2(base, exponent >> 1)
        result = result * result
        if exponent & 0x1 == 1:
            result = result * base
        return result

print(Solution().Power2(2, -3))
