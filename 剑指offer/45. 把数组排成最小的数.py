# -*- coding:utf-8 -*-
import functools
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return None

        def cmp(x, y):
            if x + "" + y < y + "" + x:
                return -1
            elif x + "" + y == y + "" + x:
                return 0
            else:
                return 1

        numbers = list(map(str, numbers))
        new_numbers = sorted(numbers, key=functools.cmp_to_key(cmp))
        re = "".join(new_numbers)
        return re


numbers = [3, 32, 321]
print(Solution().PrintMinNumber(numbers))
