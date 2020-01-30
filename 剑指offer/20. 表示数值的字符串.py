# -*- coding:utf-8 -*-
import re


class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        try:
            ss = float(s)
            print(ss)
            return True
        except:
            return False

    def isNumeric2(self, s):
        return re.match(r"^[\+\-]?\d*(\.\d+)?([eE][\+\-]?\d+)?$", s)


print(Solution().isNumeric2("100"))
