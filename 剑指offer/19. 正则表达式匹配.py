# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if not s and not pattern:
            return True
        return self.matchHelper(s, pattern, 0, 0)

    def matchHelper(self, s, pattern, i, j):
        if i == len(s) and j == len(pattern):
            return True
        if i != len(s) and j == len(pattern):
            return False
        if j+1 < len(pattern) and pattern[j + 1] == '*':
            if (i != len(s) and s[i] == pattern[j]) or (pattern[j] == '.' and i != len(s)):
                return self.matchHelper(s, pattern, i + 1, j + 2) or \
                       self.matchHelper(s, pattern, i + 1, j) or \
                       self.matchHelper(s, pattern, i, j + 2)
            else:
                return self.matchHelper(s, pattern, i, j + 2)
        if (i != len(s) and s[i] == pattern[j]) or (pattern[j] == '.' and i != len(s)-1):
            return self.matchHelper(s, pattern, i + 1, j + 1)
        return False

print(Solution().match("",".*"))