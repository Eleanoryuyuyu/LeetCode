# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        char_dic = {}
        for i in range(len(s)):
            if s[i] not in char_dic:
                char_dic[s[i]] = 1
            else:
                char_dic[s[i]] += 1
        for i in range(len(s)):
            if char_dic[s[i]] == 1:
                return i
        return -1
