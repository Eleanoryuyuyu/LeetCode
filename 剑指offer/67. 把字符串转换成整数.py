# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if s == '0' or not s:
            return 0
        re = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        flag = 1
        sum = 0
        for i in range(len(s)):
            if i == 0 and s[i] == '+':
                flag = 1
            elif i == 0 and s[i] == '-':
                flag = -1
            else:
                if s[i] in re:
                    sum = sum * 10 + (ord(s[i]) - ord('0'))
                    if (flag == 1 and sum > 0x7FFFFFFF) or (flag == -1 and sum > 0x80000000):
                        return 0
                else:
                    return 0
        sum = sum * flag
        return sum


s = "+214748365"
print(Solution().StrToInt("-2147483649"))
